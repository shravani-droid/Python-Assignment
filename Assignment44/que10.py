# drop the "English" column from original dataframe


import pandas as pd
import matplotlib.pyplot as plt


Border = "-" * 50

def Studentsmarks():

    df =pd.DataFrame ({
        "Name" : ["Amit"  ,"Sagar" ,"Pooja"],
        "Maths" : [85,90,78] ,
        "Science" : [92,88, 80,],
        "English" : [ 75, 85,82]
    })

    print(Border)
    print("Students Exam Report")
    print(Border)

    df = df.drop("English", axis=1)

    print("After Dropping English Column:")
    print(Border)
    print(df)

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()