# Group students by gender and calcute average marks


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
    
def main():
    Studentsmarks()

if __name__ == "__main__":
    main()