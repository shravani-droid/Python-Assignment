# Add new column "Total" to the Dataframe as the sum of all subject marks

import pandas as pd

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

    print(df)
    print(Border)


    df["Total"] = df["Maths"] + df["Science"] + df["English"]


    print("New Column Added Sucessfully :")
    print(Border)

    print(df)


def main():
    Studentsmarks()

if __name__ == "__main__":
    main()