# Importing necessary imports
from readFile import readFile

def askName():
    """This function takes valid input for Customer name. If any invalid input name is provided,
     it display error message and takes input again"""
    while True:
        name = input("Enter your Full Name to proceed: ")
        if name == "":
            print("Name is mandatory! Please make sure to enter you name.")
        elif name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid name entered! Please choose letters from A-Z only.")
    return name


def askItemId():
    """This function takes valid input for Item ID. If any invalid input name is provided,
         it display error message and takes input again"""
    while True:
        try:
            itemId = int(input("Enter the Item-ID corresponding of Item Name: "))
            if 1 <= itemId <= len(readFile()):
                break
            else:
                print("Invalid ID found. Please enter value between (1-10) only")
        except:
            print("Invalid input found. Please choose option between (1-10) only.")
    return itemId
