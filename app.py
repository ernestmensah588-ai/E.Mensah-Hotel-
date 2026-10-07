<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>E.Mensah Hostel - Booking & Management</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f4f6f9; }
        header { background-color: #0d3b66; color: white; padding: 25px 40px; text-align: center; }
        header h1 { margin: 0; font-size: 2.2em; letter-spacing: 1px; }
        header p { margin-top: 5px; color: #f4d35e; font-weight: bold; }
        
        .main-container { padding: 30px; max-width: 1200px; margin: 0 auto; }
        .grid-layout { display: flex; gap: 30px; margin-bottom: 30px; }
        .card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); flex: 1; }
        
        /* Flyer Styling */
        .flyer-banner { text-align: center; background: #fafafa; border: 2px dashed #0d3b66; padding: 15px; border-radius: 10px; margin-bottom: 30px; }
        .flyer-banner img { max-width: 100%; height: auto; max-height: 400px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.15); }
        
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #e0e0e0; padding: 12px; text-align: left; }
        th { background-color: #0d3b66; color: white; }
        input, select, textarea { width: 100%; padding: 10px; margin: 8px 0 16px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 5px; }
        button { background-color: #f4d35e; color: #0d3b66; font-weight: bold; border: none; padding: 12px 20px; cursor: pointer; border-radius: 5px; width: 100%; font-size: 16px; }
        button:hover { background-color: #ee9b00; color: white; }
        .status-Available { color: #2a9d8f; font-weight: bold; }
        .status-Booked { color: #e76f51; font-weight: bold; }
    </style>
</head>
<body>

    <header>
        <h1>🏨 E.Mensah Hostel</h1>
        <p>A Warm Home Away From Home — Comfortable & Affordable Accommodation</p>
    </header>

    <div class="main-container">

        <!-- Flyer Display Section -->
        <div class="flyer-banner">
            <h2 style="color: #0d3b66; margin-top: 0;">Special Promotion</h2>
            <!-- Displays the flyer from static/flyer.jpg -->
            <img src="{{ url_for('static', filename='flyer.jpg') }}" alt="E.Mensah Hostel Flyer">
            <p style="margin-bottom: 0; color: #555;"><strong>Book Online Today and Get 15% Off Your Stay!</strong></p>
        </div>

        <div class="grid-layout">
            <!-- Reservation Form -->
            <div class="card">
                <h2>Guest Reservation Form</h2>
                <form action="/book" method="POST">
                    <label>Guest Full Name:</label>
                    <input type="text" name="guest_name" required placeholder="e.g. John Doe">

                    <label>Phone / Contact Number:</label>
                    <input type="text" name="guest_phone" required placeholder="e.g. +233 24 123 4567">

                    <label>Select Room:</label>
                    <select name="room_number" required>
                        {% for room in rooms %}
                            {% if room[3] == 'Available' %}
                                <option value="{{ room[0] }}">Room {{ room[0] }} ({{ room[1] }} - ${{ room[2] }}/night)</option>
                            {% endif %}
                        {% endfor %}
                    </select>

                    <label>Check-in Date:</label>
                    <input type="date" name="check_in_date" required>

                    <label>Special Requests / Preferences:</label>
                    <textarea name="special_requests" rows="3" placeholder="e.g. Lower bunk bed, late night check-in..."></textarea>

                    <button type="submit">Confirm Reservation</button>
                </form>
            </div>

            <!-- Room Directory -->
            <div class="card">
                <h2>Room Directory & Status</h2>
                <table>
                    <tr>
                        <th>Room #</th>
                        <th>Category</th>
                        <th>Rate/Night</th>
                        <th>Status</th>
                    </tr>
                    {% for room in rooms %}
                    <tr>
                        <td>{{ room[0] }}</td>
                        <td>{{ room[1] }}</td>
                        <td>${{ room[2] }}</td>
                        <td class="status-{{ room[3] }}">{{ room[3] }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>
        </div>

        <!-- Booking Log -->
        <div class="card">
            <h2>Recent Booking Logs & Guest Information</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Guest Name</th>
                    <th>Contact</th>
                    <th>Room #</th>
                    <th>Check-in Date</th>
                    <th>Booking Timestamp</th>
                    <th>Special Requests</th>
                </tr>
                {% for booking in bookings %}
                <tr>
                    <td>#{{ booking[0] }}</td>
                    <td>{{ booking[1] }}</td>
                    <td>{{ booking[2] }}</td>
                    <td>{{ booking[3] }}</td>
                    <td>{{ booking[4] }}</td>
                    <td>{{ booking[5] }}</td>
                    <td>{{ booking[6] }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>

    </div>

</body>
</html>
