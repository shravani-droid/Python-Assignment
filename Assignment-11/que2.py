# write a program which acept one number and prints count of digit in that number

def Num(No):
    digit = 0
    cnt = 0
    while No != 0:
        digit = No % 10
        cnt = cnt + 1
        No = No // 10
    return cnt

def main():
    No = int(input("Enter the Number : "))
    Ret = Num(No)
    print("Count is : ",Ret)

if __name__ == "__main__":
    main()