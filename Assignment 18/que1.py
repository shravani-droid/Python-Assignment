# write a program which accepts N numbers from user and store it into list. Returns addition of all elements from that list.

def Add(Data):
    sum = 0
    for value in Data :
        
        sum = sum + value

    return sum

def main():
    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    Ret = Add(Data)
    print("Addition of all elements from that list is : ",Ret)


if __name__ == "__main__":
    main()