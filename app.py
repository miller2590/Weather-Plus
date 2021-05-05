from tkinter import *
import requests
import json
from configparser import ConfigParser

# Config
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Creating root Object
root = Tk()
root.title('Weather Plus')
root.geometry("550x800")
root.configure(background="white")

frame = Frame(master=root)
frame.pack(fill=X)

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
    text="Search",
    master=frame,
    width=5,
    height=0,
    fg="black",
    bg="#3ACDFF"
)
submit_btn.pack()

city_name = city_entry.get()



mainloop()
