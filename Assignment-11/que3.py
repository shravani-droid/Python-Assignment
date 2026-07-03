#write a program which acept one number and prints sum of digit

def Sum(No):
    digit = 0
    sum = 0
    while No != 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
        
    return sum


def main():
    No = int(input("Enter the number : "))
    Ret = Sum(No)
    print("The sum is : ",Ret)

if __name__ == "__main__":
    main()