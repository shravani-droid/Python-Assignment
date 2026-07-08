# write a program which contains one lambda function which accepts one parameter and returns power of two.

Square = lambda No :(No ** 2)

def main():
    Data = int(input("Enter the number : "))

    Ret = Square(Data)

    print(f"The square of {Data} is : ",Ret)

if __name__ == "__main__":
    main()