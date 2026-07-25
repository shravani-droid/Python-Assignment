# write a script that schedule a following task:
# print Lunch Time ! every day at 1:00 pm
# print wrap up work every day at 6:00 pm


import schedule
import time


def DisplayMsg1():
    print("Lunch Time !")

def DisplayMsg2():
    print("Wrap up work.")

def main():
    schedule.every().day.at("18:26").do(DisplayMsg1)
    schedule.every().day.at("18:25").do(DisplayMsg2)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()