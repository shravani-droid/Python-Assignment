#Write a program which contains one function that accept one number from users and returns true if number is divisible by 5 otherwise returns false

def ChkDivi(No):
    if(No % 5 == 0):
        return True
    else:
        return False
    
def main():
    No1 = int(input("Enter the number : "))

    Ret = ChkDivi(No1)

    if(Ret == True):
        print(f"The Given number {No1} is Divisible by 5 : ",Ret)
    else:
        print(f"The Given number {No1} is Not Divisible by 5 : ",Ret)

if __name__ == "__main__":
    main()