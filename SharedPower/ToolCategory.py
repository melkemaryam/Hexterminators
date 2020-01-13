# --------------------------------------------------------------------
# Filename:     SessionTypeHelpers.py
#
# Date Created: 30th November 2019
# --------------------------------------------------------------------

import enum

class ToolCategorySpecify(enum.Enum): 
    Measuring  = 1
    Shaping = 2
    Fastening = 3
    Mechanical = 4
    Cutting = 5


class ToolCategory:

    '''
    Function name: getToolCatFromUser()
    Task: gets the input value of the tool category from the user
    '''
    @staticmethod
    def getToolCatFromUser():

            print("1. Measuring\n")
            print("2. Shaping\n")
            print("3. Fastening\n")
            print("4. Mechanical\n")
            print("5. Cutting\n")

            chooseCategory = input("Please choose the category of the tool from the list above:")

            while (chooseCategory.isdigit() == False):
                chooseCategory = input('Please only enter numbers:')

            chooseCategory = int(chooseCategory)

            toolCategory = ToolCategorySpecify(chooseCategory)

            return toolCategory
