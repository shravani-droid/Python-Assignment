#write a program which Accepts one number and prints the factorial of tha number.

def Fact(No):
    fact = 1

    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    No1 = int(input("Enter the number : "))

    Ret = Fact(No1)

    print("Factorial of the given number is : ",Ret)
     

if __name__ =="__main__":
    main()