import sqlite3

class Interface:
    	
	def __init1__(self,usernameInputSI, usernameInputSU, passwordInputSI, passwordInputSU, firstNameInputSU, lastNameInputSU, streetInputSU, streetNumberInputSU, zipCodeInputSU, sortCodeInputSU, accountNumberInputSU, emailInputSU):
		self.usernameInputSI = usernameInputSI
		self.usernameInputSU = usernameInputSU
		self.passwordInputSI = passwordInputSI
		self.passwordInputSU = passwordInputSU
		self.firstNameInputSU = firstNameInputSU
		self.lastNameInputSU = lastNameInputSU
		self.streetInputSU = streetInputSU
		self.streetNumberInputSU = streetNumberInputSU
		self.zipCodeInputSU = zipCodeInputSU
		self.sortCodeInputSU = sortCodeInputSU
		self.accountNumberInputSU = accountNumberInputSU
		self.emailInputSU = emailInputSU

	
	def checkAccount(self):

		haveAccount = input("Welcome to SharedPower. \nDo you already have an account? 1: Yes or 0: No \n")

		if haveAccount == 1:
    			
			def signIn(self):
				# check wether username already exists in the database
				usernameInputSI = input("Please enter your username:\n")

				while usernameInputSI == "":
					usernameInputSI = input("Please try again and enter your username:\n")
					
				passwordInputSI = input("Please enter the password:\n")	
				# check wether password is correct in the database
					
				while passwordInputSI == "":
					passwordInputSI = input("Please try again:\n")

				#if passwordInputSI != passwordInputSU:
				#	forgotPassword = input("Did you forget your password? 1:Yes or 0:No\n")
				#
				#	if forgotPassword == 1:
						#-> reset password in DB
				#		usernameInputSU = input("Please enter a new password\n")
						#save new passord in the DB

				#	else:
				#	 	passwordInputSI = input("Please enter the password\n")



		if haveAccount == 0:
			
			def signUp(self):
				# check availability of the username

				#while usernameInputSU is already in Database:
				usernameInputSU = input("Please sign up here.\nPlease come up with an unique username:\n")

				while usernameInputSU == "":
					usernameInputSU = input("Please try again:\n")
					
				#if usernameInputSU == already in Database:
				#	usernameInputSU = input("Please try again:\n")

				passwordInputSU = input("Please enter a safe password:\n")

				while passwordInputSU == "":
					passwordInputSU = input("Please try again:\n")
					
				#save password in Database with username

				firstNameInputSU = input("Please enter your first name:\n")

				while firstNameInputSU == "":
					firstNameInputSU = input("Please try again:\n")

				#save in DB

				lastNameInputSU = input("Please enter your last name:\n")

				while lastNameInputSU == "":
					lastNameInputSU = input("Please try again:\n")

				#save in DB

				print("Please enter your bank details:\n")
				streetInputSU = input("Street name:\n")
				while streetInputSU == "":
						streetInputSU = input("Please try again:\n")

				streetNumberInputSU = input("Street number:\n")
				while streetNumberInputSU == "":
						streetNumberInputSU	= input("Please try again:\n")

				zipCodeInputSU = input("Zip Code:\n")
				while zipCodeInputSU == "":
						zipCodeInputSU = input("Please try again:\n")

				sortCodeInputSU = input("Sort Code:\n")
				while sortCodeInputSU == "":
						sortCodeInputSU = input("Please try again:\n")

				accountNumberInputSU = input("Account Number:\n")
				while accountNumberInputSU == "":
						accountNumberInputSU = input("Please try again:\n")

				#add several different bank details and add to the DB
				#bank details: Street, number, Zipcode, Sort code, account number

				emailInputSU = input("Last but not least, we need your email address for verification:\n")

				while emailInputSU == "":
					emailInputSU = input("Please try again:\n")

				#create complete account in DB (and send a verification email)

		if haveAccount != 1 or 0:
			self.checkAccount()