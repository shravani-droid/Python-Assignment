# write a python program that perform a file backup every hour.
# Accept the source file path
# Accept the destination directory path
# Copy the source file to the destination directory
# Add the current date and time to backup filename


import os
import sys
import shutil
import time
import datetime

def CreateBackupFile(Directory,SourceFileName):
    Border = "-" * 40
    timestamp = time.ctime()

    


    LogFileName = f"{SourceFileName}_{timestamp}.log"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

   

    Ret = False
    Ret = os.path.exists(Directory)

    if(Ret == False):
        print("Automation Error:There is no such directory with name",Directory)
        return

    Ret = os.path.isdir(Directory) #isdir inbuilt function

    if(Ret == False):
        print("Automation Error : It is not a directory with name")
        return

    print("Log File gets created with file name : ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border + "\n")
    fobj.write("Automation Script \n")
    fobj.write(Border + "\n\n")

    fobj.write("File Backup \n\n")
    fobj.write(Border + "\n")

    shutil.copy(SourceFileName,Directory)

    fobj.write(Border + "\n")
    fobj.write("Log File gets created at : "+timestamp)
    fobj.write("\n"+ Border + "\n")

    fobj.close()

def main():
    f1 = (sys.argv[1])
    f2 = (sys.argv[2])

    CreateBackupFile(f1,f2)

if __name__ == "__main__":
    main()
