# write a lambda function using map() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

GiveSum = lambda No1,No2:No1 + No2

def main():

    #list = int(input("Enter the numbers of list : "))

    Data = [4,4,6]

    #for i in range (list):
      #  l1 = input(f"Enter elements {i+1}: ")
       # Data.append(l1)

    print("Input Data is : ",Data)

    MData = reduce(GiveSum,Data)

    print("Sum of all numbers  is : ",MData)

if __name__ == "__main__":
    main()