import threading

def Sum(No):

    Add = 0

    for i in No:
        Add = Add + i

    print("Sum of elements is :", Add)


def Product(No):

    Mult = 1

    for i in No:
        Mult = Mult * i

    print("Product of elements is :", Mult)


def main():

    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    tobj1 = threading.Thread(target=Sum, args=(Data,))
    tobj2 = threading.Thread(target=Product, args=(Data,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()