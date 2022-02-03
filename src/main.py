import sys, time, os, json
from statistics import mean
from decimal import *

getcontext().prec = 17 #sets decimal place for Decimal type values so program can accurately round to 16 decimal places

def function1(X: list, m: Decimal, c: Decimal) -> list:
    '''

    '''
    try:
        #Checks if data types of arguments passed in are correct
        if type(X) != list: raise TypeError("Argument passed into parameter 'channel' is not of type list.")
        if type(m) != Decimal: raise TypeError("Argument passed into parameter 'm' is not of type Decimal.")
        if type(c) != Decimal: raise TypeError("Argument passed into parameter 'c' is not of type Decimal.")
        return [m * i + c for i in X]
    except Exception as e:
        print("Error in function1(): " + str(e))
        sys.exit(1)
       
def function2(channel1: list, channel2: list) -> (list, Decimal):
    ''' This function takes two channel lists of equal lengths and calculates a new list 
    where each element is the sum of the corresponding elements in the original lists.
    It also calculates the average number in this new list. The function then returns the new list
    and the average value.

    Parameters:
    channel1 (list): a list of floating point numbers stored as Decimal type,
    channel2 (list): a list of floating point numbers stored as Decimal type

    Returns:
    list: a list of the sum of the corresponding elements in channel1 and channel2,
    Decimal: the mean of the values in the return list
    '''
    try:
        if type(channel1) != list: raise TypeError("Argument passed into parameter 'list1' is not of type list.")
        if type(channel2) != list: raise TypeError("Argument passed into parameter 'list2' is not of type list.")
        outputList = [i+j for i, j in zip(channel1, channel2)]
        return outputList, mean(outputList)
    except Exception as e:
        print("Error in function2(): " + str(e))
        sys.exit(1)
   
def function3(channel: list) -> list:
    '''
    This function takes a channel (a list of floating point numbers) and returns a new list of the same length
    but every value is 1 divided by each value in the list passed into the function. This function handles the
    division by zero error as if it identifies a 0 to be in the original list it will just set the value to 0
    in the return list instead of throwing an error.

    Parameters:
    channel (list): a list of floating point numbers

    Returns:
    list: a list where 1 has been divided by every value in channel
    '''
    try:
        if type(channel) != list: raise TypeError("Argument passed into parameter 'channel' is not of type list.")
        return [0 if i == 0 else 1/i for i in channel]
    except Exception as e:
        print("Error in function3(): " + str(e))
        sys.exit(1)

def function4(channel: list, metric: Decimal) -> list:
    ''' This function takes a channel list and adds a metric on to each 
    value present in the original list and then returns the result of 
    this as a new list.

    Parameters:
    channel (list): a list of floating point numbers stored as Decimal type
    metric (Decimal): a single floating point number

    Returns:
    list: a list where each value in channel has had the metric parameter added 
    '''
    try:
        if type(channel) != list: raise TypeError("Argument passed into parameter 'channel' is not of type list.")
        if type(metric) != Decimal: raise TypeError("Argument passed into parameter 'metric' is not of type Decimal.")
        return [i + metric for i in channel]
    except Exception as e:
        print("Error in function4(): " + str(e))
        sys.exit(1)

def readChannel(dir: str) -> list:
    '''
    This function takes a filename (inputted by the user) and then read in the values for a single 
    channel (a sequence of floating point numbers) from a .txt file in src/input and stores them
    in an array. Each value is set to a Decimal variable type, so there is no floating-point errors 
    when carrying out calculations with the data. 

    Parameters:
    dir (str): the filename which the user wants to read the channel data from

    Returns:
    list: a channel list of floating point numbers where each number is stored as a Decimal variable type
    '''
    try:
        print("Reading input for channel...")
        with open("inputs/"+dir) as f:
            channelArray = [Decimal(i) for i in f.read().split(', ')[1:]]
            if len(channelArray) == 0: raise ValueError
            print("Channel has been successfully read from input.")
            return channelArray
    except FileNotFoundError:
        print("File name entered for the channel data could not be found in src/inputs. Please try again.")
        return readChannel(input("Enter the name of the file which stores the channel data in src/inputs: ") or "channels.txt")
    except ValueError:
        print("The file provided does not contain any data. Please try again after amending the file format or use a different file.")
        return readChannel(input("Enter the name of the file which stores the channel data in src/inputs: ") or "channels.txt")
    except Exception:
        print("The file provided format does not match the standard format or the data is of the incorrect type. Please amend this and try and input the file again")
        return readChannel(input("Enter the name of the file which stores the channel data in src/inputs: ") or "channels.txt")
        

