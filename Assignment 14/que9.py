# write a lambda function which accepts two numbers and returns multiplication.

MultiplyNum = lambda No1,No2 :(No1 * No2 )

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))

    Ret = MultiplyNum(Data1,Data2)

    print(f"The Multiplication of given numbers {Data1},{Data2} is  : ",Ret)


    if(MultiplyNum == True):
        return MultiplyNum
    

    
if __name__ == "__main__":
    main()