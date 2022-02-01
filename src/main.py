import sys, time, os, json
from typing import List
from statistics import mean
from decimal import *

getcontext().prec = 16 #sets decimel function so it can accurately round to 15 decimel places

def readInputX(dir: str) -> List[float]:
    
    try:
        print("Reading input for X...")

        with open("inputs/"+dir) as f:
            X = [Decimal(i) for i in f.read().split(', ')[1:]]
            if len(X) == 0: raise ValueError("No values for X in the file provided.")
            print("X successfully read from input.")
            return X
    except Exception as e:
        print("Error reading input file: " + str(e))
        sys.exit(1)

def readParameters(dir: str) -> (float,float):

    try:
        print("Reading input for paramaters m and c...")
        with open("inputs/"+dir) as f:
            parameters = [i for i in f.readlines()]
            if len(parameters) != 2: raise ValueError("Not correct number of values for paramaters present in the input file.")
            m = Decimal(float(parameters[0].replace("\n", "").replace("m,", "")))
            c = Decimal(float(parameters[1].replace("\n", "").replace("c,", "")))
            print("File successfully read from input.")
            return m, c

    except Exception as e:
        print("Error reading input file: " + str(e))
        sys.exit(1)

def function1(X:List[float], m: float, c: float) -> List[float]:
    try:
        return [m * i + c for i in X]
    except Exception as e:
        print("Error while calculating array Y: " + str(e))
        sys.exit(1)

def function2(A: List[float],Y: List[float]) -> (List[float], float):
    try:
        B = [i+j for i, j in zip(A, Y)]
        return B, mean(B)
    except Exception as e:
        print("Error while calculating array B and metric b: " + str(e))
        sys.exit(1)

def function3(X: List[float]) -> List[float]:
    try:
        return [0 if i == 0 else 1/i for i in X]
    except Exception as e:
        print("Error while calculating array A: " + str(e))
        sys.exit(1)

def function4(X: List[float], b: float) -> List[float]:
    try:
        return [i + b for i in X]
    except Exception as e:
        print("Error while calculating array C: " + str(e))
        sys.exit(1)
    
    
def writeOutput(channels, b) -> None:

    print("Exporting metric and channel data...")
    
    try:
        dir = "output/output " +time.strftime("%d-%m-%Y %H%M%S")

        if not os.path.exists(dir): os.makedirs(dir)

        with open(dir + "/channel_data.txt", "w") as f:
            for key in channels:
                f.write(key + ", " + floatArrayToString(channels[key]) + "\n")

        with open(dir + "/metric_data.txt", "w") as f:
            f.write('{}'.format("b, " + str(b)))

        print("Exported metric_data.txt and channel_data.txt succesfully to " + "src/output/output " +time.strftime("%d-%m-%Y %H%M%S") + ".")
        
    except Exception as e:
        print("Error while exporting data: " + str(e))
        sys.exit(1)

def floatArrayToString(lst:[float]) -> str:
    return ', '.join([str(n) for n in lst])
          
def main():
  
    X = readInputX(input("Enter the name of the file which stores the channel X in src/inputs: ") or "channels.txt")
    m, c = readParameters(input("Enter the name of the file which stores paramaters m and c in src/inputs: ") or "parameters.txt")

    print("Processing data...")
    Y = function1(X, m, c)
    A = function3(X)
    B, b = function2(A,Y)
    C = function4(X,b)
    print("Data processed succesfully. The value of b for the provided data and parameters is " + str(b))

    channelDict = dict(X = X, Y = Y, A = A, B = B, C = C) 
    writeOutput(channelDict, b)

if __name__ == "__main__":
    main()