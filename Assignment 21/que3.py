import threading

Counter = 0
lock = threading.Lock()

def Increment():

    global Counter

    for i in range(1000000):
        lock.acquire()
        Counter += 1
        lock.release()


def main():

    tobj1 = threading.Thread(target=Increment)

    tobj2 = threading.Thread(target=Increment)

    tobj1.start()
    tobj2.start()
    
    tobj1.join()
    tobj2.join()
   
    print("Final Counter Value :", Counter)

if __name__ == "__main__":
    main()