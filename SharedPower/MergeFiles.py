''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Tool.py

Created: 17th November 2019

-------------------------------------------------
'''

import sqlite3
import pandas as pd
from DatabaseConnection import DatabaseConnection
from AvailabilityChecker import AvailabilityChecker
from LateCharge import checkIfLate

class Tool:

'''
Function name: searchTool()
Task: Search for a tool 
'''
    def searchTool(self):

'''
Function name: load_data()
Task: Loads the data from the DB/ servers
'''
        def load_data(path):
            # loads dataframe and returns it 
            # change 'csv' with whatever category the data frame is stored as    
            
            dataframe = pd.read_csv(path)
            return dataframe


'''
Function name: choose_filters()
Task: Lets you apply the filters you want
'''
        def choose_filters():
            # returns a list of the input variables
            # in_x means: user input of x (x = category, duration etc)
            
            print('''Select the category of tool: \n
            (M) Manual \n
            (E) Electric \n
            Leave blank for no filter''')
            
            # the above print statement can be replaced with a drop down list
            # like on more conventional filter tools
            
            in_category = input()
            
            # the variable stores the input which will be used later
            # to filter through the database
            
            print('''Select the duration (in days) for which you wish to hire the tool for: \n
            (1) 1 day  \n
            (2) 2 days \n
            (3) 3 days \n
            (+) 4+ days''')
            
            in_duration = input()
            
            # this function can be extended to include as many filters as needed
            
            return [in_category,in_duration] 

        # storing the filters in the variable
        filters = choose_filters() 


'''
Function name: filter_data
Task: applies the filters using the data input
'''
        def filter_data(lst):
            # argument will contain the list of inputs
            # returns filtered dataframe
            
            cols_to_filter = ["category","Duration"] 
            # list of the filtrable columns - this can be implemented earlier in the code and it can be extended
            # this list has to match the 'filters' list
            
            filter_list = [] # we will save the filters here
            
            # iterating through each input
            for i in lst:
                if i != '':
                    filter_list.append(dataframe[cols_to_filter[i]] == lst[i])
            
            return dataframe.where(filter_list)


#---------------------------------------------------------------------------------------------------

            '''
            Function name: rentAnItem()
            Task: Lets the user rent an item
            '''
            def rentAnItem(self):


                chooseCategoryRent = input("Please choose the category of the item you want to rent:\n 1: measuring\n 2: shaping\n 3: fastening\n 4: mechanical\n 5: cutting\n")

                while chooseCategoryRent.isdigit() == False:
                    chooseCategoryRent = input("Please try again:\n")

                if chooseCategoryRent == 1 or 2 or 3 or 4 or 5:
                    	DatabaseConnection.CreateDBConnection()

                    cursor.execute('SELECT tool_name FROM Tools WHERE tool_cat= ?', chooseCategoryRent)
                    toolsListbyCategory = cursor.fetchall()
                    DatabaseConnection.CloseDBConnection()
                    print ("Please find the list of available items from selected category below:\n", toolsListbyCategory)
                        			
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

                chooseTool = input("Please enter the name of the tool you want to rent\n")

                Notes.Rent(tool_id)
                print ("Please be aware the item you chose might not be in perfect shape, please see notes below:\n", printNoteStateOfItem)

                lengthOfBookingInput = input("Please enter the length of your booking. You can book a tool for at least half a day (0.5) and not more than 3.0 days.\n")

                while lengthOfBookingInput == "":
                    lengthOfBookingInput = input("Please try again.")

                if lengthOfBookingInput != 0.5 or 1.0 or 1.5 or 2.0 or 2.5 or 3.0 or 1 or 2 or 3:
                    lengthOfBookingInput = input("This was an invalid entry. Please try again.")
                # Checks the availability of the tool 
                AvailabilityChecker.get_availability(tool_id, lengthOfBookingInput)

                dateOfBooking = input("Please find the availability below and type the start date of your choice. (YY-MM-DD)\n", days_available)

                while dateOfBooking == "":
                    dateOfBooking = input("Please try again.")

                if dateOfBooking != ??-??-??:
                    dateOfBooking = input("This was an invalid entry. Please try again.")

                
		        Delivery = input("We do offer delivery services should you not be able to collect the tool yourself. Would you be interested in ordering delivery for your tool (y/n)?.\n")

		        while Delivery == "":
                        Delivery = input("Please try again.")

                    if Delivery != 'y' or 'n':
                        Delivery = input("This was an invalid entry. Please try again.")
            
                if Delivery = 'y':
                    Delivery = 1
                else Delivery = 0
            
                AvailabilityChecker.book_out(tool_id, dateOfBooking, lengthOfBookingInput, Delivery)

#--------------------------------------------------------------------------------------------------------

if chooseAction == 3:
    			#inquireItemInput = input("Please choose between three different actions: 1: Details of the items you are renting\n 2: Details of the items that you uploaded\n 3: Item lost\n 4: Return item\n")

            #while inquireItemInput.isdigit() == False:
    		#	inquireItemInput = input("Please try again:\n")

            #if inquireItemInput == 1:
            #    #show list from DB of all the information of the details of the items that the person rented
            #    print("These are the items that you are renting at the moment:\n")

            #if inquireItemInput == 2:
            #    #show list of all the information of the details of the items that the person owns
            #    print("These are all the items that you uploaded to SharedPower:\n")

            #if inquireItemInput == 3:
            #    #connection to insurance
            #    print("You will be connected to the insurance")

            #if inquireItemInput == 4:
            #    bookingIdReturnInput = input("Please enter the booking ID of the item that you want to return")

            #    while bookingIdReturnInput.isdigit() == False:
    		#		bookingIdReturnInput = input("Please try again:\n")

                #check whether this ID is correct and is in the rented register of that person
                #check whether return is overdue
                #if overdue -> calculate extra fee
            bookingIdReturnInput = input("Please enter the booking ID of the item that you want to return")

            while bookingIdReturnInput.isdigit() == False:
                bookingIdReturnInput = input("Please try again:\n")

            LateCharge.checkIfLate(bookingIdReturnInput)

            noteOnReturn = input("Please describe any damage and/or wear and tear on the item")

            while noteOnReturn == "":
                noteOnReturn = input("If no damage or wear and tear please state 'perfect condition':\n")

            Notes.Return(noteOnReturn)

            
            
       
        if chooseAction == 4:
            
            def markAvailability():

                maToolInput = input("Please enter booking number for the report\n")

                while maToolInput.isdigit() == False:
                    maToolInput = input("Please try again:\n")

                Notes.Broken(maToolInput, brokenNoteInput)

                print ("Thank you your note has been saved and will be passed onto insurance company to start the claim.\n")

                


                #if state == unavailable:
                    #state.available
                #else:
                    #state.unavailable

        #  fuck this shit <3
        #  it is not one of the basic requirements








		#if chooseAction != 1 or 2 or 3:
