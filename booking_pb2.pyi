from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateRoomsRequest(_message.Message):
    __slots__ = ("rooms",)
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[CreateRoomsInner]
    def __init__(self, rooms: _Optional[_Iterable[_Union[CreateRoomsInner, _Mapping]]] = ...) -> None: ...

class CreateRoomsInner(_message.Message):
    __slots__ = ("hotel_id", "room_number", "room_type", "price_per_night")
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ROOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_NIGHT_FIELD_NUMBER: _ClassVar[int]
    hotel_id: int
    room_number: int
    room_type: int
    price_per_night: float
    def __init__(self, hotel_id: _Optional[int] = ..., room_number: _Optional[int] = ..., room_type: _Optional[int] = ..., price_per_night: _Optional[float] = ...) -> None: ...

class CreateBookingRequest(_message.Message):
    __slots__ = ("customer_name", "customer_email", "room_id", "check_in_date", "check_out_date", "num_guests", "transaction_id")
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    NUM_GUESTS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    customer_name: str
    customer_email: str
    room_id: int
    check_in_date: str
    check_out_date: str
    num_guests: int
    transaction_id: int
    def __init__(self, customer_name: _Optional[str] = ..., customer_email: _Optional[str] = ..., room_id: _Optional[int] = ..., check_in_date: _Optional[str] = ..., check_out_date: _Optional[str] = ..., num_guests: _Optional[int] = ..., transaction_id: _Optional[int] = ...) -> None: ...

class CreateBookingResponse(_message.Message):
    __slots__ = ("booking_id",)
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    def __init__(self, booking_id: _Optional[int] = ...) -> None: ...

class GetBookingRequest(_message.Message):
    __slots__ = ("booking_id",)
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    def __init__(self, booking_id: _Optional[int] = ...) -> None: ...

class GetBookingResponse(_message.Message):
    __slots__ = ("booking_id", "customer_name", "customer_email", "room_id", "check_in_date", "check_out_date", "num_guests", "cancelled", "transaction_id", "room_number")
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    NUM_GUESTS_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    customer_name: str
    customer_email: str
    room_id: int
    check_in_date: str
    check_out_date: str
    num_guests: int
    cancelled: bool
    transaction_id: int
    room_number: int
    def __init__(self, booking_id: _Optional[int] = ..., customer_name: _Optional[str] = ..., customer_email: _Optional[str] = ..., room_id: _Optional[int] = ..., check_in_date: _Optional[str] = ..., check_out_date: _Optional[str] = ..., num_guests: _Optional[int] = ..., cancelled: bool = ..., transaction_id: _Optional[int] = ..., room_number: _Optional[int] = ...) -> None: ...

class GetRoomsRequest(_message.Message):
    __slots__ = ("hotel_id", "check_in_date", "check_out_date")
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    hotel_id: int
    check_in_date: str
    check_out_date: str
    def __init__(self, hotel_id: _Optional[int] = ..., check_in_date: _Optional[str] = ..., check_out_date: _Optional[str] = ...) -> None: ...

class GetRoomsResponse(_message.Message):
    __slots__ = ("rooms",)
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[RoomInfo]
    def __init__(self, rooms: _Optional[_Iterable[_Union[RoomInfo, _Mapping]]] = ...) -> None: ...

class UpdateBookingRequest(_message.Message):
    __slots__ = ("booking_id", "customer_name", "customer_email", "room_id", "check_in_date", "check_out_date", "num_guests", "cancelled")
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    NUM_GUESTS_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    customer_name: str
    customer_email: str
    room_id: int
    check_in_date: str
    check_out_date: str
    num_guests: int
    cancelled: bool
    def __init__(self, booking_id: _Optional[int] = ..., customer_name: _Optional[str] = ..., customer_email: _Optional[str] = ..., room_id: _Optional[int] = ..., check_in_date: _Optional[str] = ..., check_out_date: _Optional[str] = ..., num_guests: _Optional[int] = ..., cancelled: bool = ...) -> None: ...

class UpdateBookingResponse(_message.Message):
    __slots__ = ("booking_id",)
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    def __init__(self, booking_id: _Optional[int] = ...) -> None: ...

class CancelBookingRequest(_message.Message):
    __slots__ = ("booking_id",)
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    def __init__(self, booking_id: _Optional[int] = ...) -> None: ...

class ListCustomerBookingsRequest(_message.Message):
    __slots__ = ("customer_email", "hotel_id")
    CUSTOMER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    customer_email: str
    hotel_id: int
    def __init__(self, customer_email: _Optional[str] = ..., hotel_id: _Optional[int] = ...) -> None: ...

class ListCustomerBookingsResponse(_message.Message):
    __slots__ = ("bookings",)
    BOOKINGS_FIELD_NUMBER: _ClassVar[int]
    bookings: _containers.RepeatedCompositeFieldContainer[GetBookingResponse]
    def __init__(self, bookings: _Optional[_Iterable[_Union[GetBookingResponse, _Mapping]]] = ...) -> None: ...

class RoomInfo(_message.Message):
    __slots__ = ("room_id", "room_number", "hotel_id", "room_type", "price_per_night", "available")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_NIGHT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    room_number: int
    hotel_id: int
    room_type: str
    price_per_night: float
    available: bool
    def __init__(self, room_id: _Optional[int] = ..., room_number: _Optional[int] = ..., hotel_id: _Optional[int] = ..., room_type: _Optional[str] = ..., price_per_night: _Optional[float] = ..., available: bool = ...) -> None: ...

class CreateHotelEntryRequest(_message.Message):
    __slots__ = ("hotel_name", "total_rooms", "room_types", "address", "phone", "website")
    HOTEL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROOMS_FIELD_NUMBER: _ClassVar[int]
    ROOM_TYPES_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    hotel_name: str
    total_rooms: int
    room_types: int
    address: str
    phone: str
    website: str
    def __init__(self, hotel_name: _Optional[str] = ..., total_rooms: _Optional[int] = ..., room_types: _Optional[int] = ..., address: _Optional[str] = ..., phone: _Optional[str] = ..., website: _Optional[str] = ...) -> None: ...

class CreateHotelEntryResponse(_message.Message):
    __slots__ = ("hotel_id",)
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    hotel_id: int
    def __init__(self, hotel_id: _Optional[int] = ...) -> None: ...

class UpdateHotelEntryRequest(_message.Message):
    __slots__ = ("hotel_id", "total_rooms", "room_types", "address", "phone", "website")
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROOMS_FIELD_NUMBER: _ClassVar[int]
    ROOM_TYPES_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    hotel_id: int
    total_rooms: int
    room_types: int
    address: str
    phone: str
    website: str
    def __init__(self, hotel_id: _Optional[int] = ..., total_rooms: _Optional[int] = ..., room_types: _Optional[int] = ..., address: _Optional[str] = ..., phone: _Optional[str] = ..., website: _Optional[str] = ...) -> None: ...

class UpdateHotelEntryResponse(_message.Message):
    __slots__ = ("hotel_id",)
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    hotel_id: int
    def __init__(self, hotel_id: _Optional[int] = ...) -> None: ...
