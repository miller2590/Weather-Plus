from tkinter import *
import requests
import json
from PIL import ImageTk, Image
import datetime

# Creating root Object
root = Tk()
root.title('Weather Plus')
root.geometry("550x800")
root['background'] = "white"

frame = Frame()
frame.pack()

# Creating button labels
city_label = Label(
    text="Enter City Name",
    master=frame,
    fg="black",
    width=13,
    height=1
)
city_label.pack()

# Creating text entry
city_entry = Entry(master=frame)
city_entry.pack()

# Creating submit button
submit_btn = Button(
    text="Submit",
    master=frame,
    width=5,
    height=0,
    fg="black",
    bg="#3ACDFF"
)
submit_btn.pack()

city_name = city_entry.get()

root.mainloop()

