# scheduule a task that executes every five minute


import schedule
import time
import datetime
import sys

def Display(FileName):
    file = open(FileName,"a")
    file.write(f"Task executed at : {datetime.datetime.now()}\n")

    file.close()

def main():
    file = sys.argv[1]

    Display(file)

    schedule.every(5).minutes.do(Display,"Marvellous.txt")

    while True:
        schedule.run_pending()
        time.sleep(1)

    
if __name__ == "__main__":
    main()