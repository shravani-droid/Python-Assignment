# write a program which accepts one number from user and checks weather the number is prime or not.

def ChkPrime(No):
    for i in range(2,No+1):
        if(No % i == 0):
            return False
        return True

def main():
    No1 = int(input("Enter the number : "))
    
    Ret = ChkPrime(No1)

    if(Ret == True):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")
    

if __name__ == "__main__":
    main()