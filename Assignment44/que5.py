# Replace "Pooja" with "Puuja" in the Name Column

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

    print("Name Replaced Sucessfully..")
    print(Border)
    df.replace("Pooja" , "Puja" , inplace=True)

    print(df)

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()