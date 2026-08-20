# Normalised the "Math" scores using Min-Max Scaling

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

    df["Maths"] = (df["Maths"] - df["Maths"].min())/(df["Maths"].max() - df["Maths"].min())

    print(Border)
    print("Report after min-max scaling")
    print(Border)
    print(df)
    
def main():
    Studentsmarks()

if __name__ == "__main__":
    main()