
import threading

def EvenFactors(No):
    Sumeven = 0

    for i in range(1,No//2+1):
        if(No % i == 0) and (i % 2 == 0):
            Sumeven =  Sumeven + i
    print("Sum of even factors is  ",Sumeven)
   


def OddFactors(No):
    Sumodd = 0

    for i in range(1,No//2+1):
        if(No % i == 0) and (i % 2 != 0):
            Sumodd =  Sumodd + i
    print("Sum of odd factors is  ",Sumodd)
    
def main():

    No1 = int(input("Enter the number : "))

    tobj1 = threading.Thread(target = EvenFactors,args=(No1,))

    tobj2 = threading.Thread(target = OddFactors,args=(No1,))

    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()