''' 
-------------------------------------------------
Project: SharedPower
Group: Hexterminators

File name: AvailabilityCheckerTest.py

Created: 16th January 2020
-------------------------------------------------
'''

from datetime import datetime
import sqlite3
from sqlite3 import Error
import pandas

from Helpers.DatabaseConnection import DatabaseConnection

class AvailabilityCheckerTest:

    def TestSearchFutureBookings(self, database_path):
        
        function_name = 'TestSearchFutureBookings'

        try:
            #Get a user from the database
            availabilityManager = data_user(database_path)
            test_availability = availabilityManager.loadAvailibiltyID(1)

            availability_checker = availability_checker(database_path)

            future_availability = availabilityManager.loadFutureAvailability(range_start, range_end_days = 31)

            for availability in future_availability:
                print (available)

        except Error as e:
            print (__name__, ':', function_name, "-", e)