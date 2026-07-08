# write a program which accepts N numbers from user and store it into list. Returns maximum number from that list.

def ChkMax(Data):
    Max = Data[0] 
    for value in Data :
        if(value > Max):
            Max = value
    return Max

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    Ret = ChkMax(Data)
    print("Maximum Number from the given list is : ",Ret)


if __name__ == "__main__":
    main()