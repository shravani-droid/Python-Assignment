# write a lambda function which accepts two numbers and returns maximum number

CheckMax = lambda No1,No2 :(No1 if No1 > No2 else No2)
def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))


    Ret = CheckMax(Data1,Data2)

    print(f"The maximum number from {Data1},{Data2} is : ",Ret)

    if(CheckMax == True):
        return CheckMax
    

if __name__ == "__main__":
    main()