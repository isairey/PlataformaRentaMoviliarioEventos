# Importing necessary imports
from displayMessage import *
import datetime
from validate import *

dateTime = datetime.datetime.now().strftime("%c")


def returnItem():
    """ This function enables user to retun item to the shop. It takes all the necessary inputs from the user like
    name, item id, item quantity, rental duration and generates the invoice. It also charge fine for late return and updates the stock file accordingly"""

    success = True  # Main loop
    returnItemId = []  # Initializing empty list to store return details
    returnItemQty = []
    fullName = askName()  # Calling method that take username input
    showItemNameAndID()  # Prints Item name and ID
    # Importing and string second & Millisecond (Used for creating unique filename)
    s = str(datetime.datetime.now().second)
    mi = str(datetime.datetime.now().microsecond)
    fileName = "Return_" + fullName + "_" + s + mi + ".txt"  # Creating unique filename for customers

    while success:

        itemId = askItemId()  # Call method that asks for ItemId from the user
        while True:
            try:
                rentQty = int(input("Please input the quantity of the rented item: "))
                if rentQty > 0:
                    break
                else:
                    print("The item must be greater than zero.")
            except:
                print("Invalid value entered. Please select choices from 1 to 10 only.")

        # Add datas to list
        returnItemId.append(itemId)
        returnItemQty.append(rentQty)
        print("Return request has been added!")

        while True:
            # Asking user if they want to return more or stop
            rentMore = input("Would you like to return more items? Input 'y' for YES and 'n' for NO:").lower()
            # Condition if invalid input is found
            if rentMore != "y" and rentMore != 'n':
                print("Incorrect input found. Please provide either 'y' or 'n': ")
            elif rentMore == "y":
                # Condition if user want to return more
                break
            # Condition if user want to stop
            elif rentMore == "n":
                # Asking user How many days did they rented the item.
                while True:
                    try:
                        rentDays = int(input("How much days did you rent this item for?"))
                        if rentDays > 0:
                            break
                        else:
                            print("Invalid Input. Renting days can't be Zero or less.")
                    except:
                        print("Please enter integer value only.")

                with open(fileName, "w") as returnFile:
                    # Create and wite in the Invoice file
                    returnFile.write(
                        "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                        "                         HAMRO RENTAL SHOP NEPAL (Return Bill)                         \n"
                        "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    returnFile.write("\nReturned By: " + fullName + "\n")
                    returnFile.write("Date: " + dateTime + "\n\n")
                    returnFile.write(
                        "Item Name \t\t     Brand Name \t\t Rented Quantity \t Price\n")


                with open(fileName, 'a') as file:
                    totalPrice = 0
                    stockData = readFile()
                    # Loop for writing Returned item details
                    for i in range(len(returnItemId)):
                        returnItemName = str(stockData[returnItemId[i] - 1][1])
                        returnItemIdIndex = returnItemId[i] - 1
                        returnItemQuantity = returnItemQty[i]
                        returnItemBrand = stockData[returnItemIdIndex][2]
                        returnItemPrice = returnItemQuantity * int(stockData[returnItemIdIndex][3])
                        # Increasing the stock when item is returned by customer
                        stockData[returnItemIdIndex][4] = str(int(stockData[returnItemIdIndex][4]) + returnItemQuantity)
                        totalPrice += returnItemPrice  # Sum-up total cost
                        # Writing inside txt file
                        file.write(
                            returnItemName + " " + returnItemBrand + "\t\t\t" + str(returnItemQuantity) + "\t\t $" + str(
                                returnItemPrice) + "\n")


                    # For calculating fine
                    i = rentDays/5
                    if i < 1:
                        charge = 0
                    else:
                        i = int(i)
                        charge = int(i*(0.1*totalPrice))

                    file.write(
                        "\n----------------------------------------------------------------------------------------"
                        "\n \t\t\t\t\t\t\t\t Renting Charge: $" + str(totalPrice) +
                        "\n \t\t\t\t\t\t\t\t           Fine: $" + str(charge) +
                        "\n \t\t\t\t\t\t\t\t          Total: $" + str(totalPrice+charge) +
                        "\n----------------------------------------------------------------------------------------")
                    
                # Printing invoice on terminal
                with open(fileName, 'r') as file:
                    content = file.read()
                    print(content)

                # Updating txt file of stock
                with open("Available_stock.txt", 'w') as stockFile:
                    for i in range(len(stockData)):  # Iterate over the entire stockData length
                        stockFile.write(
                            stockData[i][0] + "," + stockData[i][1] + "," + stockData[i][2] + "," +
                            stockData[i][3] + "," + stockData[i][4] + "\n")

                success = False
                break