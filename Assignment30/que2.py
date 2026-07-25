# write a program that displays the current date and time after every 1 minute


import schedule
import time
import datetime

def Display():
    print("Current Date and Time is : ",datetime.datetime.now(),"PM")

def main():
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()