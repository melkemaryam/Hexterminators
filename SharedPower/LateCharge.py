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

    #Constructor
    def __init__(self, databaseFilename):
        self.databaseFilename = 'SharedPower.db'
        
    '''
    Function name: checkIfLate()
    Task: checks wether a tool is returned late and add the additional fee of a double day rate
    '''

    def checkIfLate(self, book_id):
        
        return_date = datetime.datetime.today()
        charge_ratio = 2
        
        databaseConnection = DatabaseConnection.CreateDBConnection('SharedPower.db')
        cursor = databaseConnection.cursor()
        cursor.execute('SELECT end_date FROM Bookings WHERE book_id = ?', book_id,)
        
        booking_dates = cursor.fetchone()
        #late_days = 1
        late_days = (return_date - booking_dates).days
        #counts how many days overdue
        late_charge = charge_ratio * late_days
        #adds the ratio for later calculation

        DatabaseConnection.CloseDBConnection(databaseConnection)
        
        return late_charge