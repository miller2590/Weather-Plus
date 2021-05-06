from tkinter import *
from tkinter import messagebox
import requests
from math import floor
from config import *




# Getting weather details
def sort_weather(city):
    source = requests.get(url.format(city, api_key))

    if source:
        template = source.json()
        city = template['name']
        temp_kelvin = template['main']['temp']
        temp_fahrenheit = floor((temp_kelvin - 273.15) * 1.8 + 32)
        weather_description = template['weather'][0]['description']
        group = [city, temp_fahrenheit, weather_description]

        return group
    else:
        print("Weather Unavailable")


# City search
def search():
    city = city_text.get()
    weather = sort_weather(city)

    if weather:
        location_label['text'] = f"{weather[0]}"
        temperature_label['text'] = str(weather[1]) + " Degrees"
        description_label['text'] = str(weather[2]).capitalize()
    else:
        messagebox.showerror(f"{city} not found")


# Creating root Object
root = Tk()
root.title('Weather Plus')
root.geometry("550x800")
root.configure(background="white")


# Creating button labels
city_label = Label(
    text="Enter City Name",
    fg="black",
    bg="white",
    width=13,
    height=1
)
city_label.pack()

# Creating text entry
city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack()

# Creating location label
location_label = Label(root, text="City", font={'bold', 20})
location_label.pack()

# Creating temperature label
temperature_label = Label(root, text="")
temperature_label.pack()

# Crating description label
description_label = Label(root, text="")
description_label.pack()

# Creating submit button
submit_btn = Button(
    text="Search",
    command=search,
    width=5,
    height=0,
    fg="black",
    bg="#3ACDFF"
)
submit_btn.pack()

mainloop()
