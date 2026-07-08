# Write a program which contains one function named as ChkNum() which accepts one parameter as number. if number is even then it should display "Even Number" otherwise display "Odd Number" on console.

def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False


def main():
   
    No1 = int(input("Enter the Number : "))

    Ret = ChkNum(No1)

    if (Ret == True):
        print(f"Given Number {No1} is Even ")
    else:
        print(f"Given Number {No1} is Odd  ")
 

if __name__ == "__main__":
    main()