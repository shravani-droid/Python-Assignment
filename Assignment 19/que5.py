#write a program which contains filter(),map() and reduce() in it.
# python application which contains one list of numbers.List contains the nummber which are
#  accepted from user.Filter shoould filter out all prime numbers. 
# map function will multiply each number by 2.Reduce will return maximum number from all that numbers.

from functools import reduce

def CheckPrime(No):
    if (No <= 1):
        return False
    
    for i in range(2,(No//2) + 1):
        if(No % i == 0):
            return False
        
    return True


def Multiply(No):
    return No * 2

def Maximum(No1,No2):
   if No1 > No2:
       return No1
   else:
       return No2

def main():
    Data = []
    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is : ",Data)

    FData = list(filter(CheckPrime,Data)) 

    print("List after Filter is : ",FData)

    MData = list(map(Multiply,FData))

    print("List after Map : ",MData)

    RData = reduce(Maximum,MData)

    print("List after Reduce : ",RData)


   

if __name__ == "__main__":
    main()