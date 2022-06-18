# import statistics to calculate average
from statistics import mean

# function definitions
# 1. create file function
def createOutputFile():
    file = open("lastname_firstname_A15_GAS_EXPENSES_output.txt", "w+")
#-----------------------------------------------------------------------------
# 2. size of list data type check

def checkIntDataType(gas_list):
    # size of the list
    size = len(gas_list)
    if type(size) is int:
        print("Data type of size of the list is 'Int'\n")
        else:
            print("Wrong data!")

# 3. temp data type check
def checkFloatDataType(gas):
    # data type of temp check
    if type(gas) is float:
        return True
    else:
        return False
    
# 4. read file data
def readData():
    # initialize a list
    gas_list = []
    # read lines
    for line in f.readlines():
        # stote in a list
        gas_list.append(line)
    return gas_list

# 5. write into file
def writeResults(gas_list):
    # loop over list
    for gas in gas_list:
        f.write(f"{gas.2f}\n")

# 6. average gas function
def calculateAvg(gas_list):
    # average = mean(gas_list)
    average = mean(gas_list)
    return average

# 7. write gas expenses <= 35 into file
def writeGas35(gas_list):
    # declare a list
    g_list = []
    # loop over list
    for gas in gas_list:
        # check for gas <= 35
            # write the number of gas expenses <= 35
            f.write(f"\nNumber of gas expeneses less than or equal to 35.00 is :{len(g_list)}\n")
            # call writeResults funtion to write results into file
            writeResults(g_list)
            # extra function added to write stat_list elements as its repetitive tasks
            # write min, max and average list into file

# write gas expenses > 35 and <= 50
def writeGas35and50:
    average = means(gas_list):
        g_list = []
        for gas in gas_list:
            if gas < 35.00 and <= 50.00
            f.write(f"\nNumber of gas expenses greater than 35.00 AND less than and equal to 95.00 is :{len(g_list)}\n")
            writeResults(g_list)

# write gas expenses > 50 and <= 95
def writeGas50and95:
    average = mean(gas_list):
        for gas in gas_list:
            if gas > 50.00 and <= 95.00
            f.write(f"\nNumber of gas expenses greater than 50.00 AND less than and equal to 95.00 is :{len(g_list)}\n")
            writeResults(g_list)
        
            
def writeStats(stat_list):
    # write stat_list elements into file
    file.write(f"\nThe minimum Gas Expenses in the list is {stat_list[0]:.2f}\n")
    file.write(f"\nThe maximum Gas Expenses in the list is {stat_list[1]:.2f}\n")
    file.write(f"\nThe average Gas Expenses in the list is {stat_list[2]:.2f}\n")
    # close file
    file.close()

# END PROGRAM
                










