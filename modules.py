from tkinter import *
import requests
from config import *
from math import floor
from tkinter import messagebox

# Creating root Object
root = Tk()
root.title('Weather Plus')
root.geometry("300x300")
root.configure(background="light sky blue")


class App:

    def __init__(self, master):

        # Creating Search label
        self.city_label = Label(
            master,
            text="Enter City Name",
            fg="white",
            bg="#0d6efd",
            width=13,
            height=1
        )
        self.city_label.configure(borderwidth=2)
        self.city_label.pack()

        # Creating text entry
        self.city_text = StringVar()
        self.city_entry = Entry(master, textvariable=self.city_text)
        self.city_entry.pack()

        # Creating location label
        self.location_label = Label(master,
                                    bg="#0d6efd",
                                    fg='white')
        self.location_label.pack()

        # Creating temperature label
        self.temperature_label = Label(master,
                                       bg="#0d6efd",
                                       fg='white'
                                       )
        self.temperature_label.pack()

        # Crating description label
        self.description_label = Label(master,
                                       bg="#0d6efd",
                                       fg='white'
                                       )
        self.description_label.pack()

        # Creating submit button
        self.submit_btn = Button(
            master,
            text="Search",
            command=self.search,
            width=5,
            height=0,
            fg="white",
            bg="#0d6efd"
        )
        self.submit_btn.configure(relief='raised', borderwidth=2)
        self.submit_btn.pack()

    # Getting weather details
    def sort_weather(self, city):
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
    def search(self):

        city = self.city_text.get()
        weather = self.sort_weather(city)

        if weather:
            self.location_label['text'] = f"{weather[0]}"
            self.temperature_label['text'] = str(weather[1]) + " Degrees"
            self.description_label['text'] = str(weather[2]).capitalize()
        else:
            messagebox.showerror("Error",
                                 f"{city} not found")
