#write a program which contains filter(),map() and reduce() in it.
# python application which contains one list of numbers.List contains the nummber which are
#  accepted from user.Filter shoould filter out all such numbers which are even. 
# map function will calculate its square.Reduce will return addition of all that numbers.


from functools import reduce

def CheckEven(No):
    if(No % 2 == 0):   
        return True
    else:
        return False

def Square(No):
    return No ** 2

def Product(No1,No2):
    return No1 + No2

def main():
    Data = []
    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data)) 

    print("List after Filter is : ",FData)

    MData = list(map(Square,FData))

    print("List after Map : ",MData)

    RData = reduce(Product,MData)

    print("List after Reduce : ",RData)


   

if __name__ == "__main__":
    main()