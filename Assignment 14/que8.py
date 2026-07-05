# write a lambda function which accepts two numbers and returns addition.

AddNum = lambda No1,No2 :(No1 + No2 )

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))

    Ret = AddNum(Data1,Data2)

    print(f"The addition of given numbers {Data1},{Data2} is  : ",Ret)


    if(AddNum == True):
        return AddNum
    
    

    
if __name__ == "__main__":
    main()