import time
from datetime import datetime
#import winsound  # For sound alerts (Windows only)
import os

def set_alarm():
    alarm_time = input("Enter the alarm time (HH:MM, 24-hour format): ")
    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        # Get the current time in HH:MM format
        now = datetime.now().strftime("%H:%M")
        
        if now == alarm_time:
            print("Wake up! It's time!")
            # Play an alarm sound
            for _ in range(5):  # Repeat the sound 5 times
                #winsound.Beep(2500, 1000)  # Frequency=2500Hz, Duration=1000ms
                os.system("aplay alarm.WAV")  # For Linux
                time.sleep(1)
            break
        
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    set_alarm()
