from typing import Any, cast, override
import grpc
from grpc import ServicerContext
from concurrent import futures
from dotenv import load_dotenv
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
import os

from booking_pb2 import (
    CancelBookingRequest,
    CreateBookingRequest,
    CreateBookingResponse,
    CreateHotelEntryRequest,
    CreateHotelEntryResponse,
    CreateRoomsRequest,
    Empty,
    GetBookingRequest,
    GetBookingResponse,
    GetRoomsRequest,
    GetRoomsResponse,
    ListCustomerBookingsRequest,
    ListCustomerBookingsResponse,
    RoomInfo,
    UpdateBookingRequest,
    UpdateBookingResponse,
    UpdateHotelEntryRequest,
    UpdateHotelEntryResponse,
)
from booking_pb2_grpc import (
    BookingServiceServicer,
    add_BookingServiceServicer_to_server,
)


# Load environment variables from .env file
_ = load_dotenv()

# PostgreSQL connection details
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

SERVICE_PORT = os.getenv("SERVICE_PORT")

# Path to the migration SQL file
MIGRATION_FILE = "migrations.sql"

try:
    conn: psycopg.Connection = psycopg.connect(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres")
    conn.autocommit = True
    conn.execute(f"CREATE DATABASE {DB_NAME}")
    conn.close()
    print("DB CREATED")
except:
    print("DB ALREADY EXISTS")

class BookingServiceImpl(BookingServiceServicer):
    def __init__(self):
        self.pool: ConnectionPool = ConnectionPool(
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        self.run_migrations()

    def run_migrations(self):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                with open(MIGRATION_FILE, "r") as f:
                    migration_sql = f.read()
                    cur.execute(migration_sql)
                    print("MIGRATION SUCCESSFUL")

    @override
    def CreateHotelEntry(self, request: CreateHotelEntryRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                row = cur.execute("""
                    INSERT INTO HOTELS (
                        total_rooms,
                        room_types,
                        address,
                        phone,
                        website
                    ) VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    returning hotel_id;
                """, (request.total_rooms, request.room_types, request.address, request.phone, request.website)).fetchone()

                assert row is not None
                response = CreateHotelEntryResponse(hotel_id=cast(int, row[0]))

                return response

    @override
    def UpdateHotelEntry(self, request: UpdateHotelEntryRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                query = "UPDATE HOTELS SET"
                values: list[Any] = []
                if request.total_rooms != None:
                    query += " total_rooms = %s,"
                    values.append(request.total_rooms)
                if request.room_types != None:
                    query += " room_types = %s,"
                    values.append(request.room_types)
                if request.address != None:
                    query += " address = %s,"
                    values.append(request.address)
                if request.phone != None:
                    query += " phone = %s,"
                    values.append(request.phone)
                if request.website != None:
                    query += " phone = %s,"
                    values.append(request.website)

                query = query.strip(',') + "WHERE hotel_id = %s"

                if len(values) > 0:
                    row = cur.execute(query, values + [request.hotel_id]).fetchone()
                    assert row is not None
                    response = UpdateHotelEntryResponse(hotel_id=cast(int, row[0]))
                else:
                    response = UpdateHotelEntryResponse(hotel_id=request.hotel_id)

                return response

    @override
    def CreateBooking(self, request: CreateBookingRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                row = cur.execute("""
                INSERT INTO BOOKINGS (
                    customer_name,
                    customer_email,
                    room_id, 
                    check_in_date,
                    check_out_date,
                    num_guests,
                    transaction_id
                ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
                )
                returning booking_id;
                """, 
                (
                    request.customer_name, 
                    request.customer_email, 
                    request.room_id, 
                    request.check_in_date, 
                    request.check_out_date, 
                    request.num_guests,
                    request.transaction_id
                )).fetchone()
                _ = cur.execute("UPDATE ROOMS SET available = %s WHERE room_id = %s", [False, request.room_id])

                assert row is not None
                return CreateBookingResponse(booking_id=row[0])

    @override
    def UpdateBooking(self, request: UpdateBookingRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                query = "UPDATE bookings SET"
                values: list[Any] = []
                
                # Build update fields
                update_parts = []
                if request.customer_name not in [None, ""]:
                    update_parts.append(" customer_name = %s")
                    values.append(request.customer_name)
                if request.customer_email not in [None, ""]:
                    update_parts.append(" customer_email = %s")
                    values.append(request.customer_email)
                if request.room_id > 0:
                    update_parts.append(" room_id = %s")
                    values.append(request.room_id)
                    cur_room = cur.execute("SELECT room_id FROOM bookings WHERE booking_id = %s", [request.booking_id]).fetchone()
                    assert cur_room is not None
                    _ = cur.execute("UPDATE ROOMS SET available = %s WHERE room_id = %s", [False, cur_room])
                    _ = cur.execute("UPDATE ROOMS SET available = %s WHERE room_id = %s", [True, request.room_id])
                if request.check_in_date not in [None, ""]:
                    update_parts.append(" check_in_date = %s")
                    values.append(request.check_in_date)
                if request.check_out_date not in [None, ""]:
                    update_parts.append(" check_out_date = %s")
                    values.append(request.check_out_date)
                if request.num_guests > 0:
                    update_parts.append(" num_guests = %s")
                    values.append(request.num_guests)
                # if request.cancelled is not False:
                #     update_parts.append(" cancelled = %s")
                #     values.append(request.cancelled)
                
                # If no fields to update, just return the original booking_id
                if not update_parts:
                    return UpdateBookingResponse(booking_id=request.booking_id)
                
                # Construct final query
                query += ",".join(update_parts)
                query += " WHERE booking_id = %s RETURNING booking_id"
                values.append(request.booking_id)
                
                try:
                    row = cur.execute(query, values).fetchone()
                    if row is None:
                        context.abort(grpc.StatusCode.NOT_FOUND, "Booking not found")
                    return UpdateBookingResponse(booking_id=row[0])
                except Exception as e:
                    context.abort(grpc.StatusCode.INTERNAL, f"Database error: {str(e)}")

    @override
    def GetBooking(self, request: GetBookingRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                row = cur.execute("SELECT * FROM bookings WHERE booking_id = %s;", (request.booking_id,)).fetchone()
                if row is None:
                    context.abort(grpc.StatusCode.NOT_FOUND, "Booking not found")
                assert row is not None
                
                # Explicitly create the response with proper type conversions
                return GetBookingResponse(
                    booking_id=int(row['booking_id']),
                    customer_name=str(row['customer_name']),
                    customer_email=str(row['customer_email']),
                    room_id=row['room_id'],
                    check_in_date=str(row['check_in_date']),
                    check_out_date=str(row['check_out_date']),
                    num_guests=int(row['num_guests']),
                    cancelled=bool(row.get('cancelled', False)),  # Default to False if not in DB
                    transaction_id=int(row.get('transaction_id', 0))
                )

    def CancelBooking(self, request: CancelBookingRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                _ = cur.execute("UPDATE BOOKINGS SET cancelled = %s WHERE booking_id = %s returning booking_id;", (True, request.booking_id))
                return Empty()

    def ListCustomerBookings(self, request: ListCustomerBookingsRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                row = map(lambda r: GetBookingResponse(
                    booking_id=int(r['booking_id']),
                    customer_name=str(r['customer_name']),
                    customer_email=str(r['customer_email']),
                    room_id=r['room_id'],
                    check_in_date=str(r['check_in_date']),
                    check_out_date=str(r['check_out_date']),
                    num_guests=int(r['num_guests']),
                    cancelled=bool(r.get('cancelled', False)),  # Default to False if not in DB
                    transaction_id=int(r.get('transaction_id', 0)),
                    room_number=int(r['room_number'])
                ), 
                          cur.execute("SELECT * FROM bookings inner join rooms on bookings.room_id = rooms.room_id WHERE customer_email = %s AND rooms.hotel_id = %s;", [request.customer_email, request.hotel_id])
                        .fetchall())
                return ListCustomerBookingsResponse(bookings=row)

    def CreateRooms(self, request: CreateRoomsRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                values = []
                for room in request.rooms:
                    values.append((room.hotel_id, room.room_number, room.room_type, room.price_per_night))

                if len(values) > 0:
                    _ = cur.executemany("""
                    INSERT INTO ROOMS (
                        hotel_id,
                        room_number,
                        room_type,
                        price_per_night
                    ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s
                    );
                    """, values)

                return Empty()
    
    def GetRooms(self, request: GetRoomsRequest, context: ServicerContext):
        with self.pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                rows = cur.execute("SELECT * FROM rooms WHERE hotel_id = %s", (request.hotel_id,)).fetchall()
            
                # Convert database rows to RoomInfo messages
                room_infos = []
                for row in rows:
                    room_info = RoomInfo(
                        room_id=row['room_id'],
                        room_number=row['room_number'],
                        hotel_id=row['hotel_id'],
                        room_type=str(row['room_type']),  # Assuming room_type is string in proto
                        price_per_night=float(row['price_per_night']),
                        available=bool(row.get('available', True))  # Default to True if not in DB
                    )
                    room_infos.append(room_info)
                
                return GetRoomsResponse(rooms=room_infos)
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BookingServiceServicer_to_server(BookingServiceImpl(), server)
    server.add_insecure_port(f"[::]:{SERVICE_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
