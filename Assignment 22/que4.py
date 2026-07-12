# Write a program that calculates :
# 1^5+2^5+3^5+......+N^5  
# for multiple value of N simultaneously using Pool.
# Input: [1000000,2000000,3000000,4000000] 
#  measure total executation time.

import multiprocessing
import os
import time 

def SumCube(No):
    print("Process is running with PID : ",os.getpid())
    sum =  0 
    for i in range (1,No+1):
        sum = sum + (i ** 5)

    return sum

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumCube,Data)

    pobj.close()
    pobj.join()
    
    end_time = time.perf_counter()

    print("Result is : ")
    print(Result)

    print(f"Time Requried : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()