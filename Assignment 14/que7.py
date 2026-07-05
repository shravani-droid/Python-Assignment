# write a lambda function which accepts two numbers and returns True if divisible by 5

CheckDivisible = lambda No1,No2 :(No1  % 5 == 0 and  No2 % 5 == 0 )

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))

    Ret = CheckDivisible(Data1,Data2)

    print(f"The given numbers {Data1},{Data2} are divisible by 5 : ",Ret)


    if(CheckDivisible == True):
        return True
    else:
        return False

    

    
if __name__ == "__main__":
    main()