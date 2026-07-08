#write a program which contains filter(),map() and reduce() in it.
# python application which contains one list of numbers.List contains the nummber which are
#  accepted from user. Filter should filter out all such numbers which are greater than or equal to 70 
# and less that or equal to 90. map function will increase each number by 10.Reduce will return product of all that number.



 
    

from functools import reduce

def CheckNum(No):
    if(No >= 70 and No <= 90):   
        return True
    else:
        return False

def Increment(No):
    return No + 10

def Product(No1,No2):
    return No1 * No2

def main():
    Data = []
    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is : ",Data)

    FData = list(filter(CheckNum,Data)) 

    print("Data after Filter is : ",FData)

    MData = list(map(Increment,FData))

    print("Data after Map : ",MData)

    RData = reduce(Product,MData)

    print("Data after Reduce : ",RData)


   

if __name__ == "__main__":
    main()