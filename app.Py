from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize the Database for E.Mensah Hostel
def init_db():
    conn = sqlite3.connect('emensah_hostel.db')
    cursor = conn.cursor()
    
    # Create Rooms Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            room_number INTEGER PRIMARY KEY,
            room_type TEXT NOT NULL,
            price_per_night REAL NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    ''')
    
    # Create Bookings Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT NOT NULL,
            guest_phone TEXT NOT NULL,
            room_number INTEGER NOT NULL,
            booking_time TEXT NOT NULL,
            check_in_date TEXT NOT NULL,
            special_requests TEXT,
            FOREIGN KEY (room_number) REFERENCES rooms (room_number)
        )
    ''')
    
    # Insert initial hostel rooms
    cursor.execute('SELECT COUNT(*) FROM rooms')
    if cursor.fetchone()[0] == 0:
        initial_rooms = [
            (101, '4-Bed Student Dorm (Shared)', 15.0, 'Available'),
            (102, '2-Bed Deluxe Dorm (Shared)', 25.0, 'Available'),
            (201, 'Private Single Room', 45.0, 'Available'),
            (202, 'Private Executive Suite', 70.0, 'Available')
        ]
        cursor.executemany('INSERT INTO rooms VALUES (?, ?, ?, ?)', initial_rooms)
    
    conn.commit()
    conn.close()

# Home Page: View Rooms, Flyer, and Bookings
@app.route('/')
def home():
    conn = sqlite3.connect('emensah_hostel.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM rooms')
    rooms = cursor.fetchall()
    
    cursor.execute('SELECT * FROM bookings ORDER BY id DESC')
    bookings = cursor.fetchall()
    
    conn.close()
    return render_template('index.html', rooms=rooms, bookings=bookings)

# New Booking Action
@app.route('/book', methods=['POST'])
def book_room():
    guest_name = request.form['guest_name']
    guest_phone = request.form['guest_phone']
    room_number = request.form['room_number']
    check_in_date = request.form['check_in_date']
    special_requests = request.form['special_requests']
    booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('emensah_hostel.db')
    cursor = conn.cursor()

    # Save booking record
    cursor.execute('''
        INSERT INTO bookings (guest_name, guest_phone, room_number, booking_time, check_in_date, special_requests)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (guest_name, guest_phone, room_number, booking_time, check_in_date, special_requests))

    # Update room status to Booked
    cursor.execute('UPDATE rooms SET status = "Booked" WHERE room_number = ?', (room_number,))

    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
