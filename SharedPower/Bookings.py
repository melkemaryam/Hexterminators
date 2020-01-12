''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Bookings.py

Created: 10th January 2020

-------------------------------------------------
'''

class Bookings:

    #Constructor
    def __init__(self, book_id, tool, user):

        self.book_id = book_id
        self.tool = tool
        self.user = user
        
    # --------------------------------------------------------------------
    # Returns the booking id
    # --------------------------------------------------------------------
    def getBookingId(self):
        return self.book_id

    # --------------------------------------------------------------------
    # Returns the tool
    # --------------------------------------------------------------------
    def getTool(self):
        return self.tool

    # --------------------------------------------------------------------
    # Returns the user
    # --------------------------------------------------------------------
    def getUser(self):
        return self.user

    # --------------------------------------------------------------------
    # __str__ function
    # --------------------------------------------------------------------
    def __str__(self):

        return_value = '{id} \t {tool} \t {user}'.format(id = self.book_id, tool = self.tool.getName(), user = self.user.getLastName())

        return return_value

    # --------------------------------------------------------------------
    # __repr__ function
    # --------------------------------------------------------------------
    def __repr__(self):

        return_value = '{id} \t {tool} \t {user}'.format(id = self.book_id, tool = self.tool.getName(), user = self.user.getLastName())

        return return_value
