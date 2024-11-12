CREATE TABLE IF NOT EXISTS HOTELS (
    hotel_id SERIAL PRIMARY KEY,
    total_rooms INTEGER,
    room_types INTEGER,
    address VARCHAR(255),
    phone VARCHAR(20),
    website VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ROOMS (
    room_id SERIAL PRIMARY KEY,
    hotel_id BIGINT,
    room_number INTEGER,
    room_type INTEGER,
    available BOOLEAN NOT NULL DEFAULT False,
    price_per_night REAL DEFAULT 0,
    FOREIGN KEY (hotel_id) REFERENCES HOTELS(hotel_id)
);

CREATE TABLE IF NOT EXISTS BOOKINGS (
    booking_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_email VARCHAR(255),
    room_id BIGINT,
    check_in_date DATE,
    check_out_date DATE,
    num_guests INTEGER,
    cancelled BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (room_id) REFERENCES ROOMS(room_id)
);

-- v1
ALTER TABLE BOOKINGS
ADD COLUMN IF NOT EXISTS cancelled BOOLEAN DEFAULT FALSE;

ALTER TABLE ROOMS
ADD COLUMN IF NOT EXISTS price_per_night REAL DEFAULT 0;
