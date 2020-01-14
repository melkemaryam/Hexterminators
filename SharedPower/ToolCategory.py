''' 
-------------------------------------------------

Project: SharedPower
Group: Hexterminators

File name: ToolCategory.py

Created: 17th November 2019

-------------------------------------------------
'''

#tools that enact chemical changes, including temperature and ignition, such as lighters and blowtorches.
#Guiding, measuring and perception tools include the ruler, glasses, set square, sensors, straightedge, theodolite, microscope, monitor, clock, phone, printer
#Shaping tools, such as molds, jigs, trowels.
#Fastening tools, such as welders, rivet guns, nail guns, or glue guns.
#Wikipedia: https://en.wikipedia.org/wiki/Tool#Tool_substitution 1.12.2019 3:08 am
		
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
