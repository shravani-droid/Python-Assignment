def ChkGreater():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    if No1 > No2 :
        return No1
    else:
        return No2

def main():
    Ret = ChkGreater()
    print("Greater Number is : ",Ret)

if __name__ == "__main__":
    main()