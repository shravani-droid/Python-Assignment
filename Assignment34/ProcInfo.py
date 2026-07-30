# Desgin automation script which displays information of running processes as its name, PID , Username
# Usage: ProcInfo.py

import sys
import schedule
import time
import os
import psutil

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ("pid","name","username"))

        listprocess.append(info)

    return listprocess

def PlatformSurvellience(FileName):
    Border = "-" * 50
    print(Border)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = ("ProcessInformation_%s.log" %timestamp) 
    fobj = open(FileName,"w")

    print(f"Log File gets created sucessfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("-----Platform Survellience System-----\n")
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
    print("-----Information Of Running Process-----")
    print(Border)

    # --u , --h file handling and validations
    if(sys.argv == 1):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is automation script is use to get the information ")
            print("1 : It fetches the information of running process")
            print("2 : It fetches the process name")
            print("3 : It displays the Pid of running process")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as :")
            print(f"python {sys.argv[0]} ")

        else:
            print("Unable to process as arguments are not matching")
            print("please use --h or --u flag for getting more details")

    elif(len(sys.argv) == 1):

        PlatformSurvellience(sys.argv[0])

       
        print("Press Ctrl+c to abort the automation script")

        # schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvellience,sys.argv[1])

        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)

    else:
        print("Invalid numbers of arguments")
        print("Unable to process as arguments are not matching")
        print("please use --h or --u flag for getting more details")




if __name__ == "__main__":
    main() 