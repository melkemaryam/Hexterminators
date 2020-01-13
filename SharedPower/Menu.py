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

from Tools import Tools
from Bookings import Bookings


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

    # --------------------------------------------------------------------
    # Private Functions
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # __register_new_user
    # Register a new customer user and save the details into the database.
    # --------------------------------------------------------------------
    def signUp(self):

        newUser = None
        
        userManager = UserManager(self.databaseFilename)

        usernameInputSU = input("Please sign up here.\nPlease come up with an unique username:\n")

		while usernameInputSU == "":
			usernameInputSU = input("Please try again:\n")

		passwordInputSU = input("Please enter a safe password:\n")

		while passwordInputSU == "":
			passwordInputSU = input("Please try again:\n")

		firstNameInputSU = input("Please enter your first name:\n")

		while firstNameInputSU == "":
			firstNameInputSU = input("Please try again:\n")

		lastNameInputSU = input("Please enter your last name:\n")

		while lastNameInputSU == "":
			lastNameInputSU = input("Please try again:\n")

        emailInputSU = input("Last but not least, we need your email address for verification:\n")

		while emailInputSU == "":
		    emailInputSU = input("Please try again:\n")

        emailInputSU = input("Last but not least, we need your email address for verification:\n")

		while emailInputSU == "":
		    emailInputSU = input("Please try again:\n")

		print("Please enter your bank details:\n")
		streetInputSU = input("Address Line 1:\n")

		while streetInputSU == "":
			streetInputSU = input("Please try again:\n")

		streetNumberInputSU = input("Address Line 2:\n")
		while streetNumberInputSU.isdigit() == False:
			streetNumberInputSU	= input("Please try again:\n")

		zipCodeInputSU = input("Post Code:\n")
		    while zipCodeInputSU == "":
				zipCodeInputSU = input("Please try again:\n")
        
        accountNumberInputSU = input("Account Number:\n")
		while accountNumberInputSU.isdigit() == False:
			accountNumberInputSU = input("Please try again:\n")

		sortCodeInputSU = input("Sort Code:\n")
		while sortCodeInputSU.isdigit() == False:
			sortCodeInputSU = input("Please try again:\n")


        # create new user in teh DB
        newUser = userManager.createUser(F_name, L_name, email, password)

        return newUser

    # --------------------------------------------------------------------
    # __validate_existing_user
    # Attempt to validate an existing user with their email and password
    # --------------------------------------------------------------------
    def __validate_existing_user(self):

        validated_user = None
        
        # Create a UserManager and pass in the filename for the database
        user_manager = UserManager(self.__database_filename)

        # Get the new user details from the user
        user_email      = input('Please enter the your email: ')
        user_password   = input('Please enter the your password: ')

        # Attempt to validate a user using their email address and password
        validated_user = user_manager.validate_user(user_email, user_password)

        # We can now return this user to the caller
        return validated_user


    # --------------------------------------------------------------------
    # action
    # Display and handle requests from the main menu.
    # --------------------------------------------------------------------
    def action(self):

        user_input = 0

        while (user_input < 6):

            # Display the login and register menu
            print('\nMain Menu')
            print('---------')
            print('1. Search for tools by name.')
            print('2. Search for tools by category.')
            print('3. List future tool bookings.')
            print('4. Book a tool.')
            print('5. Add a tool.')
            #print("Mark Availablity.")
            print('6. Exit')

            user_input = input('Please make a selection: ')

            # Check we have got a number from the user
            while (user_input.isdigit() == False):
                print('Please only enter numbers.')
                user_input = input('Please make a selection: ')

            # We are happy that the user has entered a number so we can safely convert it
            user_input = int(user_input)
    
            if (user_input == 1):
                self.__searchToolByName()

            elif (user_input == 2):
                self.__searchToolByCategory()

            elif (user_input == 3):
                self.__show_future_tools()

            elif (user_input == 4):
                self.__book_tool()

            elif (user_input == 5):
                self.__show_future_bookings()

            else:
                # The user has categoryd a number that is not on the menu so let's just exit the while loop
                break

    # --------------------------------------------------------------------
    # Private Functions
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # __searchToolByName
    # Search for future tools by name
    # --------------------------------------------------------------------
    def __searchToolByName(self):

        # Create a toolManager and pass in the filename for the database
        tool_manager = ToolManager(self.databaseFilename)

        # Ask the user for the search criteria
        user_input = input('Please enter the name (or part of it) for the tool you are searching for: ')

        # Perform the search
        future_tools = tool_manager.searchToolByName(user_input)

        # Display the tools that have been returned
        self.__display_tool_list(future_tools)

    # --------------------------------------------------------------------
    # __searchToolByCategory
    # Search for future tools by category
    # --------------------------------------------------------------------
    def __searchToolByCategory(self):

        # Create a toolManager and pass in the filename for the database
        tool_manager = ToolManager(self.databaseFilename)

        # Ask the user for the category of tool they want to search for
        search_criteria = toolcategoryHelpers.GettoolcategoryFromUser()

        # Perform the search
        future_tools = tool_manager.searchToolByCategory(search_criteria)

        # Display the tools that have been returned
        self.__display_tool_list(future_tools)

    # --------------------------------------------------------------------
    # __show_future_tools
    # List all of the future tools
    # --------------------------------------------------------------------
    def __show_future_tools(self):

        # Create a toolManager and pass in the filename for the database
        tool_manager = toolManager(self.databaseFilename)

        # We only want to see tools that are in the future
        range_start = datetime.now()

        # Ask the user how many days ahead they want to look
        user_input = input('How many days ahead do you want to look: ')

        # Check we have got a number from the user
        while (user_input.isdigit() == False):
            print('Please only enter numbers.')
            user_input = input('How many days ahead do you want to look: ')

        days_ahead = int(user_input)

        # Get a list of all the future tools from the tool manager
        future_tools = tool_manager.load_future_tools(range_start, days_ahead)

        # Display the tools that have been returned
        self.__display_tool_list(future_tools)

    # --------------------------------------------------------------------
    # __show_future_bookinga
    # List all of the future bookings
    # --------------------------------------------------------------------
    def __show_future_bookings(self):

        # Create a BookingManager and pass in the filename for the database
        booking_manager = BookingManager(self.__databaseFilename)

        # Get a list of all the future bookings from the booking manager
        future_bookings = booking_manager.SearchFutureBookings(self.__registered_user)

        # Print the tools associated with the booking
        self.__display_tool_headers()

        for booking in future_bookings:
            tool = booking.gettool()
            print(tool)

    # --------------------------------------------------------------------
    # __book_tool
    # Book a tool
    # --------------------------------------------------------------------
    def __book_tool(self):

        # Create a toolManager and pass in the filename for the database
        tool_manager = toolManager(self.__databaseFilename)

        # Create a BookingManager as pass in the filename for the database
        booking_manager = BookingManager(self.__databaseFilename)

        # Ask the user to specify the category of tool they want to book
        category_of_tool = toolcategoryHelpers.GettoolcategoryFromUser()

        # Ask the tool manager for any upcoming tools of this category
        available_tools = tool_manager.searchToolByCategory(category_of_tool)

        # Display the tools that have been returned
        self.__display_tool_list(available_tools)

        selected_tool = None

        while (selected_tool == None):

            # Ask the user to specify the tool they want to book
            user_input = input('Please enter the id number of the tool you want to book: ')

            # Check we have got a number from the user
            while (user_input.isdigit() == False):
                print('Please only enter numbers.')
                user_input = input('Please enter the id number of the tool you want to book: ')

            user_input = int(user_input)

            # Load the tool to confirm it
            selected_tool = tool_manager.load_tool_from_id(user_input)

        # Display the tool to the user
        self.__display_tool(selected_tool)

        # Create the booking now
        new_booking = booking_manager.createBooking(selected_tool, self.__registered_user)

        # We should now have our booking back - let's display it to the user
        print('\nBooking Confirmed!')
        self.__display_tool_headers()
        print(new_booking.gettool())
        
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
