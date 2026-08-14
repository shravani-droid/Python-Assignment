# write a python program that classifies a new data using the k-nearest neighbours algorithm. 
# The algorithm should be implemented manually without using any machine learning library.

import numpy as np
import math 


def EuclideanDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier( new_pointX,new_pointY ,k=5):

    Border = "-" * 40

    Data = [
        {"Point" : "A" , "X" : 1 , "Y" : 2 , "Label" : "Red"},
        {"Point" : "B" , "X" : 2 , "Y" : 3 , "Label" : "Red"},
        {"Point" : "C" , "X" : 3 , "Y" : 1 , "Label" : "Blue"},
        {"Point" : "D" , "X" : 6 , "Y" : 5 , "Label" : "Blue"}
    ]

    print(Border)
    print("Marvellous KNN Classfier")
    print(Border)

    for i in Data:
        print(i)
    print(Border)

    new_point = {
        "X" : new_pointX,
        "Y" : new_pointY
    }

    print("Distance of all points : ")
    print(Border)

    for d in Data : 
        d["distance"] = EuclideanDistance(d,new_point)

    for d in Data:
        print(d)

    print(Border)

    sorted_data = sorted(Data , key= lambda item : item["distance"])

    print(Border)
    print("Sorted Data : ")
    print(Border)

    for d in sorted_data:
        print(d)

    print(Border)

    nearest = sorted_data[:k]

    print(Border)
    print("Nearest members are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    votes = {}

    for neighbours in nearest:
        Label = neighbours["Label"]
        votes[Label] = votes.get(Label,0) + 1

    print(Border)
    print("Voting Result is : ")
    print(Border)

    for d in votes:
        print("Name : ",d , "Number of votes : ",votes[d])

    print(Border)

    iMax = 0

    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Final Prediction is : ",Name)
    return Name



def main():
    new_pointX = int(input("Enter the coordinate of X : "))
    new_pointY = int(input("Enter the coordinate of Y : "))

    print("\nPrediction Results")
    print("-" * 30)


    result1 = MarvellousKNNClassifier(new_pointX,new_pointY,1)
    result2 = MarvellousKNNClassifier(new_pointX,new_pointY,3)
    result3 = MarvellousKNNClassifier(new_pointX,new_pointY,5)

    print("k : 1 ->",result1)
    print("k : 3 ->",result2)
    print("k : 5 ->",result3)
    
    

if __name__ == "__main__":
    main()