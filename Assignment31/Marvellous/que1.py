# write a program that accepts :
# A message from the user
# A time interval in seconds
# schedule the program to display the message repeatedly after specified interval


import schedule
import time
import sys

def Display(Msg,pause):
    print(Msg)

def main():
    msg1 = input("Enter the Message: ")
    interval = int(input("Enter interval in seconds: "))
    Display(msg1,interval)
    schedule.every(interval).seconds.do(Display,msg1,interval)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()