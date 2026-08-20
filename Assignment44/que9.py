# Create a Dataframe with missing value and fill them with column means
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Border = "-" * 50
def Studentsmarks():

    df =pd.DataFrame ({
        "Name" : ["Amit"  ,"Sagar" ,"Pooja"],
        "Maths" : [np.nan,76,88] ,
        "Science" : [91,np.nan, 85]
    })

    print(Border)
    print("Students Exam Report")
    print(Border)

    print("Before Filling Missing Values:")
    print(df)

    print(Border)
    print("Missing Values:")
    print(df.isna().sum())

    df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
    df["Science"] = df["Science"].fillna(df["Science"].mean())

    print(Border)
    print("After Filling Missing Values:")
    print(df)

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()