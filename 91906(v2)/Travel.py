from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
import requests
import random
import re

def get_travel_suggestions(city_name):
    # Use a weather API to fetch weather data for the entered city
    city = text_field.get()

    if not re.match("^[a-zA-Z]+$", city):
        messagebox.showerror("Invalid City Name", "Please enter a valid city name without numbers or symbols.")
        return

    geolocator = Nominatim(user_agent='your_user_agent_here')
    location = geolocator.geocode(city)

    if location:
        if location.raw.get('type') == 'city':
            api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude) + "&lon=" + str(location.longitude) + "&units=metric&exclude=hourly&appid=11024d8e8defe13850dbe12e6049fbef"
            json_data = requests.get(api).json()

        else:
            messagebox.showerror("Invalid Location", "The entered city name is invalid. Please enter a valid city.")
    else:
        messagebox.showerror("Invalid Location", "The entered city name is invalid. Please enter a valid city.")


    # Extract current weather information from json_data
    current_weather = json_data['current']
    temperature = current_weather['temp']
    weather_description = current_weather['weather'][0]['description']

    todaydayimage = json_data['daily'][0]['weather'][0]['icon']
    photo = ImageTk.PhotoImage(file=f'assest/{todaydayimage}@2x.png')
    firstimage.config(image=photo)
    firstimage.image = photo

    tempday = json_data['daily'][0]['temp']['day']
    tempnight = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f'Day:{tempday}°C\n Night:{tempnight}°C')
    
    # Generate travel suggestions based on weather conditions
    if "rain" in weather_description.lower():
        return ["Today is rainy weather, it's", 
               "essential to be prepared for wet conditions.", 
               "Make sure to pack appropriate rain gear,",
               "such as waterproof jackets, umbrellas, and",
               "waterproof shoes, to keep yourself dry and",
               "comfortable. Be aware that rainy weather can",
               "lead to slippery surfaces, so take extra caution",
               "when walking or driving. Plan indoor activities",
               "or attractions to visit in case the weather",   
               "prevents you from enjoying outdoor attractions."]
    
    elif tempday > 20 and "clear" in weather_description.lower():
        return ["Let's go for a warm and sunny", 
                "adventure! However, it's important to be",
                "aware of the potential challenges that", 
                "temperatures can bring. Make sure to stay",
                "hydrated by drinking plenty of water throughout",
                "the day. It's also crucial to protect yourself",
                "from the sun's rays by wearing sunscreen,",
                "sunglasses, and a hat,and by seeking shade", 
                "during peak hours. "]
    
    elif tempday < 10:
        return ["It's a freezy day today.",
                "dress in layers to stay warm and regulate",
                "your body temperature. Wearing a base layer,",
                "insulating layer, and waterproof outer layer,",
                "can help you stay comfortable in cold weather.",
                "Don't forget to wear a hat, gloves, and a scarf",
                "to protect your extremities from the cold. Keep",
                "an eye on the weather forecast and be prepared for",
                "changes, as temperatures can drop unexpectedly.",
                "It's also crucial to stay hydrated and consume", 
                "warm beverages to help regulate your body temperature."]
    else:
        return ["It's a pleasant and versatile climate for",
                "exploration. However, it's important to be aware",
                "of the varying conditions and plan accordingly.",
                "Pack a mix of clothing, including both light and",
                "heavier layers, to accommodate temperature",
                "fluctuations throughout the day. Bring a light",
                "jacket or sweater for cooler mornings or evenings,",
                "and wear breathable clothing during the warmer",
                "parts of the day. Don't forget to include a pair",
                "of comfortable walking shoes for exploring."]

    
def getWeather():
    city = text_field.get()
    
    # Call the get_travel_suggestions function
    travel_suggestions = get_travel_suggestions(city)
    
    # Update the information_display label with travel suggestions
    information.config(text="\n".join(travel_suggestions))

min_w = 0  # Minimum width of the frame
max_w = 280  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely expanded

def expand():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = root.after(5, expand)  # Repeat this func every 5 ms
    menu_drawer.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expanded
        root.after_cancel(rep)  # Stop repeating the func

def contract():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = root.after(5, contract)  # Call this func every 5 ms
    menu_drawer.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the func

def on_enter(e):
    e.widget['background'] = 'green'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

def countryorcity_enter(event):
    # Function to handle the entry of password field
    if text_field.get() == 'Enter a city name':
        text_field.delete(0, END)

def home_page():
    root.destroy()
    import Home

def travel_page():
    root.destroy()
    import Travel

def quiz_page():
    root.destroy()
    import Quiz

def about_page():
    root.destroy()
    import About

def login_page():
    root.destroy()
    import LogIn

root = Tk()
root.geometry("600x950+50+50")

