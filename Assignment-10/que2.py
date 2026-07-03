# write a program which accepts the number and prints the sum of first N natural numbers.

def Sum(No):
    Add = 0

    for i in range(1,No+1):
        Add = Add + i
    return Add

def main():
    No1 = int(input("Enter the number :  "))

    Ret = Sum(No1)

    print("Sum of N Natural Numbers is : ",Ret)

if __name__ == "__main__":
    main()