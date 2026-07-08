# Write a program which accept number from user and  print that number of "*" on screen

def Display(No):
    for i in range(No):
        print("*",end = " ")
    return Display

def main():
    No1 = int(input("Enter the number : "))
    Ret = Display(No1)

if __name__ == "__main__":
    main()
