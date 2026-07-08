# write a program which accepts N numbers from user and store it into list.Accept one another number from user and return frequency of that number from list.

def ChkFreq(Data,Freq1):
    count = 0
    for value in Data :
        if(value == Freq1):
            count += 1
           
    return count

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    Freq = int(input("Enter a Element to search : "))

    Ret = ChkFreq(Data,Freq)

    print("Frequency of Number from the given list is : ",Ret)


if __name__ == "__main__":
    main()