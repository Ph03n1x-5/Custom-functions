# Function to create an external file to write output
def createOutputFile():
    fileName = input("Enter the file name where your output will be written\n")
    outFile = open(fileName + ".txt", "w")
    return fileName, outFile
    # end createOutputFile function
#------------------------------------------------------------------------------

def getData(weeklyGasExpense.txt):
    for i in range(0,n,1):
        print("What is the outdoor temperature in the state of " + state + " on day number " + format(i + 1, "2d") + " : ")
        wTemp[i] = checkFloatDataType()
#------------------------------------------------------------------------------       
    
def writeList(n,wTemp,outFile) :
    for i in range(0,n-1+1,1) :
        outFile.write(format("wTemp["+format(i+1,"2d")+"] = "+format(wTemp[i],"6.2f")+"°","^65s")+"\n")
        # end for loop
        # end write list function
#------------------------------------------------------------------------------

def calculateAverage(wTemp) :
    average = sum(wTemp) / len(wTemp)
    return average
#------------------------------------------------------------------------------

def writeStats(wTemp, average, outFile) :
    outFile.write(("The minimum Temperature = " + format(min(wTemp), "6.2f") + "°").center(60) + "\n")
    outFile.write(("The maximum Temperature = " + format(max(wTemp), "6.2f") + "°").center(60) + "\n")
    outFile.write(("The average Temperature = " + format(average, "6.2f") + "°").center(60) + "\n")
#------------------------------------------------------------------------------

def findGasExpenseLessThan35(n, wGas, gGas, gCount):
    gCount = 0
    for i in range(0, n, 1):
        if wGas[i] <= 35:
            gGas[i] = wGas[i]
            gCount = gCount + 1
            # end IF statement
        # end FOR loop
    return gCount
#------------------------------------------------------------------------------

def writeGasExpenseBetween35And50(n, gGas, gCount, outFile):
    outFile.write("="*60 + "\n")
    for i in range(0, n, 1):
        if gGas[i] > 35 and <= 50:
            outFile.write(format("gGas["+format(i+1,"2d")+"] = "+format(gGas[i],"6.2f")+"°","^65s")+"\n")
        # end IF statement
    outFile.write("="*60 + "\n")
    # end FOR loop
#------------------------------------------------------------------------------        
def writeGasExpenseGreaterThan35():
    for i in range(0, n, 1):
        if gGas[i] > 50 and <= 95:


    outFile.write(("TEMPERATURE(S) GREATER THAN OR EQUAL TO 75° OCCUR(S) " + format(gCount, ",d") + " TIME(S).").center(60) + "\n")
#------------------------------------------------------------------------------

def read_File(name):
    data = []
    try:
        f = open(name, 'r')
        data = f.read().replace(',"").rstrip('\n').split('\n')
        f.close()
        except IOError:
            print("File not found")

        for i in range(len(data)):
            data[i] = int(data[i])
        return data
#------------------------------------------------------------------------------

def count_gas_1(data):
    list and count gasexpense > 35 and <= 50 task 6
    _list = []
    count = 0
    for i in data:
        if (i > 35 and i <= 50):
            list.append(i)
            count += 1
#-------------------------------------------------------------------------------

def count_gas_2(data):
    list and count gasexpense > 50 and <= 95 task 7
    _list = []
    count = 0
    for i in data:
        if (i > 50 and i <= 95):
            list.append(i)
            count += 1
#-------------------------------------------------------------------------------

def task8(data):
    print(data)
    print("minnimum = {}, and average = {} gas."format(min(data),max(data),(sum(data)/len(data))))

    a = []
    for i in data:
        a.append(i)
    print("gas expense >= 95 are {}."format(a))
#------------------------------------------------------------------------------

def gas_exp1(data):

    list and count gasexpense <= 35 task f

_list = []
for i in data:
    if (i <= 35):
        _list.append(i)
    return sum(_list)
#-------------------------------------------------------------------------------

def gas_gas_exp2(data):

    list and count gasexpense <= task f
    _list = []
    for i in data:
       if (i < 35):
           _list.append(i)
        return sum(_list)
#-------------------------------------------------------------------------------

def gas_exp3(data):
    list and count gasexpense > 35 and <= 50 task g
    _list = []
    for i in data:
        if (i > 35 and i < 50):
            _list.append(i)
        return sum(_list)
#-------------------------------------------------------------------------------

def gas_exp3(data):
    list and count gasexpense > 50 and < 95 task h
    _list = []
    for i data:
        if (i > 50 and i < 95):
            _list.append(i)
        return sum(_list)
#-------------------------------------------------------------------------------

    
    
    
