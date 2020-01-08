import datetime from datetime
import sqlite3
from DatabaseConnection import DatabaseConnection

class Availability:

    def __init__(self, date, end_date, available, duration):
        self.date = date
        self.end_date = end_date
        self.available = available
        self.duration = duration
        
    def get_dates(self, date, end_date, tool_id):
        DatabaseConnection.CreateDBConnection()
		    cursor.execute('SELECT date, duration FROM bookings WHERE tool_id= ?', tool_id)
        start_dates = cursor.fetchall()
        for booking in start_dates:
            date = booking[0]
            duration = booking[1]
        DatabaseConnection.CloseConnection()
        end_date = start_date + timedelta(days=duration)
        delta = end_date - start_date
        for i in range(delta.days + 1):
           if date == delta:
              available = 0
           else:
              available = 1
    
