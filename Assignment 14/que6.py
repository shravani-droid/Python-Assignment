# write a lambda function which accepts two numbers and returns True if number is odd otherwise False

CheckOdd = lambda No1,No2 :(No1  % 2 != 0 and  No2 % 2 != 0 )

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))

    Ret = CheckOdd(Data1,Data2)

    print(f"The given numbers {Data1},{Data2} are Odd : ",Ret)


    if(CheckOdd == True):
        return True
    else:
        return False

    

    
if __name__ == "__main__":
    main()