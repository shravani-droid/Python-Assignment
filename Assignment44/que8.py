# plot a line chart of mmarks for "Amit" across all subject
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

    amit_data = df[df["Name"] == "Amit"]

    subjects = ["Maths","Science","English"]
    marks = amit_data[subjects].iloc[0]

    plt.plot(subjects,marks,marker="o")

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("amits Marks in all subjects")
    plt.show()

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()