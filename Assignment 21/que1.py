
import threading

def Prime(Data):
    print("Prime numbers are: ")
    for No in Data:
        if No <= 1:
            continue

        for i in range(2, (No // 2) + 1):
            if No % i == 0:
                break
        else:
            print(No)

def NonPrime(Data):

    print("Non-prime numbers are :")

    for No in Data:
        if No <= 1:
            print(No)
            continue
        for i in range(2, (No // 2) + 1):
            if No % i == 0:
                print(No)
                break
    
def main():

    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    tobj1 = threading.Thread(target = Prime,args=(Data,))

    tobj2 = threading.Thread(target = NonPrime,args=(Data,))

    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()