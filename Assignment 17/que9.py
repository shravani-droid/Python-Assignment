# write a program which accepts number from user and returns the number of digits in that number.

def Display(No):
    digit = 0
    count = 0
    while No != 0:
        digit = No % 10
        count = count + 1
        No = No // 10
    return count

def main():
    No1 = int(input("Enter the number :  "))
    
    Ret = Display(No1)

    print(f"Number of digits in {No1} nummber is : ",Ret)

if __name__ == "__main__":
    main()