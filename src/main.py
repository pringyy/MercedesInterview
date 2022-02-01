import sys, time, os, json
from statistics import mean
from decimal import *

getcontext().prec = 16 #sets decimel function so it can accurately round to 15 decimel places

def readInputX(dir: str) -> [float]:

    print("Reading input for X...")

    with open("inputs/"+dir) as f:
        X = [Decimal(i) for i in f.read().split(', ')[1:]]
        if len(X) == 0: raise ValueError("No values for X in the file provided.")
        print("X successfully read from input.")
        return X

def readParameters(dir: str):

    print("Reading input for paramaters m and c...")
   
    with open("inputs/"+dir) as f:
        parameters = [(i) for i in f.readlines()]
        if len(parameters) == 0: raise ValueError("No values present for paramaters in the file provided.")
        m = Decimal(float(parameters[0].replace("\n", "").replace("m,", "")))
        c = Decimal(float(parameters[1].replace("\n", "").replace("c,", "")))
        print("File successfully read from input.")
        return m, c

def function1(X:[float], m, c) -> [float]:
    return [m * i + c for i in X]

def function2(A:[float],Y:[float]) -> float:
    B = [i+j for i, j in zip(A, Y)]
    return B, mean(B)

def function3(X:[float]) ->[float]:
    return [0 if i == 0 else 1/i for i in X]

def function4(X: [float], b: float) -> [float]:
    return [i + b for i in X]
    
def writeOutput(X,Y,A,b,C, B) -> None:

    print("Exporting metric and channel data...")
    
    try:
        dir = "output/output " +time.strftime("%d-%m-%Y %H%M%S")

        if not os.path.exists(dir): os.makedirs(dir)

        with open(dir + "/channel_data", "w") as f:
            f.write('{}\n{}\n{}\n{}\n{}'.format("X, "+ floatArrayToString(X), "Y, " + floatArrayToString(Y), "A, " + floatArrayToString(A), "C, " + floatArrayToString(C), "B, " + floatArrayToString(B)))

        with open(dir + "/metric_data", "w") as f:
            f.write('{}'.format("b, " + str(b)))

        print("Exported metric_data.txt and channel_data.txt succesfully to " + "src/output/output " +time.strftime("%d-%m-%Y %H%M%S") + ".")

    except Exception as e:
        print("Error while exporting data: " + str(e))
        sys.exit(1)

def floatArrayToString(lst:[float]) -> str:
    return ', '.join([str(n) for n in lst])
          
def main():

    try:
        X = readInputX(input("Enter the name of the file which stores the channel X in src/inputs: ") or "channels.txt")
        m, c = readParameters(input("Enter the name of the file which stores paramaters m and c in src/inputs: ") or "parameters.txt")
    except Exception as e:
        print("Error reading input file: " + str(e))
        sys.exit(1)
 
    try:
        print("Processing data...")
        Y = function1(X, m, c)
        A = function3(X)
        B, b = function2(A,Y)
        C = function4(X,b)
        print("Data processed succesfully. The value of b for the provided data and parameters is " + str(b))

    except Exception as e:
        print("Error while processing data: " + str(e))
        sys.exit(1)

    writeOutput(X,Y,A,b,C,B)

if __name__ == "__main__":
    main()