''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: BookingManager.py

Created: 27th December 2019

-------------------------------------------------
'''

from datetime import datetime

from ToolManager import ToolManager
from BookingManager import BookingManager
from UserManager import UserManager
from ToolCategory import ToolCategory

from Tools import Tools
from Bookings import Bookings
from CheckInputs import CheckInputs


class Menu:
       
    #Constructor
    def __init__(self, databaseFilename, registeredUser):

        self.databaseFilename = databaseFilename
        self.registeredUser = registeredUser

    def checkAccount(self):
    
        registeredUser = None

        while (registeredUser == None):
            haveAccount = input("Welcome to SharedPower. \nDo you already have an account? 1: Yes or 2: No. Press 3 for Exit.\n")
            
        while (haveAccount.isdigit() == False):
            haveAccount = input("Please try again:\n")

        haveAccount = int(haveAccount)
    
        if(haveAccount == 1):
            # Call the method to register the new user - this will return us a user object
            registeredUser = self.signIn()
        
        elif(haveAccount == 2):
            # Call the method to validate an existing user - this will return us a user object
            registeredUser = self.signUp()

        else:
            # The user has typed a number that is not on the menu so let's just exit the while loop
            break
            
        return registeredUser

    

    '''
    Function name: signUp()
    Task: lets a new user sign up for a new account
    '''
    def signUp(self):

        newUser = None
        
        userManager = UserManager(self.databaseFilename)

        username = input("Please sign up here.\nPlease come up with an unique username:\n")
        while username == "":
            username = input("Please try again:\n")

        password = input("Please enter a safe password,\n password should contain at least one upper case letter, one lower case letter, one digit and one special character:\n")
        validatePass = CheckInputs.passwordCheck(password)
        while password == "" or validatePass == False:
            password = input("Please try again:\n")

        F_name = input("Please enter your first name:\n")
        while F_name == "" or F_name.isdigit() == True:
            F_name = input("Please try again:\n")

        L_name = input("Please enter your last name:\n")
        while L_name == "" or L_name.isdigit() == True:
            L_name = input("Please try again:\n")

        tel_no = input("Last but not least, we need your email address for verification:\n")
        while tel_no == "" or tel_no.isdigit() == False:
            tel_no = input("Please try again:\n")

        email = input("Last but not least, we need your email address for verification:\n")
        CheckInputs.emailCheck(email)
        while email == "" or validationE == False:
            email = input("Please try again:\n")

        print("Please enter your bank details:\n")
        address1 = input("Address Line 1:\n")
        while address1 == "":
            address1 = input("Please try again:\n")

        address2 = input("Address Line 2:\n")
        while address2 == "":
            address2 = input("Please try again:\n")

        postcode = input("Post Code:\n")
        validationP = CheckInputs.postCodeCheck(postcode)
        while postcode == "" or validationP == False:
            postcode = input("Please try again:\n")
        
        acc_no = input("Account Number:\n")
        validationA = CheckInputs.accNoCheck(acc_no)
        while acc_no == "" or validationA == False:
            acc_no = input("Please try again:\n")

        sort_code = input("Sort Code:\n")
        validationS = CheckInputs.sortCodeCheck(sort_code)
        while sort_code == "" or validationS == False:
            sort_code = input("Please try again:\n")

        branch_name = input("Post Code:\n")
        while postcode == "":
            postcode = input("Please try again:\n")


        # create new user in the DB
        newUser = userManager.createUser(username, password, F_name, L_name, tel_no, email, address1, address2, postcode, acc_no, sort_code, branch_name)

        return newUser

    '''
    Function name: signIn()
    Task: lets existing user sign in
    '''

    def signIn(self):

        confirmUser = None
        
        userManager = UserManager(self.databaseFilename)

        username = input('Please enter the your username: ')
        password = input('Please enter the your password: ')

        confirmUser = userManager.confirmUser(username, password)

        return confirmUser


    '''
    Function name: action()
    Task: interaction with the user
    '''

    def action(self):

        userInput = 0

        while (userInput < 6):

            # Display the login and register menu
            print('\nSharedPower')
            print('---------')
            print('1. Search for tools by name.')
            print('2. Search for tools by category.')
            print('3. List future tool bookings.')
            print('4. Rent a tool.')
            print('5. Add a tool.')
            #print("Mark Availablity.")
            print('6. Exit')

            userInput = input('Please choose an action: ')

            while (userInput.isdigit() == False):
                print('Please enter a number between 1 and 6:')
                userInput = input('Please choose an action: ')

            userInput = int(userInput)
    
            if (userInput == 1):
                self.searchToolByName()

            elif (userInput == 2):
                self.searchToolByCategory()

            elif (userInput == 3):
                self.showFutureTools()

            elif (userInput == 4):
                self.rentATool()

            elif (userInput == 5):
                self.addATool()

            else:
                break

    '''
    Function name: searchToolByName()
    Task: lets a user search for a tool by name
    '''
    def searchToolByName(self):

        toolManager = ToolManager(self.databaseFilename)

        userInput = input('Please enter the name (or part of it) for the tool you are searching for: ')

        # search
        tools = toolManager.searchToolByName(userInput)

        # show results
        self.ToolList(tools)

    '''
    Function name: searchToolByCat()
    Task: lets a user search for a tool by category
    '''
    def searchToolByCategory(self):

        toolManager = ToolManager(self.databaseFilename)

        search_criteria = ToolCategory.getToolCatFromUser()

        # search
        tools = toolManager.searchToolByCategory(search_criteria)

        # show results
        self.ToolList(tools)

    '''
    Function name: showFutureTools()
    Task: shows the user future tools
    '''
    def showFutureTools(self):

        toolManager = toolManager(self.databaseFilename)

        # specify future
        range_start = datetime.now()

        userInput = input('How many days ahead do you want to look: ')

        # Check we have got a number from the user
        while (userInput.isdigit() == False):
            print('Please only enter numbers.')
            userInput = input('How many days ahead do you want to look: ')

        days_ahead = int(userInput)

        # list from all the future tools
        futureTools = toolManager.loadFutureTools(range_start, days_ahead)

        # show results
        self.ToolList(futureTools)

    '''
    Function name: showFutureRentedTools()
    Task: shows the user future tools that have already been rented
    '''
    def shwoFutureRentedTools(self):

        bookingManager = BookingManager(self.databaseFilename)

        # get list
        futureTools = bookingManager.searchFutureBookings(self.registeredUser)

        # shwo results
        self.displayToolHeaders()

        for Bookings in futureTools:
            tool = Bookings.getTool()
            print(tool)

    '''
    Function name: rentATool()
    Task: lets a user rent a new tool
    '''
    def rentATool(self):

        toolManager = toolManager(self.databaseFilename)

        booking_manager = BookingManager(self.databaseFilename)

        # specify the category of the tool
        catOfTool = ToolCategory.gettoolcategoryFromUser()

        # Ask the tool manager for any upcoming tools of this category
        availableTools = toolManager.searchToolByCategory(catOfTool)

        # Display the tools that have been returned
        self.ToolList(available_tools)

        selectedTool = None

        while (selectedTool == None):

            # ask for name of the tool
            userInput = input('Please enter the name of the tool you want to rent: ')
            
            while userInput == "":
                userInput = input("Please try again:\n")
 
            # load tool
            selectedTool = toolManager.loadToolName(userInput)
        
            # show results
            self.tool(selectedTool)

            # specify id of the tool
            userInput = input('Please enter the id number of the tool you want to rent: ')

            # check if number
            while (userInput.isdigit() == False):
                print('Please only enter numbers.')
                userInput = input('Please enter the id number of the tool you want to rent: ')

            userInput = int(userInput)

            # Load the selected to confirm it
            selectedTool = toolManager.loadToolId(userInput)

        # show results
        self.displayTool(selectedTool)

        # Create the booking now
        newBooking = bookingManager.createBooking(selectedTool, self.registeredUser)

        # show to user
        print('\nYou have successfully rented a tool:\n')
        self.displayToolHeaders()
        print(newBooking.getTool())
        


    
    # --------------------------------------------------------------------
    # __display_tool_list
    # Display the tools in an organised list
    # --------------------------------------------------------------------
    def __display_tool_list(self, tool_list):

        self.__display_tool_headers()

        # Iterate through the list printing out each tool as we go
        for tool in tool_list:
            print(tool)

    # --------------------------------------------------------------------
    # __display_tool
    # Display the tools
    # --------------------------------------------------------------------
    def __display_tool(self, tool):

        self.__display_tool_headers()
        print(tool)

    # --------------------------------------------------------------------
    # __display_tool_headers
    # Display the tool headers
    # --------------------------------------------------------------------
    def __display_tool_headers(self):

        # Iterate through the list printing out each tool as we go
        print('id \t name \t \t \t \t trainer \t \t start \t \t \t end \t \t \t duration \t category')
        print('-- \t ---- \t \t \t \t ------- \t \t ----- \t \t \t --- \t \t \t -------- \t ----')
