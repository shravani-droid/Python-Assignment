# write a program which accept number from user and cecks weather thet number is positive or negative or zero

def ChkNum(No):
    if(No > 0 ):
        print(f"{No} is Positive Number")
    elif(No < 0):
        print(f"{No} is Negative Number")
    else:
        print("It is Zero")

def main():

    No1 = int(input("Enter the number : "))

    Ret = ChkNum(No1)

if __name__ == "__main__":
    main()