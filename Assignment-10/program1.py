# write a program which accepts one number and prints multiplication table of that nummber

def Mul(No):

    for i in range(1,11):
        print(No*i)

def main():
    No = int(input("Enter the number : "))

    print("Multiplication Table is : ")

    Ret=Mul(No)

if __name__ == "__main__":
    main()
