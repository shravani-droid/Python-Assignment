# write a program which accepts N numbers from user and store it into list. Returns mininmum number from that list.

def ChkMini(Data):
    Mini = Data[0] 
    for value in Data :
        if(value < Mini):
            Mini = value
    return Mini

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    Ret = ChkMini(Data)
    print("Minimum Number from the given list is : ",Ret)


if __name__ == "__main__":
    main()