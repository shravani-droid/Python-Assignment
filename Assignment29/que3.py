# write a program which accept an exsiting file name through command line argunment, 
# creates a new file named Demo.txt ,and copies all contents from the given file into Demo.txt 
# Input: (command Line) ABC.txt
# Output: Create Demo.txt and copy content of ABC.txt into Demo.txt

import sys

def CopyFileData(ExsistingFile,NewFile):
   
    file1 = open(ExsistingFile,"r")
    file2 = open(NewFile,"w")
    
    Data = file1.read()
    file2.write(Data)

    file1.close()
    file2.close()

    
    
def main():
    oldfile = (sys.argv[1])
    newfile = "DemoX.txt"

    CopyFileData(oldfile,newfile)
    print(f"The content of exsitsing file is copied in new file successfully")

if __name__ == "__main__":
    main()
