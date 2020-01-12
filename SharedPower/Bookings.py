''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Bookings.py

Created: 10th January 2020

-------------------------------------------------
'''

class Bookings:

    # --------------------------------------------------------------------
    # Constructor
    # --------------------------------------------------------------------
    def __init__(self, book_id, tool, user):

        # Transfer our incoming parameters to the member variables for this class
        self.__book_id   = book_id
        self.__tool      = tool
        self.__user      = user
        
    # --------------------------------------------------------------------
    # Returns the booking id
    # --------------------------------------------------------------------
    def getBookingId(self):
        return self.__book_id

    # --------------------------------------------------------------------
    # Returns the tool
    # --------------------------------------------------------------------
    def getTool(self):
        return self.__tool

    # --------------------------------------------------------------------
    # Returns the user
    # --------------------------------------------------------------------
    def getUser(self):
        return self.__user

    # --------------------------------------------------------------------
    # __str__ function
    # --------------------------------------------------------------------
    def __str__(self):

        return_value = '{id} \t {tool} \t {user}'.format(id = self.__book_id,
                                                            tool = self.__tool.getName(), 
                                                            user = self.__user.getSurname())

        return return_value

    # --------------------------------------------------------------------
    # __repr__ function
    # --------------------------------------------------------------------
    def __repr__(self):

        return_value = '{id} \t {tool} \t {user}'.format(id = self.__book_id,
                                                            tool = self.__tool.getName(), 
                                                            user = self.__user.getSurname())

        return return_value
