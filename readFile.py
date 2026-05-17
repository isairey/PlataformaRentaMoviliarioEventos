def readFile():
    """This function read data from the Available_Stock.txt file and store it in a 2d list and return that list"""
    with open("Available_stock.txt") as file:
        listOfLine = []
        lines = file.readlines()
        for line in lines:
            listOfLine.append(line.replace("\n", "").split(","))
        return listOfLine


