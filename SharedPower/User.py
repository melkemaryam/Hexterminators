''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: User.py

Created: 10th January 2020

-------------------------------------------------
'''

class User:

    # --------------------------------------------------------------------
    # Constructor
    # --------------------------------------------------------------------
    def __init__(self, cust_id, F_name, L_name, email):
        
        # Transfer our incoming parameters to the member variables for this class
        self.__id          = cust_id
        self.__forename    = F_name
        self.__surname     = L_name
        self.__email       = email
        
    # --------------------------------------------------------------------
    # Returns the user id
    # --------------------------------------------------------------------
    def getId(self):
        return self.__id

    # --------------------------------------------------------------------
    # Sets the user forename
    # --------------------------------------------------------------------
    def setForename(self, new_forename):
        self.__forename = new_forename

    # --------------------------------------------------------------------
    # Returns the user forename
    # --------------------------------------------------------------------
    def getForename(self):
        return self.__forename

    # --------------------------------------------------------------------
    # Sets the user surname
    # --------------------------------------------------------------------
    def setSurname(self, new_surname):
        self.__surname = new_surname

    # --------------------------------------------------------------------
    # Returns the user surname
    # --------------------------------------------------------------------
    def getSurname(self):
        return self.__surname

    # --------------------------------------------------------------------
    # Sets the user email
    # --------------------------------------------------------------------
    def setEmail(self, new_email):
        self.__email = new_email

    # --------------------------------------------------------------------
    # Returns the user email
    # --------------------------------------------------------------------
    def getEmail(self):
        return self.__email

    # --------------------------------------------------------------------
    # __str__ function
    # --------------------------------------------------------------------
    def __str__(self):

        returnValue = ('%i \t %s \t \t %s \t \t %s' % (self.__id,
                                                                self.__forename,
                                                                self.__surname,
                                                                self.__email))

        return returnValue

    # --------------------------------------------------------------------
    # __repr__ function
    # --------------------------------------------------------------------
    def __repr__(self):

        returnValue = ('%i \t %s \t \t %s \t \t %s' % (self.__id,
                                                                self.__forename,
                                                                self.__surname,
                                                                self.__email))

        return returnValue
