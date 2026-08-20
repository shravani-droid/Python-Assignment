# create a dataframe for student marks and print information like shape, columns and data types.

import pandas as pd

Border = "-" * 50

def Studentsmarks():

   
    df =pd.DataFrame ({
        "Name :" : ["Amit"  ,"Sagar" ,"Pooja"],
        "Maths :" : [85,90,78] ,
        "Science :" : [92,88, 80,],
        "English :" : [ 75, 85,82]
    })

    print(Border)
    print("Students Exam Report")
    print(Border)

    print("Shape : ",df.shape)
    print(Border)

    print("Columns : ",df.columns)
    print(Border)

    print("Data Types : \n",df.dtypes)
    print(Border)

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()