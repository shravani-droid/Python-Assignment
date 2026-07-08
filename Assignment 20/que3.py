
import threading

def EvenList(Data):
    Sumeven = 0

    for i in Data:
        if (i % 2 == 0):
            Sumeven =  Sumeven + i
    print("Sum of even number of list is : ",Sumeven)
   

def OddList(Data):
    Sumodd = 0

    for i in Data:
        if (i % 2 != 0):
            Sumodd =  Sumodd + i
    print("Sum of odd odd number of list is : ",Sumodd)
    
def main():

    Data = []

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        No = int(input("Enter number: "))
        Data.append(No)

    print("Input Data is:", Data)

    tobj1 = threading.Thread(target = EvenList,args=(Data,))

    tobj2 = threading.Thread(target = OddList,args=(Data,))

    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()