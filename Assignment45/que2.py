# Create a gender column and perform one-hot encoding.

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

    print(Border)
    print("Gender Column added sucessfully")
    print(Border)
    print(encode)
    
def main():
    Studentsmarks()

if __name__ == "__main__":
    main()