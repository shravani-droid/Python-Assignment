# write a program which accept the two file names from user:
# first file is existing file and second file is new file
# copy all contents from the first file into the second file
# Input: ABC.txt Demo.txt
# Output: contents of ABC.txt copied into Demo.txt

def CopyData(ExistingFile,NewFile):

    f1 = open(ExistingFile,"r")
    f2 = open(NewFile,"w")

    Data = f1.read()
    f2.write(Data)

def main():
    file1 = input("Enter the existing file name : ")
    file2 = input("Enter the new file name : ")

    CopyData(file1,file2)

    print(f"Contents of {file1} are copied in {file2}")

if __name__ == "__main__":
    main()


