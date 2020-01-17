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

class AvailabilityChecker:

    def __init__(self, databaseFilename):
            self.databasefilename = databaseFilename

    '''
    Function name: date_generator()
    Task: generate list of dates for the required 6 weeks bookings
    '''

    def date_generator(self):

        dates = []
        from_date = datetime.date.today()

        i=1
        while i<43:
            dates.append(from_date + datetime.timedelta(days = i))
            i+=1

        #generates a list of dates up to 6 weeks ahead

        return dates    

    '''
    Function name: get_availability()
    Task: returns a list of possible dates of renting for a tool including the required length of booking
    '''

    def get_availability(self, tool_id, lengthOfBookingInput):

        #checks what date it is today  
        today = datetime.date.today() 

        #checks how many days out of 6 weeks have availability set up for specific tool            
        databaseConnection = DatabaseConnection.CreateDBConnection('SharedPower.db')

        cursor = databaseConnection.cursor()

        cursor.execute('SELECT count(*) FROM bookings WHERE tool_id = ? AND start_date > ?', (tool_id, today,))

        missing_days = cursor.fetchone()

        #counting from which date forward availability must be set
        missing_availability = today + datetime.timedelta(days = missing_days)
        
        #brings back all arguments for a tool from a day when it is not rented - cust_id is empty
        cursor.execute('SELECT tool_id, price, date FROM bookings WHERE tool_id = ? AND available = 1', tool_id,)

        availability_row=cursor.fetchone()

        if (availability_row != None):
            tool_id = availability_row[0]
            price = availability_row[1]
            date = availability_row[2]

        #generates a list of dates that do not have availability set
        new_dates = []
        i=1
        while i<(43-missing_days):
            new_dates.append(missing_availability + datetime.timedelta(days = i))
            i+=1

        #sets up availability for up to 6 weeks ahead for days that weren't set
        for missing_availability in new_dates:
            cursor.execute('INSERT INTO Bookings (tool_id, price, start_date, cust_id, delivery, available) VALUES(?, ?, ?, ?, ?, ?)', (tool_id, price, missing_availability, 0, 0, 1,))

        databaseConnection.commit()

        #fetches days the tool is actually available for the upcoming 6 weeks   
        self.date_generator()
        for from_date in new_dates:
            end_date = from_date + datetime.timedelta(days = lengthOfBookingInput)
            cursor.execute('SELECT date FROM bookings WHERE tool_id = ? AND (date BETWEEN ? AND ?) AND available = 1', (tool_id, from_date, end_date,))
            
        days_available = cursor.fetchall()
        
        DatabaseConnection.CloseDBConnection(self.databasefilename)

        days_available = []
        for date in quick_dates:
            quick_dates = date[0]
            days_available.append(quick_dates)
            #reforges the list into list
        
        return days_available
    
    '''
    Function name: book_out()
    Task: sets tool as unavailable for booking dates and stores value for delivery charge
    '''

    def book_out(self, tool_id, dateOfBooking, lengthOfBookingInput, Delivery):
        
        databaseConnection = DatabaseConnection.CreateDBConnection(self.databasefilename)

        cursor = databaseConnection.cursor()

        #creates list of dates to take the availability out for
        booking_dates = [dateOfBooking]
        i = 1
        while i>= lengthOfBookingInput:
            booking_dates.append(dateOfBooking + datetime.timedelta(days = 1))
            i+=1
     
        #sets availability to 0 (rented) for the number of days
        for dateOfBooking in booking_dates:
            cursor.execute('UPDATE Bookings SET available = 0 WHERE tool_id = ? AND date = ?', tool_id, dateOfBooking,)

        #sets delivery status
        if Delivery == 1:
            for dateOfBooking in booking_dates:
                cursor.execute('UPDATE Bookings SET Delivery = 1 WHERE tool_id = ? AND date = ?', tool_id, dateOfBooking,)
                
        databaseConnection.commit()

        DatabaseConnection.CloseDBConnection(self.databasefilename)

    
