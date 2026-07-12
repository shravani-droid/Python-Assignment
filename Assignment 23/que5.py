# Write a program that calculates factorial of multiple numbers 
# simulteneously using multiprocessing.pool.



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
    print("-"*60)

    for i in range(Size):
         print(f"Factorial of {Data[i]} is : {Result[i]} ")

   

   

if __name__ == "__main__":
    main()