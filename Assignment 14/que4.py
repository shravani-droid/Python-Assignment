# # write a lambda function which accepts two numbers and returns minimum number

CheckMin = lambda No1,No2 :(No1 if No1 < No2 else No2)

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))


    Ret = CheckMin(Data1,Data2)

    print(f"The minimum number from {Data1},{Data2} is : ",Ret)

    if(CheckMin == True):
        return CheckMin
    

if __name__ == "__main__":
    main()