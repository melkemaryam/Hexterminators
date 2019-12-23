import sqlite3
import pandas as pd

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


    def __init2__(self, chooseAction, chooseCategoryAdd, toolName, typeName, descriptionTool, dayPriceTool, halfDayPriceTool, availabilityTool, photoUploadTool, chooseCategoryRent, chooseTool, lengthOfBookingInput, inquireItem):
    	self.chooseAction = chooseAction
        self.chooseCategoryAdd = chooseCategoryAdd
		self.toolName = toolName
		self.typeName = typeName
		self.descriptionTool = descriptionTool
		self.dayPriceTool = dayPriceTool
		self.halfDayPriceTool = halfDayPriceTool
		self.availabilityTool = availabilityTool
		self.photoUploadTool = photoUploadTool
		self.chooseCategoryRent = chooseCategoryRent
		self.chooseTool = chooseTool
		self.lengthOfBookingInput = lengthOfBookingInput
		self.inquireItem = inquireItem


	#load DB

	def action(self):
		
		chooseAction = input("Please choose what you want to do next:\n 1: Add a new item\n 2: Rent an item\n 3: Inquire an item\n 4: Mark availability of one of your items\n")

		if chooseAction == 1:


			#tools that enact chemical changes, including temperature and ignition, such as lighters and blowtorches.
			#Guiding, measuring and perception tools include the ruler, glasses, set square, sensors, straightedge, theodolite, microscope, monitor, clock, phone, printer
			#Shaping tools, such as molds, jigs, trowels.
			#Fastening tools, such as welders, rivet guns, nail guns, or glue guns.
			#Wikipedia: https://en.wikipedia.org/wiki/Tool#Tool_substitution 1.12.2019 3:08 am

			chooseCategoryAdd = input("Please choose the category of the item that you want to add:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")

			#save all the data in the DB with assigned toolId
			toolName = input("Please enter the full name of your tool:\n")
			typeName = input("Please enter the type of the item:\n")
			descriptionTool = input("Please enter a short description that also displays the condition and size of your tool:\n")
			dayPriceTool = float(input("Please enter the price in Pounds for a day rent\n"))
			halfDayPriceTool = float(input("Please enter the price in Pounds for half a day\n"))
			availabilityTool = input("Please enter the start and the end date of the availability of this particular tool: dd.mm.yyyy - dd.mm.yyyy\n")

			#after setting all up -> mark availibilty

			photoUploadTool = input("Do you want to upload a photo of your tool? 1: Yes or 0: No") 
			if photoUploadTool == 1: 
				#upload photo from desktop folder
				print("Thank you very much. Your new tool with the photo has been added to our Database.")
			else:
				print("Thank you very much. Your new tool has been added to our Database.")

		if chooseAction == 2:
    			
			chooseCategoryRent = input("Please choose the category of your item:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")
			if chooseCategoryRent == 1:
				#list of all the measuring tools in the DB plus amount of pieces of each tool
				chooseTool = input("Please enter the name of the tool you want to rent\n")


			if chooseCategoryRent == 2:
				#list of all the shaping tools in the DB plus amount of pieces of each tool
				chooseTool = input("Please enter the name of the tool you want to rent\n")

			if chooseCategoryRent == 3:
				#list of all the fastening tools in the DB plus amount of pieces of each tool
				chooseTool = input("Please enter the name of the tool you want to rent\n")

			if chooseCategoryRent == 4:
				#list of all the mechanical tools in the DB plus amount of pieces of each tool
				chooseTool = input("Please enter the name of the tool you want to rent\n")

			if chooseCategoryRent != 1 or 2 or 3 or 4:
				chooseCategoryRent = input("Your Input was invalid. Please try to enter it again and choose the category of your item:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")



			lengthOfBookingInput = input("Please enter the length of your booking. You can book a tool for at least half a day (0.5) and not more than 3.0 days.\n")

			while lengthOfBookingInput == "":
				lengthOfBookingInput = input("Please try again.")

			if lengthOfBookingInput != 0.5 or 1.0 or 1.5 or 2.0 or 2.5 or 3.0 or 1 or 2 or 3:
				lengthOfBookingInput = input("This was an invalid entry. Please try again.")

		if chooseAction == 3:
			inquireItem = input("Please choose between three different actions")




		#if chooseAction != 1 or 2 or 3: