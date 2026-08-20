# Create a bar plot of student names vs total marks


import pandas as pd
import matplotlib.pyplot as plt


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

    df.plot.bar(x="Name",y="Total",rot=0)

    plt.show()

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()