# Write a program that counts how many even numbers exits between 1 and N using pool.map()


import multiprocessing
import os


def EvenCount(No):
    print("Process is running with PID : ",os.getpid())

    count = 0

    for i in range(1,No+1):
       if(i % 2 == 0):
           count += 1 

    return count

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    

    pobj = multiprocessing.Pool()

    Result = pobj.map(EvenCount,Data)

    pobj.close()
    pobj.join()
    
    print("Result is : ")
    print(Result)
    print("-"*60)

    for i in range(Size):
         print(f"Even number between 1 and {Data[i]} : {Result[i]} ")

   

    

if __name__ == "__main__":
    main()