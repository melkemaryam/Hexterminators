''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: ToolManagerTests.py

Created: 16th January 2020
-------------------------------------------------
'''

from sqlite3 import Error

from Managers.ToolManager import ToolManager
from Managers.BookingManager import BookingManager
from GetterSetter.Tools import Tools

class ToolManagerTests:


    # Test the Search Future Bookings 
    def TestSearchFutureBookings(self, database_path):

        function_name   = 'TestSearchFutureBookings'

        try:

            # Get a tool from the tool manager
            toolManager = ToolManager(database_path)
            test_tool = toolManager.loadToolId(1)

            bookingManager = BookingManager(database_path)

            future_bookings = toolManager.loadFutureTool(range_start, range_end_days = 42)

            for booking in future_bookings:
                print(booking)

        except Error as e:

            # Catch and display any errors that occur
            print(__name__, ':', function_name, " - ", e)