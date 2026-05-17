# Importing necessary imports
from displayMessage import *
import datetime
from validate import *

dateTime = datetime.datetime.now().strftime("%c")

def rentItem():
    """ This function enables user to rent item from the shop. It takes all the necessary inputs from the user like
       name, item id, item quantity and generates the invoice. It also updates the stock file accordingly"""

    success = True  # For main loop
    purchasedItem_ID = []  # Initializing empty list to store rent details
    purchasedItem_Qty = []
    # Loop for checking username input
    fullName = askName()
    showAvailableStock()  # Prints list of available stock
    # Importing and string second & Millisecond (Used for creating unique filename)
    s = str(datetime.datetime.now().second)
    mi = str(datetime.datetime.now().microsecond)
    fileName = "Rent_" + fullName + "_" + s + mi + ".txt"  # Creating unique filename for customers

    while success:  # False only when the bill is generated, printed and Stored in txt file successfully
        try:
            itemChoice = askItemId()  # Call method that asks for ItemId from the user
            # Checking validity of itemChoice
            if 1 <= itemChoice <= len(readFile()):
                availableQuantity = int(readFile()[itemChoice - 1][4])  # Storing the available quantity
                while True:
                    try:
                        itemQuantity = int(input("How much quantity would you like to rent: "))  # Asking for quantity to rent
                        if itemQuantity > availableQuantity:
                            print("Sorry, item out of stock. Please rent a smaller quantity.")
                        elif itemQuantity <= 0:
                            print("The item must be greater than zero.")
                        else:
                            break
                    except:
                        print("Alphabets are not accepted. Please provide an integer value only.")

                if itemQuantity <= availableQuantity:
                    purchasedItem_ID.append(itemChoice)  # Appending rent data to list
                    purchasedItem_Qty.append(itemQuantity)
                    print("Item successfully added to the cart!")

                    while True:
                        rentMore = input("Would you like to rent more items? Please input 'y' for YES and 'n' for NO:").lower()
                        if rentMore != "y" and rentMore != 'n':
                            print("Invalid input found. Please enter either 'y' or 'n': ")
                        elif rentMore == "y":
                            break
                        elif rentMore == "n":
                            # Creating and opening txt file with unique name for storing rent data
                            with open(fileName, "w") as rentFile:
                                # Writing Title, Customer name & Date to txt file
                                rentFile.write(
                                    "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                    "                           HAMRO RENTAL SHOP NEPAL (Rent Bill)                         \n"
                                    "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                                rentFile.write("\nBorrowed By: " + fullName + "\n")
                                rentFile.write("Date: " + dateTime + "\n\n")

                            with open(fileName, 'a') as file:
                                totalPrice = 0  # Initialize totalPrice
                                file.write(
                                    "Item Name \t\t     Brand Name \t\t Rented Quantity \t Price\n")

                                # Writing invoice (Bill) in a txt file and printing on console at same time
                                stockData = readFile()  # Store the stock data list from readFile() in a variable
                                for i in range(len(purchasedItem_ID)):
                                    # Storing necessary value in a variable
                                    itemName = str(stockData[purchasedItem_ID[i] - 1][1])
                                    itemIdIndex = purchasedItem_ID[i] - 1
                                    itemQty = purchasedItem_Qty[i]
                                    itemBrand = str(stockData[itemIdIndex][2])
                                    itemPrice = itemQty * int(stockData[itemIdIndex][3])
                                    # Decreasing the stock when item is rented by customer
                                    stockData[itemIdIndex][4] = str(int(stockData[itemIdIndex][4]) - itemQty)
                                    totalPrice += itemPrice  # Sum-up total cost
                                    # Writing inside txt file
                                    file.write(
                                        itemName + " " + itemBrand + "\t\t\t" + str(itemQty) + "\t\t $" + str(
                                            itemPrice) + "\n")

                                file.write(
                                    "\n----------------------------------------------------------------------------------------"
                                    "\n \t\t\t\t\t\t\t\t Total Amount: $" + str(totalPrice) +
                                    "\n----------------------------------------------------------------------------------------")

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

        except:
            print("Something went wrong! Please ensure you enter only numerical values in the required field.")
