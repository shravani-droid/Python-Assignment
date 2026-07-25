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

def CreateBackupFile(DirectoryPath="Backup"):
    Border = "-" * 40
    timestamp = time.ctime()

    LogFileName = f"{Marvellous}_{timestamp}.txt"
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    DestinationFile= os.path.join(DirectoryPath,LogFileName)

    shutil.copy("Marvellous.txt",DestinationFile)

    fobj = open(LogFileName,"w")

    fobj.write(Border + "\n")
    fobj.write("Automation Script \n")
    fobj.write(Border + "\n\n")

    fobj.write("File Backup \n\n")
    fobj.write(Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("Log File gets created at : "+timestamp)
    fobj.write("\n"+ Border + "\n")

    fobj.close()

def main():
    
    CreateBackupFile(f1,f2)

if __name__ == "__main__":
    main()
