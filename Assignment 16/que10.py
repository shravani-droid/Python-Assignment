# write a program which accept name from user and display its length.

def DisplayLen(name1):
    count = 0
    for char in name1 :
        count += 1
    return count


def main():
    name = input("Enter the name : ")

    Ret = DisplayLen(name)
    print("Length of name is : ",Ret)

if __name__ == "__main__":
    main()