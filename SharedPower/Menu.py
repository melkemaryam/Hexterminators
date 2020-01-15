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
from User import User


class Menu:
       
    #Constructor
    def __init__(self, databaseFilename, registeredUser):

        self.databaseFilename = databaseFilename
        self.registeredUser = registeredUser

    def checkAccount(self):
    
        haveAccount = 0
        registeredUser = None

        while (haveAccount < 3):

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

            elif(haveAccount == 3):
                # Call the method to kill app - exit kinda
                quit()

            else:
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
        validatePass = CheckInputs.passwordCheck(newUser, password)
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
        validationE = CheckInputs.emailCheck(newUser, email)
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
        validationP = CheckInputs.postCodeCheck(newUser, postcode)
        while postcode == "" or validationP == False:
            postcode = input("Please try again:\n")
        
        acc_no = input("Account Number:\n")
        validationA = CheckInputs.accNoCheck(newUser, acc_no)
        while acc_no == "" or validationA == False:
            acc_no = input("Please try again:\n")

        sort_code = input("Sort Code:\n")
        validationS = CheckInputs.sortCodeCheck(newUser, sort_code)
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

        while (userInput < 8):

            # Display the login and register menu
            print('\nSharedPower')
            print('---------')
            print('1. Search for tools by name.')
            print('2. Search for tools by category.')
            print('3. List future tool bookings.')
            print('4. Rent a tool.')
            print('5. Add a tool.')
            print('6. Return a tool.')
            print('7. Report a broken tool.')
            print('8. Exit')

            userInput = input('Please choose an action: ')

            while (userInput.isdigit() == False):
                print('Please enter a number between 1 and 7:')
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

            elif (userInput == 6):
                self.markAvailability()

            elif (userInput == 7):
                self.returnATool()

            elif(userInput == 8):
                quit()

            else:
                print('Please enter a number between 1 and 7:')
                userInput = input('Please choose an action: ')

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
        self.toolList(tools)

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
        self.toolList(tools)

    '''
    Function name: showFutureTools()
    Task: shows the user future tools
    '''
    def showFutureTools(self):

        toolManager = ToolManager(self.databaseFilename)

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
        self.toolList(futureTools)

    '''
    Function name: showFutureRentedTools()
    Task: shows the user future tools that have already been rented
    '''
    def shwoFutureRentedTools(self):

        bookingManager = BookingManager(self.databaseFilename)

        # get list
        futureTools = bookingManager.searchFutureBookings(self.registeredUser)

        # shwo results
        self.toolHeaders()

        for Bookings in futureTools:
            tool = Bookings.getTool()
            print(tool)

    '''
    Function name: rentATool()
    Task: lets a user rent a new tool
    '''
    def rentATool(self):

        toolManager = ToolManager(self.databaseFilename)

        bookingManager = BookingManager(self.databaseFilename)

        # specify the category of the tool
        catOfTool = ToolCategory.getToolCatFromUser()

        # Ask the tool manager for any upcoming tools of this category
        availableTools = toolManager.searchToolByCategory(catOfTool)

        # show results
        self.toolList(availableTools)

        selectedTool = None

        while (selectedTool == None):

            # ask for name of the tool
            userInput = input('Please enter the name of the tool you want to rent: ')
            
            while userInput == "":
                userInput = input("Please try again:\n")
 
            # load tool
            selectedTool = toolManager.loadToolName(userInput)
        
            # show results
            self.showTool(selectedTool)

            # specify id of the tool
            userInput = input('Please enter the ID number of the tool you want to rent: ')

            # check if number
            while (userInput.isdigit() == False):
                print('Please only enter numbers.')
                userInput = input('Please enter the ID number of the tool you want to rent: ')

            userInput = int(userInput)

            # Load the selected tool to confirm it
            selectedTool = toolManager.loadToolId(userInput)

        # show results
        self.showTool(selectedTool)

        # Create the booking now
        newBooking = bookingManager.createBooking(selectedTool, self.registeredUser)

        # show to user
        print('\nYou have successfully rented a tool:\n')
        self.toolHeaders()
        print(newBooking.getTool())
    
    '''
    Function name: addATool()
    Task: lets a user add a new tool
    '''

    def addATool(self):
    
        newTool = None
    
        toolManager = ToolManager(self.databaseFilename)

        # Get new information
        tool_name = input("Please enter the full name of your tool:\n")

        while tool_name == "":
        	tool_name = input("Please try again:\n")

        tool_cat = ToolCategory.getToolCatFromUser()
        while tool_cat == "":
    	    tool_cat= input("Please try again:\n")

        tool_desc = input("Please enter a short description that also displays the condition and size of your tool:\n")

        while tool_desc == "":
            tool_desc = input("Please try again:\n")

        price = input("Please enter the price in Pounds for a day rent:\n")

        while (price.isdigit() == False):
            print('Please only enter whole numbers.\n')
            price = input('Please enter the price in Pounds for a day rent:\n')

        price = int(price)

        halfDayPrice = input("Please enter the price in Pounds for a half day rent:\n")

        while (halfDayPrice.isdigit() == False):
            print('Please only enter whole numbers.\n')
            halfDayPrice = input('Please enter the price in Pounds for a half day rent:\n')

        halfDayPrice = int(halfDayPrice)

		# Connecting to the DB
        #DatabaseConnection.CreateDBConnection()
        #cursor.execute('SELECT count(*) FROM tools')
        #newToolID = int(cursor.fetchone()) + 1
        #cursor.execute('INSERT INTO Tools (cust_id, tool_id, tool_name, tool_cat, price, available, half_price) VALUES(owner_id, newToolID, toolNameInput, categoryNameInput, dayPriceToolInput, 1, halfDayPriceToolInput)')
                
        #AvailabilityChecker.get_availability(tool_id)
        #marking availability for 6 weeks ahead 
        #DatabaseConnection.CloseDBConnection()
		# Disconnecting from the DB
        #photoUploadTool = input("Do you want to upload a photo of your tool? 1: Yes or 0: No") 
        #if photoUploadTool == 1: 
            #upload photo from desktop folder
            #print("Thank you very much. Your new tool with the photo has been added to our Database.")
        #else:
            #print("Thank you very much. Your new tool has been added to our Database.")

        #Notes.Rent(tool_id, descriptionToolInput)

        # create new tool
        newTool = toolManager.createTool(self.registeredUser, tool_name, tool_cat, tool_desc, price, halfDayPrice)

        # The new session should now be created so we can advise the user and then return
        print('\nYou have successfully added a new tool')

    def markAvailability(self):

        book_id = input("Please enter the number of booking we should pick up for investigation:\n")

        while book_id == "":
        	book_id = input("Please try again:\n")

        tool_id = ToolManager.loadToolName(self.registeredUser, book_id)[1]

        brokenNoteInput = input("Please describe damage to the item\n")
        
        while brokenNoteInput == "":
        	brokenNoteInput = input("Please do not leave this field empty\n")

        BookingManager.markAvailability(self.registeredUser, tool_id)
        BookingManager.bookOutNotes(self.registeredUser, book_id, brokenNoteInput)
        
        print ("Thank you. Your note has been saved and will be passed onto insurance company to start the claim.\n")
    
    '''
    Function name: returnATool()
    Task: puts tool back on virtual shelf and adds any extra charges should the tool be returned past the renting date
    '''

    def returnATool(self):

        book_id = input("Please enter the number of bookings you would like to finalise:\n")

        while book_id == "":
        	book_id = input("Please try again:\n")

        BookingManager.returnItem(self.registeredUser, book_id)

        print ("Thank you. Your booking has been finalised. Please find the details in the invoice send to you on 1st of the next month.\n")


    '''
    Function name: toolList()
    Task: shows all the tools in a list
    '''
    def toolList(self, tool_list):

        self.toolHeaders()

        # Iterate through the list printing out each tool as we go
        for tool in tool_list:
            print(tool)

    '''
    Function name: showTool()
    Task: shows the tool
    '''
    def showTool(self, tool):

        self.toolHeaders()
        print(tool)

    '''
    Function name: toolHeaders()
    Task: shows the header for showing tools
    '''
    def toolHeaders(self):

        # Iterate through the list printing out each tool as we go
        print('id \t name \t \t \t \t category \t \t \t description \t \t \t price \t half day price')
        print('-- \t ---- \t \t \t \t ----- \t \t \t --- \t \t \t -------- \t ----')
