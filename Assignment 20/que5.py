
import threading

def NumList1(No):

    for i in range(1,No+1): 
        print(i,end = " ")
    print("-"*60)
   

def NumList2(No):

    for i in range(50,0,-1): 
        print(i,end = " ")
    
def main():


    tobj1 = threading.Thread(target = NumList1,args=(50,))

    tobj2 = threading.Thread(target = NumList2,args=(50,))

    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()


if __name__ == "__main__":
    main()