# Importing necessary imports
from datetime import datetime
from readFile import readFile

formatted_date_time = datetime.now().strftime("%Y-%m-%d")


def mainMenuMessage():
    """This function display the main menu option which contain company name in
     header and 4 available menu options in body"""
    print("__________________________________________________________")
    print("|                 HAMRO RENTAL SHOP NEPAL                |")
    print("|                Your Function, Our Rentals              |")
    print("|                     Kathmandu, Nepal                   |")
    print("|                                       Date:" + formatted_date_time + "  |")
    print("|--------------------------------------------------------|")
    print("|                                                        |")
    print("|                       MENU OPTIONS                     |")
    print("|                                                        |")
    print("|              (Enter-1) To Display Items                |")
    print("|              (Enter-2) To Rent our Items               |")
    print("|              (Enter-3) To Return  Items                |")
    print("|              (Enter-4) To Exit to Home                 |")
    print("|                                                        |")
    print("|                                                        |")
    print("|--------------------------------------------------------|")


def menuOptions():
    """This function displays the 4 available menu options"""
    print("MENU OPTIONS")
    print("(Enter-2) To Rent our Items")
    print("(Enter-3) To Return  Items")
    print("(Enter-4) To Exit to Home\n")


def showAvailableStock():
    """This function displays all the stock details like item id, name, quantity, brand name and price """
    print("\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("                                          LIST OF AVAILABLE ITEM IN OUR STOCK                                      ")
    print("-------------------------------------------------------------------------------------------------------------------\n")
    print("Item ID \t Item Name \t\t\t Brand Name \t\t\t Price \t\t Available Quantity")
    print("-------------------------------------------------------------------------------------------------------------------")
    for i in range(len(readFile())):
        print(readFile()[i][0] + "\t\t " + readFile()[i][1] + "\t " + readFile()[i][2] + "\t\t $" +
              readFile()[i][3] + "\t\t\t" + readFile()[i][4])
    print("\n")


def showItemNameAndID():
    """This function display list of all the available items and its ID"""
    print("\nItem ID \t Item Name")
    print("------------------------------------------------")
    for i in range(len(readFile())):
        print(readFile()[i][0] + "\t\t " + readFile()[i][1])
    print("\n")


def rentTitle():
    """This method display welcome message for customer who is renting items"""
    print("\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("                      WELCOME! YOU'RE ABOUT TO RENT OUR PRODUCT. HAVE A GOOD TIME WITH US :)                       ")
    print("-------------------------------------------------------------------------------------------------------------------\n")


def returnTitle():
    """This method display welcome message for customer who is returning items"""
    print("\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("                      WELCOME! YOU'RE ABOUT TO RETURN OUR PRODUCT. HAVE A GOOD TIME WITH US :)                     ")
    print("-------------------------------------------------------------------------------------------------------------------\n")


def thankYouMessage():
    """This method display thankyou message for customer"""
    print("\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("                        THANK YOU! FOR CHOOSING HAMRO RENTAL NEPAL. SEE YOU SOON AGAIN :)                          ")
    print("-------------------------------------------------------------------------------------------------------------------\n")


