# Export the final DataFrame to a csv file

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

    df["Gender"] = ["Male","Male","Female"]

    # one hot encoding
    encode = pd.get_dummies(
        df,
        columns=['Gender'],
        drop_first=True,
        dtype = int)

    encode = encode.rename(columns={"Gender_Male" : "Gender"})

    result = df.groupby("Gender")[["Maths","Science","English"]].mean()

    print(Border)
    print("Average calculated sucessfully")
    print(Border)
    print(result)

    plt.pie(x=[90,88,85],labels=["Maths","Science","English"])
    plt.title("Pie Chart of Sagar's marks")

    print(Border)
    print("Pie chart created sucessfully")
    print(Border)

    plt.show()

    df["Total"] = df["Maths"] + df["Science"] + df["English"]
    
    
    print("New Column Added Sucessfully :")
    print(Border)

    df["Status"] = np.where(df["Total"] >= 250, "Pass", "Fail")

    print(df)

    PassCount = df["Status"].value_counts()["Pass"]

    print(Border)
    print("Pass Count is : ",PassCount)
    print(Border)

    df.to_csv("StudentReport.csv", index=False)

    print(Border)
    print("CSV file created Sucessfully")
    print(Border)

    
def main():
    Studentsmarks()

if __name__ == "__main__":
    main()