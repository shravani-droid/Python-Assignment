# Write a program whivh contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input: 11 5    Output: 16

def Add(No1,No2):
    add = No1 + No2
    return add


def main():
    no1 = int(input("Enter the number: "))
    no2 = int(input("Enter the number: "))

    Ret = Add(no1,no2)

    print(f"Sum of number {no1} and {no2} is : ",Ret)


if __name__ == "__main__":
    main()