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


def DirectoryScanner(DirectoryPath = "Assignment31"):

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        print("Directory Name : ",FolderName)

        for fname in FileName:
            print("Number of Files : ",fname)

        for sname in SubFolder:
            count += 1
            print("Number of Subdirectories : ",count)

    print("Date and time of Scanning : ",datetime.datetime.now())

def main():
    Dp = print("hello")
    DirectoryScanner()
    schedule.every(9).seconds.do(DirectoryScanner,Dp)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

        

        
