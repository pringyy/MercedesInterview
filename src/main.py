import sys
import time

m = 2.0
c = 0.5

def readInput(dir: str) -> [float]:
    """This function reads in the values for variable X

    Parameters:
    dir (str): the input filename provided by the user

    Returns:
    X ([float]): an array of floating point numbers 
    """
    try:
        with open(dir) as f:
            X = [float(i) for i in f.read().split(', ')[1:]]
            if len(X) == 0: raise ValueError("No values present.")
            return X
    except Exception as e:
        print("Error reading input file: " + str(e))
        sys.exit(1)

def function1(X:[float]) -> [float]:
    return [m*i+c for i in X]

def function2(A:[float],Y:[float]) -> float:
    return averageValue([i+j for i, j in zip(A, Y)])

def function3(X:[float]) ->[float]:
    return [0 if i == 0 else 1/i for i in X]

def function4(X: [float], b: float) -> [float]:
    return [i+b for i in X]
    
def averageValue(lst:[float]) -> float:
    """This function calculates the average value of elements an array

    Parameters:
    lst ([float]): an array of floating point numbers

    Returns:
    sum(lst)/len(lst) (float): the mean value of elements in the array
    """
    return sum(lst)/len(lst)

def floatListToString(lst:[float]) -> str:
    return ', '.join([str(n) for n in lst])

def writeOutput(X,Y,A,b,C) -> None:
    """This function exports all the data calculated in the program into a .txt file

    Parameters:

    Returns:
    None
    """
    try:
        with open("output/output "  + time.strftime("%d-%m-%Y %H%M%S") , "w") as f:
            f.write('{}\n{}\n{}\n{}\n{}'.format("X, "+ floatListToString(X), "Y, " + floatListToString(Y), "A, " + floatListToString(A), "b, " + str(b), "C, " + floatListToString(C)))
    except Exception as e:
        print("Error exporting data: " + str(e))
        sys.exit(1)
        
    
def main():
    try:
        X = readInput(input("Enter the name of the file you want to process:"))
        Y = function1(X)
        A = function3(X)
        b = function2(A,Y)
        C = function4(X,b)
        writeOutput(X,Y,A,b,C)
    except Exception as e:
        print("Error when processing data: " + str(e))
        sys.exit(1)

    print(b)
    """print(A)
    print(len(C))
    print(len(A))"""
    print(C)

if __name__ == "__main__":
    main()