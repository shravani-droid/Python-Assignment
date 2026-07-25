# Write a program that scans a specified directory every minute.
# The task should display:
#   Directory Name
#   Number of file
#   number of subdirectories
#   date and time of scanning ......use os module

import os
import sys
import time
import schedule
import datetime


def DirectoryScanner(DirectoryPath):

    

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        print("Directory Name : ",FolderName)

        count1 = 0
        count2 = 0

        for fname in FileName:
            count1 += 1
        print("Number of Files : ",count1)
            

        for sname in SubFolder:
            count2 += 1
        print("Number of Subdirectories : ",count2)

    print("Date and time of Scanning : ",datetime.datetime.now())

def main():
    Dp = sys.argv[1]
    DirectoryScanner(Dp)
    schedule.every(9).seconds.do(DirectoryScanner,Dp)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

        

        
