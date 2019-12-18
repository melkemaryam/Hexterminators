class Interface:

	def checkAccount():

		haveAccount = input("Welcome to SharedPower. \nDo you already haven an account? 1: Yes or 0: No \n")

		if haveAccount == 1:
			# check wether username already exists in the database
			usernameInputSI = raw_input("Please enter your username:\n")

			while usernameInputSI == "":
				usernameInputSI = raw_input("Please try again and enter your username:\n")
				
			passwordInputSI = raw_input("Please enter the password:\n")	
			# check wether password is correct in the database
				
			while passwordInputSI == "":
				passwordInputSI = raw_input("Please try again:\n")

			#if passwordInputSI != passwordInputSU:
			#	forgotPassword = input("Did you forget your password? 1:Yes or 0:No\n")
			#
			#	if forgotPassword == 1:
					#-> reset password in DB
			#		usernameInputSU = raw_input("Please enter a new password\n")
					#save new passord in the DB

			#	else:
			#	 	passwordInputSI = raw_input("Please enter the password\n")



		if haveAccount == 0:
			# check availability of the username

			#while usernameInputSU is already in Database:
			usernameInputSU = raw_input("Please sign up here.\nPlease come up with an unique username:\n")

			while usernameInputSU == "":
				usernameInputSU = raw_input("Please try again:\n")
				
			#if usernameInputSU == already in Database:

			passwordInputSU = raw_input("Please enter a safe password:\n")

			while passwordInputSU == "":
				passwordInputSU = raw_input("Please try again:\n")
				
			#save password in Database with username

			firstNameInputSU = raw_input("Please enter your first name:\n")

			while firstNameInputSU == "":
				firstNameInputSU = raw_input("Please try again:\n")

			#save in DB

			lastNameInputSU = raw_input("Please enter your last name:\n")

			while lastNameInputSU == "":
				lastNameInputSU = raw_input("Please try again:\n")

			#save in DB

			bankDetailsInputSU = raw_input("Please enter your bank details:\n")

			while bankDetailsInputSU == "":
				bankDetailsInputSU = raw_input("Please try again:\n")

			#add several different bank details and add to the DB

			emailInputSU = raw_input("Last but not least, we need your email address for verification:\n")

			while emailInputSU == "":
				emailInputSU = raw_input("Please try again:\n")

			#create complete account in DB and send a verification email

	#if haveAccount != 1 or 0:
		#account()



	#load DB

	def action():
		
		chooseAction = input("Please choose what you want to do next:\n 1: Add a new item\n 2: Rent an item\n 3: Inquire an item\n")

		if chooseAction == 1:


			#tools that enact chemical changes, including temperature and ignition, such as lighters and blowtorches.
			#Guiding, measuring and perception tools include the ruler, glasses, set square, sensors, straightedge, theodolite, microscope, monitor, clock, phone, printer
			#Shaping tools, such as molds, jigs, trowels.
			#Fastening tools, such as welders, rivet guns, nail guns, or glue guns.
			#Wikipedia: https://en.wikipedia.org/wiki/Tool#Tool_substitution 1.12.2019 3:08 am

			chooseCategoryAdd = input("Please choose the category of the item that you want to add:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")

			#save all the data in the DB with assigned toolId
			toolName = raw_input("Please enter the full name of your tool:")
			typeName = raw_input("Please enter the type of the item:")
			descriptionTool = raw_input("Please enter a short description that also displays the condition and size of your tool:")
			dayPriceTool = float(input("Please enter the price in Pounds for a day rent"))
			halfDayPriceTool = float(input("Please enter the price in Pounds for half a day"))
			#availabilityTool = date

			#after setting all up -> mark availibilty

			photoUploadTool = input("Do you want to upload a photo of your tool? 1: Yes or 2: No") 
			if photoUploadTool == 1: 
				#upload photo aus desktop folder

			#print("Thank you verry much. Your new tool has been added to our Database.")

		if chooseAction == 2:
    		chooseCategoryRent = input("Please choose the category of your item:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")
			if chooseCategory == 1:
				#list of all the measuring tools in the DB plus amount of pieces of each tool
				chooseTool = raw_input("Please enter the name of the tool you want to rent\n")


			if chooseCategory == 2:
				#list of all the shaping tools in the DB plus amount of pieces of each tool
				chooseTool = raw_input("Please enter the name of the tool you want to rent\n")

			if chooseCategory == 3:
				#list of all the fastening tools in the DB plus amount of pieces of each tool
				chooseTool = raw_input("Please enter the name of the tool you want to rent\n")

			if chooseCategory == 4:
				#list of all the mechanical tools in the DB plus amount of pieces of each tool
				chooseTool = raw_input("Please enter the name of the tool you want to rent\n")

			if chooseCategory != 1 or 2 or 3 or 4:
				chooseCategoryRent = input("Your Input was invalid. Please try to enter it again and choose the category of your item:\n 1: measuring\n 2: shaping\n 3: fastening\n 4:mechanical\n")



			lengthOfBookingInput = input("Please enter the length of your booking. You can book a tool for at least half a day (0.5) and not more than 3.0 days.\n")

			while lengthOfBookingInput == "":
				lengthOfBookingInput = input("Please try again.")

			if lengthOfBookingInput != 0.5 or 1.0 or 1.5 or 2.0 or 2.5 or 3.0 or 1 or 2 or 3:
				lengthOfBookingInput = input("This was an invalid entry. Please try again.")

		if chooseAction == 3:
			inquireItem = input("Please choose between three different action")




		#if chooseAction != 1 or 2 or 3: