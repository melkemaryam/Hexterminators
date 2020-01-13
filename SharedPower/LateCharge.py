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
        self.charge_ratio = 2
        #basic late charge is double the rate

    def checkIfLate(self, return_date, bookingIdReturnInput):
        return_date = datetime.datetime.today()
        actual_booking = []
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('SELECT date FROM booking WHERE book_id = ?', bookingIdReturnInput)
        booking_dates = cursor.fetchall()
        for date in booking_dates:
            actual_booking.append(booking_dates)
        #checks which dates belong to the booking

        late_days = (return_date - max(actual_booking)).days
        #counts how many days overdue
        late_charge = charge_ratio * late_days
        #adds the ratio for later calculation

        cursor.execute('UPDATE booking SET late_return = ? WHERE book_id = ?', late_charge, bookingIdReturnInput)

        DatabaseConnection.CloseDBConnection()