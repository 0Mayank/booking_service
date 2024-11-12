# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: booking.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'booking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x12\x07\x62ooking\"\x07\n\x05\x45mpty\">\n\x12\x43reateRoomsRequest\x12(\n\x05rooms\x18\x01 \x03(\x0b\x32\x19.booking.CreateRoomsInner\"e\n\x10\x43reateRoomsInner\x12\x10\n\x08hotel_id\x18\x01 \x01(\x03\x12\x13\n\x0broom_number\x18\x02 \x01(\x05\x12\x11\n\troom_type\x18\x03 \x01(\x05\x12\x17\n\x0fprice_per_night\x18\x04 \x01(\x01\"\x99\x01\n\x14\x43reateBookingRequest\x12\x15\n\rcustomer_name\x18\x01 \x01(\t\x12\x16\n\x0e\x63ustomer_email\x18\x02 \x01(\t\x12\x0f\n\x07room_id\x18\x03 \x01(\x03\x12\x15\n\rcheck_in_date\x18\x04 \x01(\t\x12\x16\n\x0e\x63heck_out_date\x18\x05 \x01(\t\x12\x12\n\nnum_guests\x18\x06 \x01(\x05\"+\n\x15\x43reateBookingResponse\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\"\'\n\x11GetBookingRequest\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\"\xbe\x01\n\x12GetBookingResponse\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\x12\x15\n\rcustomer_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63ustomer_email\x18\x03 \x01(\t\x12\x0f\n\x07room_id\x18\x04 \x01(\x03\x12\x15\n\rcheck_in_date\x18\x05 \x01(\t\x12\x16\n\x0e\x63heck_out_date\x18\x06 \x01(\t\x12\x12\n\nnum_guests\x18\x07 \x01(\x05\x12\x11\n\tcancelled\x18\x08 \x01(\x08\"#\n\x0fGetRoomsRequest\x12\x10\n\x08hotel_id\x18\x01 \x01(\x03\"4\n\x10GetRoomsResponse\x12 \n\x05rooms\x18\x01 \x03(\x0b\x32\x11.booking.RoomInfo\"\xd6\x02\n\x14UpdateBookingRequest\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\x12\x1a\n\rcustomer_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x63ustomer_email\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07room_id\x18\x04 \x01(\x03H\x02\x88\x01\x01\x12\x1a\n\rcheck_in_date\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0e\x63heck_out_date\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x17\n\nnum_guests\x18\x07 \x01(\x05H\x05\x88\x01\x01\x12\x16\n\tcancelled\x18\x08 \x01(\x08H\x06\x88\x01\x01\x42\x10\n\x0e_customer_nameB\x11\n\x0f_customer_emailB\n\n\x08_room_idB\x10\n\x0e_check_in_dateB\x11\n\x0f_check_out_dateB\r\n\x0b_num_guestsB\x0c\n\n_cancelled\"+\n\x15UpdateBookingResponse\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\"*\n\x14\x43\x61ncelBookingRequest\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\"G\n\x1bListCustomerBookingsRequest\x12\x16\n\x0e\x63ustomer_email\x18\x01 \x01(\t\x12\x10\n\x08hotel_id\x18\x02 \x01(\x03\"T\n\x1cListCustomerBookingsResponse\x12\x34\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\".booking.ListCustomerBookingsInner\"B\n\x19ListCustomerBookingsInner\x12\x12\n\nbooking_id\x18\x01 \x01(\x03\x12\x11\n\tcancelled\x18\x02 \x01(\x08\"\x81\x01\n\x08RoomInfo\x12\x0f\n\x07room_id\x18\x01 \x01(\x03\x12\x13\n\x0broom_number\x18\x02 \x01(\x05\x12\x10\n\x08hotel_id\x18\x03 \x01(\x03\x12\x11\n\troom_type\x18\x04 \x01(\t\x12\x17\n\x0fprice_per_night\x18\x05 \x01(\x01\x12\x11\n\tavailable\x18\x06 \x01(\x08\"\x87\x01\n\x17\x43reateHotelEntryRequest\x12\x12\n\nhotel_name\x18\x01 \x01(\t\x12\x13\n\x0btotal_rooms\x18\x02 \x01(\x05\x12\x12\n\nroom_types\x18\x03 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\r\n\x05phone\x18\x05 \x01(\t\x12\x0f\n\x07website\x18\x06 \x01(\t\",\n\x18\x43reateHotelEntryResponse\x12\x10\n\x08hotel_id\x18\x01 \x01(\x03\"\xdf\x01\n\x17UpdateHotelEntryRequest\x12\x10\n\x08hotel_id\x18\x01 \x01(\x03\x12\x18\n\x0btotal_rooms\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x17\n\nroom_types\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07\x61\x64\x64ress\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05phone\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07website\x18\x06 \x01(\tH\x04\x88\x01\x01\x42\x0e\n\x0c_total_roomsB\r\n\x0b_room_typesB\n\n\x08_addressB\x08\n\x06_phoneB\n\n\x08_website\",\n\x18UpdateHotelEntryResponse\x12\x10\n\x08hotel_id\x18\x01 \x01(\x03\x32\xcb\x05\n\x0e\x42ookingService\x12N\n\rCreateBooking\x12\x1d.booking.CreateBookingRequest\x1a\x1e.booking.CreateBookingResponse\x12\x45\n\nGetBooking\x12\x1a.booking.GetBookingRequest\x1a\x1b.booking.GetBookingResponse\x12N\n\rUpdateBooking\x12\x1d.booking.UpdateBookingRequest\x1a\x1e.booking.UpdateBookingResponse\x12>\n\rCancelBooking\x12\x1d.booking.CancelBookingRequest\x1a\x0e.booking.Empty\x12\x63\n\x14ListCustomerBookings\x12$.booking.ListCustomerBookingsRequest\x1a%.booking.ListCustomerBookingsResponse\x12:\n\x0b\x43reateRooms\x12\x1b.booking.CreateRoomsRequest\x1a\x0e.booking.Empty\x12?\n\x08GetRooms\x12\x18.booking.GetRoomsRequest\x1a\x19.booking.GetRoomsResponse\x12W\n\x10\x43reateHotelEntry\x12 .booking.CreateHotelEntryRequest\x1a!.booking.CreateHotelEntryResponse\x12W\n\x10UpdateHotelEntry\x12 .booking.UpdateHotelEntryRequest\x1a!.booking.UpdateHotelEntryResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=26
  _globals['_EMPTY']._serialized_end=33
  _globals['_CREATEROOMSREQUEST']._serialized_start=35
  _globals['_CREATEROOMSREQUEST']._serialized_end=97
  _globals['_CREATEROOMSINNER']._serialized_start=99
  _globals['_CREATEROOMSINNER']._serialized_end=200
  _globals['_CREATEBOOKINGREQUEST']._serialized_start=203
  _globals['_CREATEBOOKINGREQUEST']._serialized_end=356
  _globals['_CREATEBOOKINGRESPONSE']._serialized_start=358
  _globals['_CREATEBOOKINGRESPONSE']._serialized_end=401
  _globals['_GETBOOKINGREQUEST']._serialized_start=403
  _globals['_GETBOOKINGREQUEST']._serialized_end=442
  _globals['_GETBOOKINGRESPONSE']._serialized_start=445
  _globals['_GETBOOKINGRESPONSE']._serialized_end=635
  _globals['_GETROOMSREQUEST']._serialized_start=637
  _globals['_GETROOMSREQUEST']._serialized_end=672
  _globals['_GETROOMSRESPONSE']._serialized_start=674
  _globals['_GETROOMSRESPONSE']._serialized_end=726
  _globals['_UPDATEBOOKINGREQUEST']._serialized_start=729
  _globals['_UPDATEBOOKINGREQUEST']._serialized_end=1071
  _globals['_UPDATEBOOKINGRESPONSE']._serialized_start=1073
  _globals['_UPDATEBOOKINGRESPONSE']._serialized_end=1116
  _globals['_CANCELBOOKINGREQUEST']._serialized_start=1118
  _globals['_CANCELBOOKINGREQUEST']._serialized_end=1160
  _globals['_LISTCUSTOMERBOOKINGSREQUEST']._serialized_start=1162
  _globals['_LISTCUSTOMERBOOKINGSREQUEST']._serialized_end=1233
  _globals['_LISTCUSTOMERBOOKINGSRESPONSE']._serialized_start=1235
  _globals['_LISTCUSTOMERBOOKINGSRESPONSE']._serialized_end=1319
  _globals['_LISTCUSTOMERBOOKINGSINNER']._serialized_start=1321
  _globals['_LISTCUSTOMERBOOKINGSINNER']._serialized_end=1387
  _globals['_ROOMINFO']._serialized_start=1390
  _globals['_ROOMINFO']._serialized_end=1519
  _globals['_CREATEHOTELENTRYREQUEST']._serialized_start=1522
  _globals['_CREATEHOTELENTRYREQUEST']._serialized_end=1657
  _globals['_CREATEHOTELENTRYRESPONSE']._serialized_start=1659
  _globals['_CREATEHOTELENTRYRESPONSE']._serialized_end=1703
  _globals['_UPDATEHOTELENTRYREQUEST']._serialized_start=1706
  _globals['_UPDATEHOTELENTRYREQUEST']._serialized_end=1929
  _globals['_UPDATEHOTELENTRYRESPONSE']._serialized_start=1931
  _globals['_UPDATEHOTELENTRYRESPONSE']._serialized_end=1975
  _globals['_BOOKINGSERVICE']._serialized_start=1978
  _globals['_BOOKINGSERVICE']._serialized_end=2693
# @@protoc_insertion_point(module_scope)