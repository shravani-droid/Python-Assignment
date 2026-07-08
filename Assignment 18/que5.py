# write a program which accepts N numbers from user and store it into list.Returns addition of a prime numbers from that list.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is a part of our user defined 
# module named as MarvellousNum. Name of the function from main python files should be ListPrime().

from MarvellousNum import *

def ListPrime(Data):
    sum = 0
    for value in Data :
        if(ChkPrime (value) == True):
            sum = sum + value   
    return sum

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    Ret = ListPrime(Data)
    print("Addition of all prime numbers from that list is : ",Ret)


if __name__ == "__main__":
    main()