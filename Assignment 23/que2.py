# Write a python program using multiprocessing.pool to calculate the sum of all odd numbers 
# from 1 to N. 
# Input: Data = [1000000,2000000,3000000,4000000] 
# Expected Task: for each number N, 
# calculate:2+4+6+...+N


import multiprocessing
import os


def SumOdd(No):
    print("Process is running with PID : ",os.getpid())

    count = 0

    for i in range(1,No+1,2):
       count = count + i

    return count

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd,Data)

    pobj.close()
    pobj.join()
    
    print("Result is : ")
    print(Result)
    print("-"*60)

    for i in range(Size):
         print(f"Sum of Odd number between 1 and {Data[i]} : {Result[i]} ")

   

    

if __name__ == "__main__":
    main()