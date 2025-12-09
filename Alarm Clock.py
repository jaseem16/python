import datetime
import time
import winsound

alarm = input("Set alarm (HH:MM:SS): ")

while True:
    if datetime.datetime.now().strftime("%H:%M:%S") == alarm:
        winsound.Beep(2000, 2000)
        break
    time.sleep(1)
