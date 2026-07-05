# write a lambda function which accepts two numbers and returns largest number.

CheckLargest = lambda No1,No2 : (No1 if No1 > No2 else No2)

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))


    Ret = CheckLargest(Data1,Data2)

    print(f"The Largest number between  {Data1},{Data2} is : ",Ret)

    if(CheckLargest == True):
        return CheckLargest
    

if __name__ == "__main__":
    main()