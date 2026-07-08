# write a program which accepts one number and display below pattern.
# input: 5
# output : 1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5

def Display(No):
    for i in range(1,No):
        for j in range(1,No):
          print(j,end = " ")
        print(No)

def main():
    No1 = int(input("Enter the number : "))
    Ret = Display(No1)

if __name__ == "__main__":
    main()