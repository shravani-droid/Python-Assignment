# Create a function named:
# DisplayMessage(message)
# Schedule the function using:
#   schedule.every(5).seconds.do(DisplayMessage,message)  the message should be accepted from user


import schedule
import time
import sys

def DisplayMessage(Msg):
    print(Msg)

def main():
    msg1 = input("Enter the Message: ")

    DisplayMessage(msg1)
    schedule.every(5).seconds.do(DisplayMessage,msg1)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()