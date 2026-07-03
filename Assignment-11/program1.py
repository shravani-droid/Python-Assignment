# write a program which accepts the one number and checks whether it is prime or not.


def PEven(No1):
    for i in range(2,  No1):
        if(No1 % i == 0 ):
            return False
    return True
     

def main():
    No1 = int(input("Enter the number : "))

    Ret = PEven(No1)

    if(Ret == True):
        print("Given number is prime")
    else:
        print("given is not prime")
      

if __name__ == "__main__":
    main()
