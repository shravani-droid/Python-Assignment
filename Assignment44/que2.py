# Use the datafframe from  and print the descriptive statistics using .describe().

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

    print("Descriptive Statistics : \n",df.describe(include="all")) # describes the ststictic info of all incuding text

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()