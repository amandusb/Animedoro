#Pythontimer for animedoro

import time
from tkinter import *
from tkinter import messagebox

# creating the TK window
root_window = Tk()

# setting the size of the tk window
root_window.geometry("300x250")

# title for the window created
root_window.title("Animedoro")

# declare variables
hour, minute, second = StringVar(), StringVar(), StringVar()

# TODO: part of restart timer
""" def restart_Timer():
    restart = True """

def reset():
    # resets the default values of hours, minutes and seconds
    hour.set("00")
    minute.set("00")
    second.set("00")

reset()
""" # setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00") """

# use of Entry class to take input from the user
hourEntry = Entry(root_window, width = 3, font = ("Arial", 25,""),
                    textvariable = hour)
hourEntry.place(x = 80, y = 20)

minuteEntry = Entry(root_window, width = 3, font = ("Arial", 25, ""),
                    textvariable = minute)
minuteEntry.place(x = 130, y = 20)

secondEntry = Entry(root_window, width = 3, font = ("Arial", 25, ""),
                    textvariable = second)
secondEntry.place(x = 180, y = 20)

def submit():
    try:
        # input is stored in temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >- 1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # converting input in mins or secs to hours
        #
        hours = 0
        if mins >60:

            # divmod() returns a tuple of first val = temp//60, second val = temp%60
            #
            hours, mins = divmod(mins, 60)

        # using format() to store values of 2 decimals
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing 1 sec
        root_window.update()
        time.sleep(1)

        # when temp == 0, messagebox will appear and timer is up
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up")

        # every second will decrement temp
        temp -= 1

# button for setting countdown
cd_button = Button(root_window, text = 'Set time countdown', bd = '5',
                    command = submit)
cd_button.place(x = 70, y = 120)

# button for resetting countdown
# TODO: IMPLEMENT RESTART BUTTON

""" reset_button = Button(root_window, text = 'Reset timer', bd = '5',
                    command = reset, restart_Timer)
reset_button.place(x = 195, y = 120) """

# infinite loop which makes GUI-program run indefinitly until interrupted
root_window.mainloop()