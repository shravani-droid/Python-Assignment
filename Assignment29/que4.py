# write a program which accept two file name through command line argunment, 
# and compares the content of both file.
# if both file contains the same contents,display success
# otherwise display faliure
# Input: (command Line) Demo.txt Hello.txt
# Output: Success or Faliure

import sys

def ChkFileData(ExsistingFile,NewFile):
   
    file1 = open(ExsistingFile,"r")
    file2 = open(NewFile,"r")

    Data1 = file1.read()
    Data2 = file2.read()

    file1.close()
    file2.close()

    if Data1 == Data2:
        return True
    else:
        return False
    
    
def main():
    oldfile = (sys.argv[1])
    newfile = (sys.argv[2])

    Ret = ChkFileData(oldfile,newfile)

    if(Ret == True):
        print("Success")
    else:
        print("Faliure")
    

if __name__ == "__main__":
    main()
