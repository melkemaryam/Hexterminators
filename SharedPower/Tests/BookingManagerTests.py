''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: BookingManagerTests.py

Created: 16th January 2020
-------------------------------------------------
'''

from sqlite3 import Error

from Managers.ToolManager import ToolManager
from Managers.BookingManager import BookingManager

from GetterSetter.Tools import Tools
from GetterSetter.Bookings import Bookings

class BookingManagerTests:

    # Test the Search Future Bookings 
    def TestSearchFutureBookings(self, database_path):

        function_name   = 'TestSearchFutureBookings'

        try:

            # Get a tool from the tool manager
            toolManager = ToolManager(database_path)
            test_tool = toolManager.loadToolId(1)

            bookingManager = BookingManager(database_path)

            futureBookings = bookingManager.searchFutureBookings(test_tool)

            for booking in futureBookings:
                print(booking)

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, " - ", e)