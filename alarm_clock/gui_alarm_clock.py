import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox
#import winsound  # For sound alerts (Windows only)
import os

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}.")
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("Wake up! It's time!")
            # Play alarm sound
            for _ in range(5):  # Repeat the sound 5 times
                #winsound.Beep(2500, 1000)  # Frequency=2500Hz, Duration=1000ms
                os.system("aplay alarm.WAV")  # For Linux
                time.sleep(1)
            messagebox.showinfo("Alarm", "Wake up! It's time!")
            break
        time.sleep(1)

# Create GUI window
root = Tk()
root.title("Alarm Clock")
root.geometry("300x200")

# Heading
Label(root, text="Set Alarm", font=("Helvetica", 16), fg="blue").pack(pady=10)

# Time selection
frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = [f"{i:02}" for i in range(24)]  # Generate hours in HH format
hour.set(hours[0])
Label(frame, text="Hour:").grid(row=0, column=0, padx=5)
hour_menu = OptionMenu(frame, hour, *hours)
hour_menu.grid(row=0, column=1)

minute = StringVar(root)
minutes = [f"{i:02}" for i in range(60)]  # Generate minutes in MM format
minute.set(minutes[0])
Label(frame, text="Minute:").grid(row=1, column=0, padx=5)
minute_menu = OptionMenu(frame, minute, *minutes)
minute_menu.grid(row=1, column=1)

# Set Alarm Button
Button(root, text="Set Alarm", command=set_alarm, font=("Helvetica", 12)).pack(pady=20)

# Start the GUI loop
root.mainloop()
