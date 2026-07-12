# For every number in the given list,count how many prime numbers exits 
# between 1 and N using multiprocessing Pool.
# example: 10000 
#          20000
#          30000 
#          40000  display total count for each number

import multiprocessing
import os


def PrimeCount(No):
    print("Process is running with PID : ",os.getpid())
    count = 0

    for i in range(2,No+1):
       Prime = True

       for j in range(2,(i//2)+1):
           if(i % j == 0):
            Prime = False
            break
       if(Prime == True):
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

    Result = pobj.map(PrimeCount,Data)

    pobj.close()
    pobj.join()
    
    
    print("Result is : ")
    print(Result)

    for i in range(Size):
         print(f"Prime number between 1 and {Data[i]} : {Result[i]} ")

   

if __name__ == "__main__":
    main()