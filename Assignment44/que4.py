# Display the students who scored more than 85 marks in science

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

    high_score = df[df["Science"] > 85]

    print("Students Who Score more than 85 in Science :")
    print(Border)
    
    print(high_score)

def main():
    Studentsmarks()

if __name__ == "__main__":
    main()