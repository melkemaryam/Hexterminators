''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Tools.py

Created: 10th January 2020

-------------------------------------------------
'''

from datetime import datetime
from datetime import timedelta

from Classes.Helpers.StringHelpers import StringHelpers

class Tools:

    # --------------------------------------------------------------------
    # Constructor
    # --------------------------------------------------------------------
    def __init__(self, tool_id, user, tool_name, tool_start, tool_duration, tool_cat, price):

        # Transfer our incoming parameters to the member variables for this class
        self.__tool_id       = tool_id
        self.__tool_user     = user
        self.__tool_name     = tool_name
        self.__tool_start    = tool_start
        self.__tool_duration = tool_duration
        self.__tool_end      = self.__tool_start + timedelta(days = self.__tool_duration)
        self.__tool_cat      = tool_cat
        self.__price         = price
        
    # --------------------------------------------------------------------
    # Returns the tool id
    # --------------------------------------------------------------------
    def getId(self):
        return self.__tool_id

    # --------------------------------------------------------------------
    # Returns the tool user
    # --------------------------------------------------------------------
    def getUser(self):
        return self.__tool_user

    # --------------------------------------------------------------------
    # Sets the tool name
    # --------------------------------------------------------------------
    def setName(self, new_name):
        self.__tool_name = new_name

    # --------------------------------------------------------------------
    # Returns the tool name
    # --------------------------------------------------------------------
    def getName(self):
        return self.__tool_name

    # --------------------------------------------------------------------
    # Sets the tool start date and time
    # --------------------------------------------------------------------
    def setStart(self, new_start):
        self.__tool_start = new_start

    # --------------------------------------------------------------------
    # Returns the tool start date and time
    # --------------------------------------------------------------------
    def getStart(self):
        return self.__tool_start

    # --------------------------------------------------------------------
    # Sets the tool duration
    # --------------------------------------------------------------------
    def setDuration(self, new_duration):
        self.__tool_duration = new_duration

    # --------------------------------------------------------------------
    # Returns the tool duration
    # --------------------------------------------------------------------
    def getDuration(self):
        return self.__tool_duration

    # --------------------------------------------------------------------
    # Returns the tool end date and time
    # --------------------------------------------------------------------
    def getEnd(self):        
        return self.__tool_end

    # --------------------------------------------------------------------
    # Sets the tool price
    # --------------------------------------------------------------------
    def setPrice(self, new_price):
        self.__tool_price = new_price

    # --------------------------------------------------------------------
    # Returns the tool price
    # --------------------------------------------------------------------
    def getPrice(self):
        return self.__tool_price

    # --------------------------------------------------------------------
    # Returns the tool type
    # --------------------------------------------------------------------
    def getCategory(self):
        return self.__tool_cat

    # --------------------------------------------------------------------
    # __str__ function
    # --------------------------------------------------------------------
    def __str__(self):

        return_value = '{id} \t {name} \t {user} \t \t {start} \t {end} \t {duration} \t \t {type}'.format(id = self.__tool_id, 
                                                                                                           name = StringHelpers.PadString(self.__tool_name, 30),
                                                                                                           user = self.__tool_user.getForename() + ' ' + self.__tool_user.getSurname(),
                                                                                                           start = self.__tool_start,
                                                                                                           end = self.__tool_end,
                                                                                                           duration = self.__tool_duration,
                                                                                                           type = self.__tool_cat)

        return return_value

    # --------------------------------------------------------------------
    # __repr__ function
    # --------------------------------------------------------------------
    def __repr__(self):

        return_value = '{id} \t {name} \t {user} \t \t {start} \t {end} \t {duration} \t \t {type}'.format(id = self.__tool_id, 
                                                                                                           name = StringHelpers.PadString(self.__tool_name, 30),
                                                                                                           user = self.__tool_user.getForename() + ' ' + self.__tool_user.getSurname(),
                                                                                                           start = self.__tool_start,
                                                                                                           end = self.__tool_end,
                                                                                                           duration = self.__tool_duration,
                                                                                                           type = self.__tool_cat)

        return return_value
