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
        
    '''
    Function name: getBookingId()
    Task: returns the value of the booking ID
    '''
    def getBookingId(self):
        return self.book_id

    '''
    Function name: getTool()
    Task: returns the tool
    '''
    def getTool(self):
        return self.tool

    '''
    Function name: getUser()
    Task: returns the user
    '''
    def getUser(self):
        return self.user

    # __str__ function
    def __str__(self):

        returnValue = '{id} \t {tool} \t {username}'.format(id = self.book_id, tool = self.tool.getName(), user = self.user.getUsername())

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = '{id} \t {tool} \t {username}'.format(id = self.book_id, tool = self.tool.getName(), user = self.user.getUsername())

        return returnValue
