from datetime import datetime
from time import sleep


def main(user_input):
    if ':' in user_input:
        alarm(int(user_input.split(':')[0]), int(user_input.split(':')[1]))
    else:
        countdown(int(user_input))

def alarm(hours, minutes):
    while True:
        now = datetime.now()
        if now.hour == hours and now.minute == minutes:
            print('Time\'s up!')
            return


def countdown(seconds):
    while True:
        sleep(seconds)
        print('Time\'s up!')
        return


if __name__ == "__main__":
    user_input = input("For countdown, type seconds. For alarm, type in format hh:mm (24 hour time) ")
    main(user_input)