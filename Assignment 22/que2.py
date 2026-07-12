# Write a program that calculates factorials of multiple numbers simultaneously using Pool.map()
# Input: [10,15,20,25] 
# Output: process ID 
#         Input Number 
#         Factorial


import multiprocessing
import os


def Factorials(No):
    print("Process is running with PID : ",os.getpid())
    fact = 1

    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorials,Data)

    pobj.close()
    pobj.join()
    
    
    print("Result is : ")
    print(Result)

   

if __name__ == "__main__":
    main()