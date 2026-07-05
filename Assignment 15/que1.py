# write a lambda function using map() which accepts a list of numbers and returns a list of square of each number



Square = lambda No : No ** 2 

def main():
    Data = [4,12,8,10,5,20]

    print("Input Data is : ",Data)

    MData = list(map(Square,Data))

    print("Data after Square is : ",MData)

if __name__ == "__main__":
    main()