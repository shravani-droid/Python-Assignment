# write a program which accepts one number and display below pattern.
# input: 5
# output : * * * * *
#          * * * * *
#          * * * * *
#          * * * * *
#          * * * * *

def Display(No):
    for i in range(1,No+1):
        for j in range(1,No):
          print("*",end = " ")
        print("*")

def main():
    No1 = int(input("Enter the number : "))
    Ret = Display(No1)

if __name__ == "__main__":
    main()