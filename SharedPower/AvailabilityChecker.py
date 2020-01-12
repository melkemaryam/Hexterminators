''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: AvailabilityChecker.py

Created: 6th January 2020

-------------------------------------------------
'''

import datetime
import sqlite3
import pandas
from DatabaseConnection import DatabaseConnection

class Availability:

    def __init__(self, date, end_date, available, duration):
        self.date = date
        self.end_date = end_date
        self.available = available
        self.duration = duration

    def date_generator(self):
        dates = []
        from_date = date.today()
        i=1
        while i<43:
            dates.append(from_date + timedelta(days = i))
            i+=1
        return dates
        #generates a list of days equal to 6 weeks from today

    def get_availability(self, tool_id):
        today = date.today()     
        #checks what date it is today       
        DatabaseConnection.CreateDBConnection()
        
        cursor.execute('SELECT count(*) FROM bookings WHERE tool_id = ? AND date > ?', tool_id, today)
        missing_days = cursor.fetchone()
        #checks how many days out of 6 weeks have availability set up for specific tool
        missing_availability = today + timedelta(days = missing_days)
        #counting from which date forward availability must be set
        
        cursor.execute('SELECT tool_id, price, date, cust_id, delivery, available FROM booking WHERE tool_id = ? AND available = 1', tool_id)
        availability_row=cursor.fetchone()
        if (availability_row != None):
            cust_id = availability_row[3]
            tool_id = availability_row[0]
            price = availability_row[1]
            available = availability_row[5]
            date = availability_row[2]
            delivery = availability_row[4]
            #brings back all arguments for a tool from a day when it is not rented - cust_id is empty

        new_dates = []
        i=1
        while i<(43-missing_days):
            new_dates.append(missing_availability + timedelta(days = i))
            i+=1

        for missing_availability in new_dates:
            cursor.execute('INSERT INTO Booking (tool_id, price, date, cust_id, delivery, available) VALUES(?, ?, ?, ?, ?, ?)', newToolID, dayPriceToolInput, missing_availability, 0, 0, 1)
            #sets up availability for up to 6 weeks ahead for days that weren't set
        
        self.date_generator()
        for from_date in dates:
		    cursor.execute('SELECT date FROM bookings WHERE tool_id = ? AND date = ? AND available = 1', tool_id, from_date)
            #fetches days the tool is actually available
        
        quick_dates = cursor.fetchall()

        dates_available = []
        for date in days_available:
            quick_dates = date[0]
            dates_available.append(quick_dates)
            #reforges the list into list - is it reaslly needed?
        
        return days_available
        DatabaseConnection.CloseDBConnection()

    def book_out(self, tool_id, dateOfBooking, lengthOfBookingInput, Delivery):
        
        DatabaseConnection.CreateDBConnection()
        booking_dates = [dateOfBooking]
        i = 1
        while i>= lengthOfBookingInput:
            booking_dates.append(dateOfBooking + timedelta(days = 1))
            i+=1
            #creates list of dates to take the availability out for
        
        for dateOfBooking in booking_dates:
            cursor.execute('UPDATE Booking SET available = 0 WHERE tool_id = ? AND date = ?', tool_id, dateOfBooking)
            #sets availability to 0 (rented) for the number of days

        if Delivery = 1:
            for dateOfBooking in booking_dates:
                cursor.execute('UPDATE Booking SET Delivery = 1 WHERE tool_id = ? AND date = ?', tool_id, dateOfBooking)
                #sets delivery status

        
        DatabaseConnection.CloseDBConnection()

    

    
