import sys, time, os, json
from statistics import mean
from decimal import *

getcontext().prec = 17 #sets decimal place for Decimal type values so program can accurately round to 16 decimal places

def function1(X: list, m: Decimal, c: Decimal) -> list:
    '''

    '''
    try:
        if type(X) != list: raise TypeError("Argument passed into parameter 'channel' is not of type list.")
        if type(m) != Decimal: raise TypeError("Argument passed into parameter 'm' is not of type Decimal.")
        if type(c) != Decimal: raise TypeError("Argument passed into parameter '' is not of type Decimal.")
        return [m * i + c for i in X]
    except Exception as e:
        print("Error in function1(): " + str(e))
       
def function2(channel1: list, channel2: list) -> (list, Decimal):
    ''' This function takes the values of channels (a list of floating point numbers) and adds
    them to each other and returns a combined list

    
    '''
    try:
        if type(channel1) != list: raise TypeError("Argument passed into parameter 'list1' is not of type list.")
        if type(channel2) != list: raise TypeError("Argument passed into parameter 'list2' is not of type list.")
        outputList = [i+j for i, j in zip(channel1, channel2)]
        return outputList, mean(outputList)
    except Exception as e:
        print("Error in function2(): " + str(e))
   
def function3(channel: list) -> list:
    '''
    This function takes a channel (a list of floating point numbers) and returns a list of the same length
    but every value has been replaced with 1/channel value

    '''
    try:
        if type(channel) != list: raise TypeError("Argument passed into parameter 'channel' is not of type list.")
        return [0 if i == 0 else 1/i for i in channel]
    except Exception as e:
        print("Error in function3(): " + str(e))

def function4(channel: list, metric: Decimal) -> list:
    ''' This function takes a channel (list of floating point numbers) and adds a metric 
    (a single floating point number) on to each value present in the channel list.

    
    '''
    try:
        if type(channel) != list: raise TypeError("Argument passed into parameter 'channel' is not of type list.")
        if type(metric) != Decimal: raise TypeError("Argument passed into parameter 'metric' is not of type Decimal.")
        return [i + metric for i in channel]
    except Exception as e:
        print("Error in function4(): " + str(e))

def readChannel(dir: str) -> list:
    '''

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
    '''

    '''
    dir = "output/output "+time.strftime("%d-%m-%Y %H%M%S")+"/"
    if not os.path.exists(dir): os.makedirs(dir)
    return dir
    
def writeOutput(dict, dir, fileName) -> None:
    '''

    '''
    print("Exporting " + fileName + " data...")
    try:
        with open(dir+fileName, "w") as f:        
            for key in dict:
                if isinstance(dict[key], list):
                    f.write(key + ", " + floatArrayToString(dict[key]) + "\n")
                else:
                    f.write(key + ", " + str(dict[key]) + "\n")
        print(fileName + " successfully exported to src/"+dir)
    except Exception as e:
        print("Error while exporting " + fileName + ": " + str(e))
        sys.exit(1)

def floatArrayToString(lst:[float]) -> str:
    return ', '.join([str(float(n)) for n in lst])

    
def main():  

    print(function4([Decimal('1'),Decimal('0.25'),Decimal('1.25'),Decimal('10.0')], Decimal('2.4')))
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