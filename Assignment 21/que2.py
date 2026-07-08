import threading

def Maximum(Data):

    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    print("Maximum number is :", Max)


def Minimum(Data):

    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    print("Minimum number is :", Min)


def main():

    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    tobj1 = threading.Thread(target=Maximum, args=(Data,))
    tobj2 = threading.Thread(target=Minimum, args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    


if __name__ == "__main__":
    main()