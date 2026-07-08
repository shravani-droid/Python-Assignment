# write a program which accept number from user and returns additioon of digit in that number.

def Add(No):
    digit = 0
    sum = 0
    while No != 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
    return sum

def main():
    No1 = int(input("Enter the number: "))

    Ret = Add(No1)

    print(f"Addition of {No1} is : ",Ret)

if __name__ == "__main__":
    main()