def readParameters(dir: str) -> (Decimal, Decimal):
    '''
    This function takes a filename (inputted by the user) and then read in the values for two 
    parameters (single floating point numbers) in a .txt file stored in src/input. It then takes
    this floating point number and stores it as a Decimal variable type so there is no 
    floating-point errors when carrying out calculations.

    Parameters:
    dir (str): the filename which the user wants to read the parameter data from

    Returns:
    Decimal: a single floating point parameter value stored as a Decimal variable type
    Decimal: a single floating point parameter value stored as a Decimal variable type
    '''
    try:
        print("Reading input for paramaters m and c...")
        with open("inputs/"+dir) as f:
            parameters = [i for i in f.readlines()]
            m = Decimal(parameters[0].replace("\n", "").replace("m,", ""))
            c = Decimal(parameters[1].replace("\n", "").replace("c,", ""))
            print("File successfully read from input.")
            return m, c
    except FileNotFoundError:
        print("File name entered for the parameters could not be found in src/inputs. Please try again.")
        return readParameters(input("Enter the name of the file which stores the parameters in src/inputs: ") or "parameters.txt")
    except ValueError:
        print("The file provided does not contain any data. Please try again after amending the file format or use a different file.")
        return readParameters(input("Enter the name of the file which stores the parameters in src/inputs: ") or "parameters.txt")
    except Exception:
        print("The file provided format does not match the standard format or the data is of the incorrect type. Please amend this and try and input the file again")
        return readParameters(input("Enter the name of the file which stores the parameters in src/inputs: ") or "parameters.txt")

def createOutputDir() -> str:
    '''This creates a unique folder for the output to be written to everytime the
    program is run. It makes it unique by adding the current date and time to the 
    end of the folder name. 
    
    Parameters:
    None

    Returns
    dir (str): returns the string of the created output folder
    '''
    dir = "output/output "+time.strftime("%d-%m-%Y %H%M%S")+"/"
    if not os.path.exists(dir): os.makedirs(dir)
    return dir
    
def writeOutput(dict, dir, fileName) -> None:
    '''This function outputs the keys and values stored in a dictionary as a 
    string in a .txt file. This file is exported to a folder in src/outputs.

    Parameters:
    dict (dict): the dictionary which keys and values are to be outputted,
    dir (str): the folder name to be written to (generated in createOutputDir()),
    fileName (str): the name of the file being exported

    Returns:
    None
    '''
    print("Exporting " + fileName + " data...")
    try:
        with open(dir+fileName, "w") as f:        
            for key in dict:
                if isinstance(dict[key], list):
                    f.write(key + ", " + listToString(dict[key]) + "\n")
                else:
                    f.write(key + ", " + str(dict[key]) + "\n")
        print(fileName + " successfully exported to src/"+dir)
    except Exception as e:
        print("Error while exporting " + fileName + ": " + str(e))
        sys.exit(1)

def listToString(lst:list) -> str:
    '''This function takes a list and converts it to a string.

    Parameters:
    lst (list): a list that is wanted to be converted to a string

    Returns:
    str: a stringfied version of lst
    '''
    try:
        if type(lst) != list: raise TypeError("Argument passed into parameter 'lst' is not of type list.")
        return ', '.join([str(float(i)) if type(i) == Decimal else str(i) for i in lst])
    except Exception as e:
        print("Error in listToString(): " + str(e))
        sys.exit(1)

def main():  

    channels = dict.fromkeys(['X', 'Y', 'A', 'B', 'C']) #Initialise dicitonary keys with no values to store channel arrays
    parameters = dict.fromkeys(['m', 'c']) #Initialise dictionary keys with no values to store parameters 
    metrics = dict.fromkeys(['b']) #Initialise dictionary keys with no values to store metrics 

    channels['X'] = readChannel(input("Enter the name of the file which stores the channel X in src/inputs: ") or "channels.txt")
    parameters['m'], parameters['c'] = readParameters(input("Enter the name of the file which stores paramaters m and c in src/inputs: ") or "parameters.txt")

    print("Processing data...")
    channels['Y'] = function1(channels['X'], parameters['m'], parameters['c'])
    channels['A'] = function3(channels['X'])
    channels['B'], metrics['b'] = function2(channels['A'],channels['Y'])
    channels['C'] = function4(channels['X'], metrics['b'])
    print("Data processed succesfully. The value of b for the provided data and parameters is " + str(metrics['b']))

    dir = createOutputDir()
    writeOutput(metrics, dir, "metric_data.txt")
    writeOutput(channels, dir, "channels_data.txt")
    writeOutput(parameters, dir, "parameters_used.txt")
    
if __name__ == "__main__":
    main()