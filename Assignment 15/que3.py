# # write a lambda function using map() which accepts a list of numbers and returns a list of odd numbers

CheckOdd = lambda No:(No % 2 != 0)

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckOdd,Data)) 

    print("List of Odd numbers  is : ",FData)

if __name__ == "__main__":
    main()