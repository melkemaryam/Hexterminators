''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: LateCharge.py

Created: 13th January 2020

-------------------------------------------------
'''

import datetime
import sqlite3
from DatabaseConnection import DatabaseConnection

class LateCharge:

    def __init__(self, return_date, charge_ratio,):
        self.return_date = return_date
        self.charge_ratio = charge_ratio

    def checkIfLate(self, return_date, bookingIdReturnInput):
        return_date = date.today()
        actual_booking = []
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('SELECT date FROM bookings WHERE booking_id = ?', bookingIdReturnInput)
        booking_dates = cursor.fetchall()
            for date in booking_dates:
                actual_booking.append(booking_dates)

        late_days = (return_date - max(actual_booking)).days
        late_charge = charge_ratio * late_days

        cursor.execute('UPDATE bookings SET late = ? WHERE booking_id = ?', late_charge, bookingIdReturnInput)

        DatabaseConnection.CloseDBConnection()