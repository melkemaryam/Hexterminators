# --------------------------------------------------------------------
# Filename:     BookingManager.py
#
# Date Created: 29th November 2019
# --------------------------------------------------------------------

from datetime import datetime
from sqlite3 import Error

from Booking import Booking
from tool import tool       #here

from ToolManager import ToolManager        #here

from DatabaseConnection import DatabaseConnection

class BookingManager:

    # -----------------------------------------------------------
    # Constructor
    # -----------------------------------------------------------
    def __init__(self, database_filename):

        # Store the filename of the database so that we can use it when we are connecting.
        self.__database_filename = database_filename

    # -----------------------------------------------------------
    # create_booking
    # Create a new booking in the database
    # -----------------------------------------------------------
    def create_booking(self, tool, user):

        function_name = 'create_booking'

        try:
            
            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            # Extract the id's from our objects so that we can insert them into the database table
            tool_id  = tool.getId()
            cust_id     = user.getId()

            # Execute our INSERT query against the database
            cursor.execute('INSERT INTO Bookings (tool_id, cust_id) VALUES (?, ?)', (tool_id, cust_id)) 

            # Commit the changes
            database_connection.commit()

            # Let's get the id of the record we just created
            book_id = cursor.lastrowid

            # Create a booking object based on the information we now have
            returned_booking = Booking(book_id, tool, user)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the booking we just created
            return returned_booking

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise

    # -----------------------------------------------------------
    # search_future_bookings_for_user
    # Search for future bookings for the given user
    # -----------------------------------------------------------
    def search_future_bookings_for_user(self, user):

        function_name = 'search_future_bookings_for_user'

        # Create an empty list so that we can add bookings to it later
        returned_booking_list = []
        
        try:

            # We are going to need the tool manager in a little while so let's create it now
            tool_manager = ToolManager(self.__database_filename)

            # We only want bookings from now - so we specify the start date and include this in our SQL query
            start_date = datetime.now()

            # Grab the user id so we can use it in out database query
            cust_id = user.getId()

            # Connect to our database
            database_connection = DatabaseConnection.CreateDBConnection(self.__database_filename)

            # Create a cursor so that we can run queries
            cursor = database_connection.cursor()

            cursor.execute("SELECT Bookings.book_id, Bookings.tool_id FROM Bookings INNER JOIN Tools ON Bookings.tool_id = Tools.tool_id WHERE Tools.tool_start > ? AND Bookings.cust_id = ?", (start_date, cust_id))

            bookings_rows = cursor.fetchall()

            # Iterate through the database records, creating a tool object and adding it to our list as we go
            for Bookings in booking_rows:
                
                # Read our values from the record
                book_id          = booking_rows[0]
                tool_id          = booking_rows[1]

                # Now we can ask the tool manager to give us the tool that corresponds to the tool id we just got
                tool = tool_manager.load_tool_from_id(tool_id)

                # We should now have a record with some data in it so let's create our booking
                single_booking = Booking(book_id, tool, user)

                returned_booking_list.append(single_booking)
            
            # Close our database connection
            DatabaseConnection.CloseConnection(database_connection)

            # Return the tool list we just created
            return returned_booking_list

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, ':', e)
            raise