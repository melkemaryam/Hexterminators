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

    def __init__(self, databaseFilename):
        self.databaseFilename = 'SharedPower.db'
        #basic late charge is double the rate

    def checkIfLate(self, book_id):
        return_date = datetime.datetime.today()
        actual_booking = []
        charge_ratio = 2
        databaseConnection = DatabaseConnection.CreateDBConnection(self.databaseFilename)
        cursor = databaseConnection.cursor()
        cursor.execute('SELECT date FROM booking WHERE book_id = ?', book_id)
        booking_dates = cursor.fetchall()
        for i in booking_dates:
            actual_booking.append(booking_dates)
        #checks which dates belong to the booking

        late_days = (return_date - max(actual_booking)).days
        #counts how many days overdue
        late_charge = charge_ratio * late_days
        #adds the ratio for later calculation

        DatabaseConnection.CloseDBConnection(self.databaseFilename)
        
        return late_charge