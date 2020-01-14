''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: User.py

Created: 10th January 2020

-------------------------------------------------
'''

class User:

    #Constructor
    def __init__(self, cust_id, F_name, L_name, email):
        
        self.id = cust_id
        self.firstname = F_name
        self.lastname = L_name
        self.email = email
        
    '''
    Function name: getId()
    Task: returns the value for the ID
    '''
    def getId(self):
        return self.id

    '''
    Function name: setFirstName()
    Task: sets the first name of the user
    '''
    def setFirstName(self, newFirstname):
        self.firstname = newFirstname

    '''
    Function name: getFirstName()
    Task: returns the value of the first name of the user
    '''
    def getFirstName(self):
        return self.firstname

    '''
    Function name: setLastName()
    Task: sets the last name of the user
    '''
    def setLastName(self, newLastname):
        self.lastname = newLastname

    '''
    Function name: getLastName()
    Task: returns the last name of the user
    '''
    def getLastName(self):
        return self.lastname

    '''
    Function name: setEmail()
    Task: sets the email address of the user
    '''
    def setEmail(self, newEmail):
        self.email = newEmail

    '''
    Function name: getEmail()
    Task: returns the value of the email of the user
    '''
    def getEmail(self):
        return self.email

    # __str__ function
    def __str__(self):

        returnValue = ('%i \t %s \t \t %s \t \t %s' % (self.id, self.firstname, self.lastname, self.email))

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = ('%i \t %s \t \t %s \t \t %s' % (self.id, self.firstname, self.lastname, self.email))

        return returnValue
