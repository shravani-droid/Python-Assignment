# write a lambda function using map() which accepts a list of numbers and returns a list of even numbers

CheckEven = lambda No:(No % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data)) 

    print("List of Even numbers  is : ",FData)

if __name__ == "__main__":
    main()