# write a program which accepts a file name from the user and 
# checks weather that file exists in current directory or not
# Input: Demo.txt
# output: Displayweather Demo.txt exists or not.

import os

def ChkFileExist(FileName):

    FileExist = os.path.exists(FileName)

    if(FileExist == True):
        print(f"The given file {FileName} is present in the current directory")
    else:
        print(f"The given file {FileName} is not present in the current directory")

def main():
    file = input("Enter the name of file : ")

    ChkFileExist(file)

if __name__ == "__main__":
    main()