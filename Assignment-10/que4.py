# write a program which accepts one number and prints all even numbers till that number

def PEven(No):

    for i in range(0,No+1):
        if(i % 2 == 0):
           print(i)
   

def main():
    No1 = int(input("Enter the number : "))

    print("All even numbers are : ")

    Ret = PEven(No1)

if __name__ == "__main__":
    main()