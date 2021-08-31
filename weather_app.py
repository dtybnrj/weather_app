from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests
app = Tk()
app.title("Weather app")
app.config(background="Black")
app.geometry("700x400")

url_api ="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_file = 'weather_api.key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key']

def weather_find(city):
    final = requests.get(url_api.format(city, api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file["main"]['temp']
        c_temperature = k_temperature - 273.15
        f_temprature = (k_temperature - 273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        result = (city,country_name,c_temperature, f_temprature, weather_display)

        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0],weather[1])
        temprature_entry['text'] = '{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_info['text'] = weather[4]
    else:
        messagebox.showerror('Error','Please enter a valid city name. Cannot find this city')

search_city = StringVar()
enter_city = Entry(app, background="White",textvariable=search_city, fg="blue", font=("Arial", 25, "bold"))
enter_city.pack()
search_button = Button(app, text="SEARCH WEATHER", width=20, bg="red", fg="white", font=("Arial",25,"bold "), command=print_weather)
search_button.pack()
location_entry = Label(app, text='', font=("Arial", 35, "bold"), bg="lightblue")
location_entry.pack()
temprature_entry = Label(app, text='', font=("Arial", 35, "bold"), bg="red")
temprature_entry.pack()
weather_info = Label(app, text='', font=("Arial", 35, "bold"), bg="lightgreen")
weather_info.pack()

app.mainloop()