searchbar = ImageTk.PhotoImage(Image.open('assest/Rounded Rectangle 3.png').resize((500, 80)), Image.ANTIALIAS)
searchbaricon = ImageTk.PhotoImage(Image.open('assest/Layer 7.png').resize((65, 50)), Image.ANTIALIAS)
search = ImageTk.PhotoImage(Image.open('assest/search.png').resize((65, 65)), Image.ANTIALIAS)
suggestinfo = ImageTk.PhotoImage(Image.open('assest/info.png').resize((570, 340)), Image.ANTIALIAS)

menu_bar = Frame(root, width=600, height=80, background='#34ebba')
menu_bar.place(x=0, y=0)

search_bar = Label(root, image=searchbar)
search_bar.place(x=50, y=200)

search_bar_icon = Label(root, image=searchbaricon, bg='#203243')
search_bar_icon.place(x=80, y=215)

text_field = Entry(root, justify='center', width=20, font=('poppins',25,'bold'),bg='#203243',border=0,fg='white')
text_field.place(x=140, y=225)

text_field.insert(0, 'Enter a city name')
text_field.bind('<FocusIn>', countryorcity_enter)

search_icon = Button(root, image=search, bd=0, bg='#203243', cursor='hand2', activebackground='#203243', command=getWeather)
search_icon.place(x=470, y=208)

information_display = Label(root, image=suggestinfo)
information_display.place(x=10, y=400)

day1 = Label(root, font=('arial', 20), text='Toady', fg='white', bg='#727880' )
day1.place(x=70, y=450)

firstimage = Label(root, bg='#727880')
firstimage.place(x=60, y=490)

day1temp = Label(root, font=('arial', 15, 'bold'), fg='#fff', bg='#727880' )
day1temp.place(x=40, y=600)

information =  Label(root, text="", bg='#203243', fg='white',justify='left', font=('Helvetica', 13))
information.place(x=200, y=480)

title = Label(menu_bar, text='TRAVEL SUGGESTION', font=('Helvetica', 20, 'bold'), bg='#34ebba')
title.place(x=160, y=25)

root.update()  # For the width to get updated

menuopen = ImageTk.PhotoImage(Image.open('assest/menuopen.png').resize((50, 50), Image.ANTIALIAS))
menuclose = ImageTk.PhotoImage(Image.open('assest/menuclose.png').resize((50, 50), Image.ANTIALIAS))
logo = ImageTk.PhotoImage(Image.open('assest/logo.png').resize((200, 100), Image.ANTIALIAS))

menu_drawer = Frame(root, bg='white', width=0, height=root.winfo_height())
menu_drawer.place(x=0, y=0)

openmenu_button = Button(menu_bar, image=menuopen, bg='#34ebba', activebackground = '#34ebba',relief='flat',command=expand)
openmenu_button.place(x=20, y=13)

closemenu_button = Button(menu_drawer, image=menuclose, bg='white', relief='flat',command=contract)
closemenu_button.place(x=210, y=30)

logolabel = Label(menu_drawer, image=logo, bg='white')
logolabel.place(x=5, y=10)

Home_button = Button(menu_drawer, text='Home',bg = 'white', relief = 'flat', width = 39, height = 3, command=home_page)
Home_button.place(x=0,y=170)

Travel_button = Button(menu_drawer, text='Travel',bg = 'white', relief = 'flat', width = 39, height = 3, command=travel_page)
Travel_button.place(x=0,y=230)

Quiz_button = Button(menu_drawer, text='Quiz',bg = 'white', relief = 'flat', width = 39, height = 3, command=quiz_page)
Quiz_button.place(x=0,y=290)

About_button = Button(menu_drawer, text='About',bg = 'white', relief = 'flat', width = 39, height = 3, command=about_page)
About_button.place(x=0,y=350)

Logout_button = Button(menu_drawer, text='Logout',bg = 'white', relief = 'flat', width = 39, height = 3, command=login_page)
Logout_button.place(x=0,y=410)

# Bind to the frame, if entered or left
menu_drawer.bind('<Enter>')
menu_drawer.bind('<Leave>')

Home_button.bind("<Enter>", on_enter)
Home_button.bind("<Leave>", on_leave)

Travel_button.bind("<Enter>", on_enter)
Travel_button.bind("<Leave>", on_leave)

Quiz_button.bind("<Enter>", on_enter)
Quiz_button.bind("<Leave>", on_leave)

About_button.bind("<Enter>", on_enter)
About_button.bind("<Leave>", on_leave)

Logout_button.bind("<Enter>", on_enter)
Logout_button.bind("<Leave>", on_leave)

# So that it does not depend on the widgets inside the frame
menu_drawer.grid_propagate(False)

root.mainloop()