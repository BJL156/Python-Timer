from tqdm import tqdm
from win10toast import ToastNotifier
import time
import os

mode = int(input("secs (0), mins (1), hours(2): "))

# convert time to seconds
length = int(input("enter the length of the timer: "))
for i in range(mode):
    length *= 60

# create a notifier to send Windows notifications
toast = ToastNotifier()

while True:
    # progess bar and timer
    for i in tqdm(range(length)):
        time.sleep(1)
    
    # once timer has finished send notification and clear console
    toast.show_toast(
        title="Timer",
        msg="Fun message",
        icon_path=None,
        duration=5,
        threaded=True # keep code running while notification is out
    )

    os.system('cls' if os.name=='nt' else 'clear')