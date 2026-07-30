# Desgin automation script which accepts the directory name  from the user and create  log file in that directory 
# which contains information of running process as its name,PID ,Username.
# Usage: ProcInfoLog.py Demo

import psutil
import sys
import os
import time 
import schedule

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ("pid","name","username"))

        listprocess.append(info)

    return listprocess

def PlatformSurvellience(FolderName):
    Border = "-" * 50
    print(Border)

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName) # it chehcks if directory is present or not
        if(Ret == False):
            print("Enable to process as given name is exsisting but its not a directory name")
    else:
        os.mkdir(FolderName) # it will make the directory if its not present
        print("Directory for log file is created sucessfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Process_%s.log" %timestamp) # by this file will go to folder

    fobj = open(FileName,"w")

    print(f"Log File gets created sucessfully and is created with name {FileName}")

    fobj.write(Border + "\n")
    fobj.write("-------Platform Survellience System-----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------------System Report------------------\n")

    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("User Name : %s\n" %info.get("username"))
        fobj.write(Border+"\n")
        
    fobj.write(Border+"\n")
    fobj.write("-------------End of Log File-------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-" * 50
    print(Border)
    print("------Platform Survellience System-----")
    print(Border)

    # --h --u handling
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is use to perform")
            print("1 : It fetch the information of running processes")
            print("2 : It gets auto schedule periodically")
            print("3 : It maintains all record into log file")
            print("4 : It sends the log files through periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution ")
            print("Folder_Name : Name of the folder for the log file creation")
        else:
            print("Unable to proceed as there is no matching argunment")
            print("please use --h or --u flag for getting more details")

    elif(len(sys.argv) == 3): #4
        print("Schedular Started Successfully")
        print("Press Ctrl+c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvellience,sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid numbers of arguments")
        print("Unable to process as arguments are not matching")
        print("please use --h or --u flag for getting more details")


if __name__ == "__main__":
    main()