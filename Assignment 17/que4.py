# write a program which accepts one number from user and returns addition of its factors.

def Fact(No):
    sum = 0

    for i in range(1,No//2+1):
        if(No % i == 0):
            sum =  sum + i
    return sum

def main():
    No1 = int(input("Enter the number : "))

    Ret = Fact(No1)

    print(f"Sum of factors of {No1} is : ",Ret)
     

if __name__ =="__main__":
    main()