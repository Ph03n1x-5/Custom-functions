# importing the os path libary
import os

# declaring empty lists
gasExpenses35 = []
gasExpenses35And50 = []
gasExpenses50And95 = []
unsortedGasPrices = []
sortedGasPrices = []

# function to create an external file to write output
def createOutputFile():
    fileName = input("Enter the file name where your output will be written\n")
    outFile = open(fileName + ".txt", "w")
    return fileName, outFile

# read file data containing gas list
def readData(externalFile):
    # initialize a lists
    gas_list = []
    prices = []
    # read from txt file containing data
    with open(externalFile) as f:
        prices= f.readlines()

        # convert the gas exppenses fro string to float
    for price in prices:
        gas_list.append(float(price))
    
    #return the float value of expenses
    return gas_list


# function to check if file exists
def fileExists(externalFile):
    try:
        open(externalFile).readlines()
        return True
    except FileNotFoundError:
        print("File not found")
        return False
    

# function to check the data type of the data
def checkDataType(price):
    # check if data is a float or of int type
    if type(price) == float :
        return True
        # check if value is non-negative
    elif (price < 0):
        print("Negative Price Value")
        return False
    else:
        print("Wrong Data Type")
        return False

 # write gas expenses <= 35 
def writeGas35(gas_list):
    # loop over list
    for gas in gas_list:
        # check for gas <= 35
        if(gas <= 35):
            # append  value to g_list
            gasExpenses35.append(gas)
    return(gasExpenses35)


# write gas expenses > 35 and <= 50
def writeGas35and50(gas_list):
    for gas in gas_list:
        if gas > 35.00 and gas <= 50.00:
            #append the values to a list
            gasExpenses35And50.append(gas)
    return(gasExpenses35And50)


# write gas expenses > 50 and <= 95
def writeGas50and95(gas_list):
    for gas in gas_list:
        if gas > 50.00 and gas <= 95.00:
            # append gas prices to a list
            gasExpenses50And95.append(gas)
    return(gasExpenses50And95)


 returns a report of values that are less than or equal to 35
def gasReport35(gas_list):
    return len(gasExpenses35(gas_list))

 returns a report of values greater than 35 and less than or equal to 50
def gasReport35And50(gas_list):
    return len(gasExpenses35And50(gas_list))

 returns a report of values greater than 50 and less than or equal to 95
def gasReport50And95(gas_list):
    return len(gasExpenses50And95(gas_list))

