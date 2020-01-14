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
    def __init__(self, cust_id, F_name, L_name, email, username, address1, address2, postcode, tel_no):
        
        self.cust_id = cust_id
        self.F_name = F_name
        self.L_name = L_name
        self.email = email
        self.username = username
        self.address1 = address1
        self.address2 = address2
        self.postcode = postcode
        self.tel_no = tel_no
        
    '''
    Function name: getId()
    Task: returns the value for the ID
    '''
    def getId(self):
        return self.cust_id

    '''
    Function name: setFirstName()
    Task: sets the first name of the user
    '''
    def setFirstName(self, newFirstname):
        self.F_name = newFirstname

    '''
    Function name: getFirstName()
    Task: returns the value of the first name of the user
    '''
    def getFirstName(self):
        return self.F_name

    '''
    Function name: setLastName()
    Task: sets the last name of the user
    '''
    def setLastName(self, newLastname):
        self.L_name = newLastname

    '''
    Function name: getLastName()
    Task: returns the last name of the user
    '''
    def getLastName(self):
        return self.L_name

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

    '''
    Function name: setUsername()
    Task: sets the username of the user
    '''
    def setUsername(self, newUsername):
        self.username = newUsername
    
    '''
    Function name: getUsername()
    Task: returns the value of the username of the user
    '''
    def getUsername(self):
        return self.username
    
    '''
    Function name: setAddress1()
    Task: sets the address line 1 of the user
    '''
    def setAddress1(self, newAddress1):
        self.address1 = newAddress1

    '''
    Function name: getAddress1()
    Task: returns the value of the address line 1 of the user
    '''
    def getAddress1(self):
        return self.address1

    '''
    Function name: setAddress2()
    Task: sets the address line 2 of the user
    '''
    def setAddress2(self, newAddress2):
        self.address2 = newAddress2

    '''
    Function name: getAddress2()
    Task: returns the value of the address line 2 of the user
    '''
    def getAddress2(self):
        return self.address2

    '''
    Function name: setPostcode()
    Task: sets the postcode of the user
    '''
    def setPostcode(self, newPostcode):
        self.postcode = newPostcode

    '''
    Function name: getPostcode()
    Task: returns the value of the postcode of the user
    '''
    def getPostcode(self):
        return self.postcode

    '''
    Function name: setTelNo()
    Task: sets the telephone number of the user
    '''
    def setTelNo(self, newTelNo):
        self.tel_no = newTelNo
    
    '''
    Function name: getTelNo()
    Task: returns the value of the telephone number of the user
    '''
    def getTelNo(self):
        return self.tel_no

    

    # __str__ function
    def __str__(self):

        returnValue = ('%i \t %s \t \t %s \t \t %s \t \t %s \t \t %s \t \t %s \t \t %s \t \t %s' % (self.cust_id, self.F_name, self.L_name, self.email, self.username, self.address1, self.address2, self.postcode, self.tel_no))

        return returnValue

    # __repr__ function
    def __repr__(self):

        returnValue = ('%i \t %s \t \t %s \t \t %s \t \t %s \t \t %s \t \t %s \t \t %s \t \t %s' % (self.cust_id, self.F_name, self.L_name, self.email, self.username, self.address1, self.address2, self.postcode, self.tel_no))

        return returnValue
