def Cube():
    No1 = int(input("Enter the number : "))
    Cu = No1 ** 3
    return Cu

def main():
    Ret = Cube()
    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()