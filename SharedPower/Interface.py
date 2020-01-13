''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: Interface.py

Created: 17th November 2019

-------------------------------------------------
'''

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

		haveAccount = input("Welcome to SharedPower. \nDo you already have an account? 1: Yes or 2: No \n")

		while haveAccount.isdigit() == False:
    		haveAccount = input("Please try again:\n")

		if haveAccount == 1:
    			
			def signIn(self):
				
				print("Welcome...")
				welcome = input("Do you have an acount? y/n: ")
				if welcome == "n":
					while True:
						username  = input("Enter a username:")
						password  = input("Enter a password:")
						password1 = input("Confirm password:")
						if password == password1:
							file = open(username+".txt", "w")
							file.write(username+":"+password)
							file.close()
							welcome = "y"
							break
						print("Passwords do NOT match!")
				
				if welcome == "y":
					while True:
						login1 = input("Login:")
						login2 = input("Password:")
						file = open(login1+".txt", "r")
						data   = file.readline()
						file.close()
						if data == login1+":"+login2:
							print("Welcome")
							break
						print("Incorrect username or password.")



		if haveAccount == 2:
			
			def signUp(self):

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

				print("Please enter your bank details:\n")
				streetInputSU = input("Street name:\n")
				while streetInputSU == "":
						streetInputSU = input("Please try again:\n")

				streetNumberInputSU = input("Street number:\n")
				while streetNumberInputSU.isdigit() == False:
						streetNumberInputSU	= input("Please try again:\n")

				zipCodeInputSU = input("Zip Code:\n")
				while zipCodeInputSU == "":
						zipCodeInputSU = input("Please try again:\n")

				sortCodeInputSU = input("Sort Code:\n")
				while sortCodeInputSU.isdigit() == False:
						sortCodeInputSU = input("Please try again:\n")

				accountNumberInputSU = input("Account Number:\n")
				while accountNumberInputSU.isdigit() == False:
						accountNumberInputSU = input("Please try again:\n")

				emailInputSU = input("Last but not least, we need your email address for verification:\n")

				while emailInputSU == "":
					emailInputSU = input("Please try again:\n")
