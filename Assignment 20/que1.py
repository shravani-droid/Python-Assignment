
import threading

def DisplayEven(No):
    print("First 10 even numbers are : ")

    for i in range(2,No+1):
        print(i*2,end = " ")
   


def DisplayOdd(No):
    print("First 10 odd numbers are: ")

    for i in range(No):
        print((2*i)+1,end = " ")

    
def main():

    
    tobj1 = threading.Thread(target = DisplayEven,args=(10,))

    tobj2 = threading.Thread(target = DisplayOdd,args=(10,))

    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()


if __name__ == "__main__":
    main()