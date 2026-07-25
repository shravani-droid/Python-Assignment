# create a task that execute every dat at 9:00 AM and prints:
# Namaskar...
# Use: schedule.every().day.at("09:00").do(...)


import schedule
import time


def DisplayMsg():
    print("Namaskar")

def main():
    schedule.every().day.at("23:52").do(DisplayMsg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()