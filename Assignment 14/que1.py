# write a lambda function which accepts one number and returns square of that number

Square = lambda No :(No ** 2)

def main():
    Data = int(input("Enter the number : "))

    Ret = Square(Data)

    print(f"The square of {Data} is : ",Ret)

if __name__ == "__main__":
    main()