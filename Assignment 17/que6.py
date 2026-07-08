# Write a program which accepts one number and display below pattern.
# Input: 5
# Output: * * * * *
#         * * * *
#         * * *
#         * *
#         *


def Display(No):
    for i in range(No,0,-1):
        for j in range(1,i):
          print("*",end = " ")
        print("*")

def main():
    No1 = int(input("Enter the number : "))
    Ret = Display(No1)

if __name__ == "__main__":
    main()