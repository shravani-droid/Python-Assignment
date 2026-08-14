# Use KNN to predict wether a student passes or fails based on study hours and attendance

import numpy as np
import math

def EuclideanDistance(P1,P2):
    Ans = ((P1['Study Hours'] - P2['Study Hours'])**2 + (P1['Attendance'] - P2['Attendance'])**2)
    return Ans

def MarevellousKNN(new_pointS,new_pointA ,k = 3):

    Border = "-" * 40
    print(Border)

    Data = [
        {"Study Hours" : 2 , "Attendance" : 60 ,"Result" : "Fail"},
        {"Study Hours" : 5 , "Attendance" : 80 ,"Result" : "Pass"},
        {"Study Hours" : 6 , "Attendance" : 85 ,"Result" : "Pass"},
        {"Study Hours" : 1 , "Attendance" : 50 ,"Result" : "Fail"}
    ]

    print("Student Pass or Fail Dataset")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    new_point = {
        "Study Hours" : new_pointS,
        "Attendance" : new_pointA
    }

    print(Border)
    print("Distance of all point is : ")
    print(Border)

    for d in Data:
        print(d)

    print(Border)

    for d in Data : 
        d["distance"] = EuclideanDistance(d,new_point)
    
    for d in Data:
        print(d)

    print(Border)


    sorted_data = sorted(Data, key= lambda item : item["distance"])

    print(Border)
    print("Sorted Data : ")
    print(Border)

    for d in sorted_data:
        print(d)

    print(Border)

    nearest = sorted_data[:k] 

    print(Border)
    print("Nearest # member are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    votes = {}

    for neighbour in nearest:
        Result = neighbour["Result"]
        votes[Result] = votes.get(Result,0) + 1


    print(Border)
    print("Exam Result is : ")
    print(Border)

    for d in votes : 
        print("Result : ",d , f"Number of  student {d} : ",votes[d])

    print(Border)

    iMax = 0

    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Final Prediction is : ",Name)
        


def main():
    X = int(input("Enter Study Hour : "))
    Y = int(input("Enter Attendance : "))

    MarevellousKNN(X,Y)

if __name__ == "__main__":
    main()



