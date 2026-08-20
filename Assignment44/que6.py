# Sort the DataFrame by "Total" marks in descending order.

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

    df.insert(4, "Total",[252,263,240])

    print(df)
    print(Border)

    print("Sorting Completed ")
    print(Border)
    df.sort_values(by="Total",ascending=False,inplace=True)
    print(df)

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()