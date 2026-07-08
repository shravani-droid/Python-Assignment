# Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

Multiplication = lambda No1,No2 :(No1 * No2)

def main():
    Data1 = int(input("Enter the number : "))

    Data2 = int(input("Enter the number : "))

    Ret = Multiplication(Data1,Data2)

    print(f"The Multiplication of ({Data1}),({Data2}) is : ",Ret)

if __name__ == "__main__":
    main()