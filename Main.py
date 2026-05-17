# Importing necessary imports
from Rent import *
from Return import *


def main():
    """ This is the main function of this system which combine all the modules at a place. This prints a main menu
    and ask user to input what feature they want to use by calling the necessary functions. """

    # Main Loop
    success = True
    while success:
        mainMenuMessage()  # Prints company Name and Location
        while True:
            try:
                userInput = int(input("Enter your value to proceed: "))  # Asks for user input
                if 0 < userInput < 5:
                    if userInput == 1:
                        showAvailableStock()  # Calling methods from displayMessage module
                        menuOptions()
                else:
                    print("Invalid input provided. Please enter valid choice from 1-4 only: ")

                if userInput == 2:
                    rentTitle()  # Calling method from displayMessage module
                    rentItem()  # Calling method from Rent module
                    break

                if userInput == 3:
                    returnTitle()  # Calling method from displayMessage module
                    returnItem()  # Calling method from Renturn module
                    break

                if userInput == 4:
                    thankYouMessage()  # Calling method from displayMessage module
                    success = False  # Breaks the main loop
                    break

            except:
                print("Invalid input found! Please choose option between (1-4) only.")


# Calling this function to start the program
main()
