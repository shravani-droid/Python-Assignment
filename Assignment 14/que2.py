# write a lambda function which accepts one number and returns cube of that number

Cube = lambda No :(No ** 3)

def main():
    Data = int(input("Enter the number : "))

    Ret = Cube(Data)

    print(f"The cube of {Data} is : ",Ret)

if __name__ == "__main__":
    main()