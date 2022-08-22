from tqdm import tqdm
import pyfiglet
from win10toast import ToastNotifier
import time
import os
import json

# load json data
data = ''
with open("data", "r") as dfile:
    data = json.load(dfile)

# apply settings
progess_bar_update = data["progress_bar_update"]
title = data["title"]
message = data["message"]

def timer():
    unit = int(input("secs (0), mins (1), hours(2): "))

    # convert time to seconds
    length = int(input("enter the length of the timer: "))
    for i in range(unit):
        length *= 60

    # create a notifier to send Windows notifications
    toast = ToastNotifier()

    while True:
        # progess bar and timer
        for i in tqdm(range(int(length * progess_bar_update))):
            time.sleep(1 / progess_bar_update)
        
        # once timer has finished send notification and clear console
        toast.show_toast(
            title=title,
            msg=message,
            icon_path=None,
            duration=5,
            threaded=True # keep code running while notification is out
        )

        os.system('cls' if os.name=='nt' else 'clear')
        print("Python Timer Save Data: \n" + str(data))
        print(pyfiglet.figlet_format("Python Timer")) # fancy large text

def settings():
    # get setting to be changed
    setting_input = int(input("notifier (0), progess bar (1): "))

    if setting_input == 0:
        # change toast notification
        part = int(input("title (0), message (1): "))

        if part == 0:
            data["title"] = input("enter title of toast notification: ")
        elif part == 1:
            data["message"] = input("enter message of toast notification: ")
        else:
            input(f"error: mode {part} not available.")
            return

        # write new data to json file
        with open("data", "w") as dfile:
            json.dump(data, dfile)
        print("changes successful.")
    elif setting_input == 1:
        # progess bar settings
        data["progress_bar_update"] = int(input("enter progess bar update rate: ")) # change json data

        # write new data to json file
        with open("data", "w") as dfile:
            json.dump(data, dfile)
        print("changes successful.")
    else:
        input(f"error: mode {setting_input} not available.")


# start screen
print("Python Timer Save Data: \n" + str(data))
print(pyfiglet.figlet_format("Python Timer")) # fancy large text
mode = int(input("timer (0), settings(1): "))
if mode == 0:
    timer()
if mode == 1:
    settings()
else:
    input(f"error: mode {mode} not available.")

# exit
print("exiting program in 1 second.")
time.sleep(1)