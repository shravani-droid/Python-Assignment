# Count Lines in a file
# Write a program which accepts a file name from the user 
# and counts how many lines are present in the file. 
# Input: Demo.txt 
# Output: Total numbers of lines in demo.txt

def CountFileLines(FileName):
    try:
        file = open(FileName,"r")
        print("File gets open")

        count = 0

        for line in file:
            count = count + 1
           
        file.close()
        return count

    except FileNotFoundError as fobj2:
        print(" File not found ")

def main():
    filename = input("Enter the file name : ")

    Ret = CountFileLines(filename)

    print(f"Number of lines present in file {filename} are : ",Ret)

    

if __name__ == "__main__":
    main()