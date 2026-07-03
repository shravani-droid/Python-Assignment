def Square():
    No1 = int(input("Enter the number : "))
    Sq = No1 * No1
    return Sq

def main():
    Ret = Square()
    print("Square is : ",Ret)

if __name__ == "__main__":
    main()