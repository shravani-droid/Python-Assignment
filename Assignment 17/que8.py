# Write a program which accepts one number and display below pattern.
# Input: 5
# Output: 1
#         1 2
#         1 2 3
#         1 2 3 4
#         1 2 3 4 5


def Display(No):
    for i in range(1,No+1):
        for j in range(1,i):
          print(j,end = " ")
        print(i)

def main():
    No1 = int(input("Enter the number : "))
    Ret = Display(No1)

if __name__ == "__main__":
    main()