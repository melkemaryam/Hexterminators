import sqlite3
import pandas as pd
from DatabaseConnection import DatabaseConnection
from AvailabilityChecker import date_generator

class Tool:

    def searchTool(self):

        def load_data(path):
            # loads dataframe and returns it 
            # change 'csv' with whatever type the data frame is stored as    
            
            dataframe = pd.read_csv(path)
            return dataframe



        def choose_filters():
            # returns a list of the input variables
            # in_x means: user input of x (x = type, duration etc)
            
            print('''Select the type of tool: \n
            (M) Manual \n
            (E) Electric \n
            Leave blank for no filter''')
            
            # the above print statement can be replaced with a drop down list
            # like on more conventional filter tools
            
            in_type = input()
            
            # the variable stores the input which will be used later
            # to filter through the database
            
            print('''Select the duration (in days) for which you wish to hire the tool for: \n
            (1) 1 day  \n
            (2) 2 days \n
            (3) 3 days \n
            (+) 4+ days''')
            
            in_duration = input()
            
            # this function can be extended to include as many filters as needed
            
            return [in_type,in_duration] 

        # storing the filters in the variable
        filters = choose_filters() 



        def filter_data(lst):
            # argument will contain the list of inputs
            # returns filtered dataframe
            
            cols_to_filter = ["Type","Duration"] 
            # list of the filtrable columns - this can be implemented earlier in the code and it can be extended
            # this list has to match the 'filters' list
            
            filter_list = [] # we will save the filters here
            
            # iterating through each input
            for i in lst:
                if i != '':
                    filter_list.append(dataframe[cols_to_filter[i]] == lst[i])
            
            return dataframe.where(filter_list)


    def __init2__(self, chooseAction, chooseCategoryAdd, toolNameInput, typeNameInput, descriptionTool, dayPriceToolInput, halfDayPriceToolInput, availabilityToolInput, photoUploadTool, chooseCategoryRent, chooseTool, lengthOfBookingInput, inquireItemInput, bookingIdReturnInput):
    	self.chooseAction = chooseAction
        self.chooseCategoryAdd = chooseCategoryAdd
        self.toolNameInput = toolNameInput
		self.typeNameInput = typeNameInput
		self.descriptionToolInput = descriptionToolInput
		self.dayPriceToolInput = dayPriceToolInput
		self.halfDayPriceToolInput = halfDayPriceToolInput
		self.availabilityToolInput = availabilityToolInput
		self.photoUploadTool = photoUploadTool
		self.chooseCategoryRent = chooseCategoryRent
		self.chooseTool = chooseTool
		self.lengthOfBookingInput = lengthOfBookingInput
		self.inquireItemInput = inquireItemInput
        self.bookingIdReturnInput = bookingIdReturnInput


	#load DB

	def action(self):
		
		chooseAction = input("Please choose what you want to do next:\n 1: Add a new item\n 2: Rent an item\n 3: Inquire an item\n 4: Mark availability of one of your items\n")

		if chooseAction == 1:

            def addAnItem(self):

                #tools that enact chemical changes, including temperature and ignition, such as lighters and blowtorches.
                #Guiding, measuring and perception tools include the ruler, glasses, set square, sensors, straightedge, theodolite, microscope, monitor, clock, phone, printer
                #Shaping tools, such as molds, jigs, trowels.
                #Fastening tools, such as welders, rivet guns, nail guns, or glue guns.
                #Wikipedia: https://en.wikipedia.org/wiki/Tool#Tool_substitution 1.12.2019 3:08 am
		
		
                chooseCategoryAdd = input("Please choose the category of the item that you want to add:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")

                #save all the data in the DB with assigned toolId
                toolNameInput = input("Please enter the full name of your tool:\n")

                while toolNameInput == "":
        					toolNameInput = input("Please try again:\n")

                typeNameInput = input("Please enter the type of the item:\n")

                while typeNameInput == "":
    					typeNameInput = input("Please try again:\n")

                descriptionToolInput = input("Please enter a short description that also displays the condition and size of your tool:\n")

                while descriptionToolInput == "":
    					descriptionToolInput = input("Please try again:\n")

                dayPriceToolInput = float(input("Please enter the price in Pounds for a day rent\n"))

                while dayPriceToolInput == "":
    					dayPriceToolInput = input("Please try again:\n")

                halfDayPriceToolInput = float(input("Please enter the price in Pounds for half a day\n"))

                while halfDayPriceToolInput == "":
    					halfDayPriceToolInput = input("Please try again:\n")

                #availabilityToolInput = input("Please enter the start and the end date of the availability of this particular tool: dd.mm.yyyy - dd.mm.yyyy\n")

                #while availabilityToolInput == "":
    		#			availabilityToolInput = input("Please try again:\n")
		
		DatabaseConnection.CreateDBConnection()
		cursor.execute('SELECT count(*) FROM tools')
		newToolID = int(cursor.fetchone()) + 1
        cursor.execute('INSERT INTO Tools (cust_id, tool_id, tool_name, tool_cat, price, available, half_price) VALUES(owner_id, newToolID, toolNameInput, typeNameInput, dayPriceToolInput, 1, halfDayPriceToolInput)')
        
        AvailabilityChecker.get_availability(tool_id)
       #marking availability for 6 weeks ahead 
        DatabaseConnection.CloseConnection()
				
                photoUploadTool = input("Do you want to upload a photo of your tool? 1: Yes or 0: No") 
                if photoUploadTool == 1: 
                    #upload photo from desktop folder
                    print("Thank you very much. Your new tool with the photo has been added to our Database.")
                else:
                    print("Thank you very much. Your new tool has been added to our Database.")

		if chooseAction == 2:

            def rentAnItem(self):

                #def rentAnItem(self):


                chooseCategoryRent = input("Please choose the category of the item you want to rent:\n 1: measuring\n 2: shaping\n 3: fastening\n 4: mechanical\n 5: cutting\n")

                while chooseCategoryRent.isdigit() == False:
                    chooseCategoryRent = input("Please try again:\n")

                if chooseCategoryRent == 1 or 2 or 3 or 4 or 5:
                    	DatabaseConnection.CreateDBConnection()
			cursor.execute('SELECT tool_name FROM Tools WHERE tool_cat= ?', chooseCategoryRent)
			toolsListbyCategory = cursor.fetchall()
			DatabaseConnection.CloseConnection()
			print ("Please find the list of available items from selected category below:\n", toolsListbyCategory)
                    	chooseTool = input("Please enter the name of the tool you want to rent\n")
			
                #if chooseCategoryRent == 2:
                    #list of all the shaping tools in the DB plus amount of pieces of each tool
                    #chooseTool = input("Please enter the name of the tool you want to rent\n")

                #if chooseCategoryRent == 3:
                    #list of all the fastening tools in the DB plus amount of pieces of each tool
                    #chooseTool = input("Please enter the name of the tool you want to rent\n")

                #if chooseCategoryRent == 4:
                    #list of all the mechanical tools in the DB plus amount of pieces of each tool
                    #chooseTool = input("Please enter the name of the tool you want to rent\n")

		#if chooseCategoryRent == 5:
			#list of all the cutting tools in the DB plus amount of pieces of each tool
			#chooseTool = input("Please enter the name of the tool you want to rent\n")
			
                else chooseCategoryRent != 1 or 2 or 3 or 4 or 5:
                    	chooseCategoryRent = input("Your Input was invalid. Please try to enter it again and choose the category of your item:\n 1: measuring\n 2: shaping\n 3: fastening\n 4: mechanical\n")



                lengthOfBookingInput = input("Please enter the length of your booking. You can book a tool for at least half a day (0.5) and not more than 3.0 days.\n")

                while lengthOfBookingInput == "":
                    lengthOfBookingInput = input("Please try again.")

                if lengthOfBookingInput != 0.5 or 1.0 or 1.5 or 2.0 or 2.5 or 3.0 or 1 or 2 or 3:
                    lengthOfBookingInput = input("This was an invalid entry. Please try again.")
		
		Delivery = input("We do offer delivery services should you not be able to collect the tool yourself. Would you be interested in ordering delivery for your tool (y/n)?.\n")

		while Delivery == "":
                    Delivery = input("Please try again.")

                if Delivery != 'y' or 'n':
                    Delivery = input("This was an invalid entry. Please try again.")
		
		if Delivery = 'y':
			Delivery = 1
		else Delivery = 0
		
		DatabaseConnection.CreateDBConnection()
		cursor.execute('UPDATE Tools SET available= 0 WHERE tool_name= ? AND available = 1 LIMIT 1', chooseTool)
		today = datetime.datetime().now
		cursor.execute('UPDATE Booking availabile = 0 WHERE tool_id = ? AND date = ?',)
		DatabaseConnection.CloseConnection()

		if chooseAction == 3:
			inquireItemInput = input("Please choose between three different actions: 1: Details of the items you are renting\n 2: Details of the items that you uploaded\n 3: Item lost\n 4: Return item\n")

            while inquireItemInput.isdigit() == False:
    			inquireItemInput = input("Please try again:\n")

            if inquireItemInput == 1:
                #show list from DB of all the information of the details of the items that the person rented
                print("These are the items that you are renting at the moment:\n")

            if inquireItemInput == 2:
                #show list of all the information of the details of the items that the person owns
                print("These are all the items that you uploaded to SharedPower:\n")

            if inquireItemInput == 3:
                #connection to insurance
                print("You will be connected to the insurance")

            if inquireItemInput == 4:
                bookingIdReturnInput = input("Please enter the booking ID of the item that you want to return")

                while bookingIdReturnInput.isdigit() == False:
    				bookingIdReturnInput = input("Please try again:\n")

                #check whether this ID is correct and is in the rented register of that person
                #check whether return is overdue
                #if overdue -> calculate extra fee
       
        if chooseAction == 4:
            
            def markAvailability():

                #show list of all tools that person owns
                maToolInput = input("For which item do you want to change the availability state?\n")

                #if state == unavailable:
                    #state.available
                #else:
                    #state.unavailable








		#if chooseAction != 1 or 2 or 3:
