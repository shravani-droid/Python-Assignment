
import threading

def Small(Data):
    count = 0

    for ch in Data:
        if(ch.islower()):
            count += 1
    
    print("Sum of lowercase character of list is : ",count)
    print("Tid of Small thread is : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
   
   

def Capital(Data):
    count = 0

    for ch in Data:
        if(ch.isupper()):
            count += 1
    
    print("Sum of uppercase character of list is : ",count)
    print("Tid of Capital thread is : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
   

def Digits(Data):
    count = 0
    for ch in Data:
        if(ch.isdigit() ):
            count += 1 
    print("The number of numeric digits is : ",count)
    print("Tid of Digits thread is : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    
def main():

    Data = input("Entter a string : ")

    tobj1 = threading.Thread(target = Small,args=(Data,))

    tobj2 = threading.Thread(target = Capital,args=(Data,))

    tobj3 = threading.Thread(target = Digits,args=(Data,))

    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()

    tobj3.start()
    tobj3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()