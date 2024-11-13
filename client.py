import grpc
import booking_pb2
import booking_pb2_grpc
from dotenv import load_dotenv
import os

_ = load_dotenv()

SERVICE_PORT = os.getenv("SERVICE_PORT")
assert SERVICE_PORT is not None

class BookingServiceClient:
    def __init__(self, host="localhost", port=SERVICE_PORT):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = booking_pb2_grpc.BookingServiceStub(self.channel)

    def create_hotel(self, name, total_rooms, room_types, address, phone, website):
        request = booking_pb2.CreateHotelEntryRequest(
            hotel_name=name,
            total_rooms=total_rooms,
            room_types=room_types,
            address=address,
            phone=phone,
            website=website
        )
        response = self.stub.CreateHotelEntry(request)
        return response.hotel_id

    def create_rooms(self, rooms_data):
        rooms = []
        for room in rooms_data:
            rooms.append(booking_pb2.CreateRoomsInner(
                hotel_id=room['hotel_id'],
                room_number=room['room_number'],
                room_type=room['room_type'],
                price_per_night=room['price_per_night']
            ))
        request = booking_pb2.CreateRoomsRequest(rooms=rooms)
        return self.stub.CreateRooms(request)

    def get_rooms(self, hotel_id, check_in_date, check_out_date):
        request = booking_pb2.GetRoomsRequest(hotel_id=hotel_id, check_in_date=check_in_date, check_out_date=check_out_date)
        response = self.stub.GetRooms(request)
        return response.rooms

    def create_booking(self, customer_name, customer_email, room_id, 
                      check_in_date, check_out_date, num_guests, transaction_id):
        request = booking_pb2.CreateBookingRequest(
            customer_name=customer_name,
            customer_email=customer_email,
            room_id=room_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            num_guests=num_guests,
            transaction_id=transaction_id
        )
        response = self.stub.CreateBooking(request)
        return response.booking_id

    def get_booking(self, booking_id):
        request = booking_pb2.GetBookingRequest(booking_id=booking_id)
        response = self.stub.GetBooking(request)
        return response

    def update_booking(self, booking_id, **kwargs):
        request = booking_pb2.UpdateBookingRequest(booking_id=booking_id, **kwargs)
        response = self.stub.UpdateBooking(request)
        return response.booking_id

    def cancel_booking(self, booking_id):
        request = booking_pb2.CancelBookingRequest(booking_id=booking_id)
        _ = self.stub.CancelBooking(request)

    def list_customer_bookings(self, customer_email, hotel_id):
        request = booking_pb2.ListCustomerBookingsRequest(customer_email=customer_email, hotel_id=hotel_id)
        response = self.stub.ListCustomerBookings(request)
        return response.bookings

def main():
    # Create client instance
    client = BookingServiceClient()

    try:
        # 1. Create a hotel
        hotel_id = client.create_hotel(
            name="Grand Hotel",
            total_rooms=4,
            room_types=2,
            address="123 Main St",
            phone="555-0123",
            website="www.grandhotel.com"
        )
        print(f"Created hotel with ID: {hotel_id}")

        # 2. Create rooms
        rooms_data = [
            {
                "hotel_id": hotel_id,
                "room_number": 101,
                "room_type": 1,
                "price_per_night": 150.0
            },
            {
                "hotel_id": hotel_id,
                "room_number": 102,
                "room_type": 1,
                "price_per_night": 150.0
            },
            {
                "hotel_id": hotel_id,
                "room_number": 201,
                "room_type": 2,
                "price_per_night": 300.0
            },
            {
                "hotel_id": hotel_id,
                "room_number": 202,
                "room_type": 2,
                "price_per_night": 300.0
            },
        ]
        client.create_rooms(rooms_data)
        print("Created rooms successfully")

        # 3. Get rooms
        rooms = client.get_rooms(hotel_id, "2024-12-7", "2024-12-9")
        print(f"Available rooms: {rooms}")

        # 4. Create a booking
        booking_id = client.create_booking(
            customer_name="John Doe",
            customer_email="john@example.com",
            room_id=rooms[0].room_id,
            check_in_date="2024-12-01",
            check_out_date="2024-12-05",
            num_guests=2,
            transaction_id = 425
        )
        print(f"Created booking with ID: {booking_id}")

        # 5. Get booking details
        booking = client.get_booking(booking_id)
        print(f"Booking details: {booking}")

        # 6. Update booking
        updated_booking_id = client.update_booking(
            booking_id=booking_id,
            num_guests=3
        )
        print(f"Updated booking with ID: {updated_booking_id}")

        # 7. List customer bookings
        bookings = client.list_customer_bookings("john@example.com", hotel_id)
        print(f"Customer bookings: {bookings}")

        # 8. Cancel booking
        status = client.cancel_booking(booking_id)
        print("Booking cancelled")

    except grpc.RpcError as e:
        print(f"An error occurred: {e.code()}: {e.details()}")

if __name__ == "__main__":
    main()
