''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: __test__.py

Created: 17th January 2020
-------------------------------------------------
'''

from sqlite3 import Error
from Tests.BookingManagerTests import BookingManagerTests

databasefilename = 'SharedPower.db'
function_name = "test"
test_user = ('test', 'cust_id', 'F_name', 'L_name', 'email', 'username')

try:

    BookingManagerTests.TestSearchFutureBookings(test_user, databasefilename)

except Error as e:

    # Catch and display any errors that occur
    print(__name__, ':', function_name, " - ", e)
