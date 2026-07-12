# write a program that accepts a list of integers and uses Pool.map() to
#  calculate the sum of square from 1 to N for every element in the list.
# example Input: [1000000,2000000,30000000,4000000] 
# output: [33333833333500000,2666668666700000,........]

import multiprocessing


def SumSquare(No):
    sum =  0 
    for i in range (1,No+1):
        sum = sum + (i ** 2)

    return sum

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)



    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,Data)

    pobj.close()
    pobj.join()
    
   
    print("Result is : ")
    print(Result)

if __name__ == "__main__":
    main()