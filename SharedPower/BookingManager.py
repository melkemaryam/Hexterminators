''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: BookingManager.py

Created: 10th January 2020

-------------------------------------------------
'''

from datetime import datetime
from sqlite3 import Error

from Bookings import Bookings
from Tools import Tools       

from ToolManager import ToolManager

from DatabaseConnection import DatabaseConnection

class BookingManager:

    #Constructor

    def __init__(self, database_filename):

        
        self.__database_filename = database_filename

    '''
    Function name: createBooking
    Task: create a booking for a tool in the DB
    '''

    def createBooking(self, tool, user):

        function_name = 'createBooking'

        try:
            
            # Connecting to the DB
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)
            cursor = database_connection.cursor()

            # get IDs
            tool_id = tool.getId()
            cust_id = user.getId()

            cursor.execute('INSERT INTO Bookings (tool_id, cust_id) VALUES (?, ?)', (tool_id, cust_id)) 

            database_connection.commit()

            book_id = cursor.lastrowid

            returnedBooking = Booking(book_id, tool, user)
            
            # Diconnecting from the DB
            DatabaseConnection.CloseConnection(database_connection)

            return returnedBooking

        except Error as e:

            print(__name__, ':', function_name, ':', e)
            raise

    '''
    Function name: SearchFutureBookings
    Task: search for future bookings for the user
    '''

    def searchFutureBookings(self, user):

        function_name = 'SearchFutureBookings'

        # empty list
        RetBookingList = []
        
        try:

            tool_manager = ToolManager(self.__database_filename)
            start_date = datetime.now()

            # get ID
            cust_id = user.getId()

            # Connecting to the DB
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)
            cursor = database_connection.cursor()

            cursor.execute("SELECT Bookings.book_id, Bookings.tool_id FROM Bookings INNER JOIN Tools ON Bookings.tool_id = Tools.tool_id WHERE Tools.tool_start > ? AND Bookings.cust_id = ?", (start_date, cust_id))

            booking_rows = cursor.fetchall()

            # creating tool objects in the DB and adding it to RetBookingList[]
            for Booking in booking_rows:
                
                book_id = booking_rows[0]
                tool_id = booking_rows[1]

                # load the correct tool
                tool = tool_manager.load_tool_from_id(tool_id)

                # create booking
                single_booking = Booking(book_id, tool, user)

                RetBookingList.append(single_booking)
            
            # Disconnect from the DB
            DatabaseConnection.CloseConnection(database_connection)

            return RetBookingList

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise