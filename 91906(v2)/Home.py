from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import re

def getWeather():
    city = text_field.get()

    # Check if the city contains only alphabetical characters
    if not re.match("^[a-zA-Z]+$", city):
        messagebox.showerror("Invalid City Name", "Please enter a valid city name without numbers or symbols.")
        return

    geolocator = Nominatim(user_agent='your_user_agent_here')
    location = geolocator.geocode(city)

    if location:
        # Check if the location corresponds to a city level result
        if location.raw.get('type') == 'city':
            obj = TimezoneFinder()

            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            time_zone.config(text=result)
            long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)

            api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude) + "&lon=" + str(location.longitude) + "&units=metric&exclude=hourly&appid=11024d8e8defe13850dbe12e6049fbef"
            json_data = requests.get(api).json()

            # Rest of your code for processing weather data

        else:
            messagebox.showerror("Invalid City", "The entered location is not a valid city. Please enter a valid city name.")
    else:
        messagebox.showerror("Invalid Location", "The entered city name is invalid. Please enter a valid city.")

    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    t.config(text=(temp,'°C'))
    h.config(text=(humidity,'%'))
    p.config(text=(pressure,'hPa'))
    w.config(text=(wind,'m/s'))
    d.config(text=description)

    #1st cell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f'assest/{firstdayimage}@2x.png')
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f'Day:{tempday1}°C\n Night:{tempnight1}°C')

    #2nd cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    img = (Image.open(f'assest/{seconddayimage}@2x.png'))
    resized_image = img.resize((60,60))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f'Day:{tempday2}°C\n Night:{tempnight2}°C')

    #3rd cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    img = (Image.open(f'assest/{thirddayimage}@2x.png'))
    resized_image = img.resize((60,60))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f'Day:{tempday3}°C\n Night:{tempnight3}°C')

    #4th cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    img = (Image.open(f'assest/{fourthdayimage}@2x.png'))
    resized_image = img.resize((60,60))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f'Day:{tempday4}°C\n Night:{tempnight4}°C')

    #5th cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    img = (Image.open(f'assest/{fifthdayimage}@2x.png'))
    resized_image = img.resize((60,60))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f'Day:{tempday5}°C\n Night:{tempnight5}°C')

    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    img = (Image.open(f'assest/{sixthdayimage}@2x.png'))
    resized_image = img.resize((60,60))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(text=f'Day:{tempday6}°C\n Night:{tempnight6}°C')

    #7th cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    img = (Image.open(f'assest/{seventhdayimage}@2x.png'))
    resized_image = img.resize((60,60))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f'Day:{tempday7}°C\n Night:{tempnight7}°C')

    #days 
    first = datetime.now()
    day1.config(text=first.strftime('%A'))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime('%A'))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime('%A'))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime('%A'))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime('%A'))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime('%A'))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime('%A'))

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
inforectangle = ImageTk.PhotoImage(Image.open('assest/rectangle.png').resize((500, 280)), Image.ANTIALIAS)
forecastrectangle = ImageTk.PhotoImage(Image.open('assest/rectangle2.png').resize((614, 700)), Image.ANTIALIAS)
firstbox = ImageTk.PhotoImage(Image.open('assest/L.png').resize((170, 350)), Image.ANTIALIAS)
secondbox = ImageTk.PhotoImage(Image.open('assest/P.png').resize((100, 150)), Image.ANTIALIAS)

menu_bar = Frame(root, width=600, height=80, background='#34ebba')
menu_bar.place(x=0, y=0)

title = Label(menu_bar, text='Home', font=('Helvetica', 20, 'bold'), bg='#34ebba')
title.place(x=265, y=25)

#clock  
clock = Label(root, font=('Helvetica', 30, 'bold'), fg='#203243')
clock.place(x=70, y=90)

#timezone
time_zone = Label(root, font=('Helvetica', 20, 'bold'), fg='#203243')
time_zone.place(x=360, y=80)

long_lat = Label(root, font=('Helvetica', 10), fg='#203243')
long_lat.place(x=360, y=110)

#search
search_bar = Label(root, image=searchbar)
search_bar.place(x=50, y=150)

search_bar_icon = Label(root, image=searchbaricon, bg='#203243')
search_bar_icon.place(x=80, y=165)

text_field = Entry(root, justify='center', width=20, font=('poppins',25,'bold'),bg='#203243',border=0,fg='white')
text_field.place(x=140, y=175)

text_field.insert(0, 'Enter a city name')
text_field.bind('<FocusIn>', countryorcity_enter)

search_icon = Button(root, image=search, bd=0, bg='#203243', cursor='hand2', activebackground='#203243', command=getWeather)
search_icon.place(x=470, y=158)

information = Label(root, image=inforectangle)
information.place(x=50, y=260)

temperature = Label(root, text = 'Temperature :', font=('Helvetica', 15), fg='white', bg='#203243')
temperature.place(x=100, y=280)

humidity = Label(root, text = 'Humidity :', font=('Helvetica', 15), fg='white', bg='#203243')
humidity.place(x=100, y=330)

pressure = Label(root, text = 'Pressure :', font=('Helvetica', 15), fg='white', bg='#203243')
pressure.place(x=100, y=380)

wind_speed = Label(root, text = 'Wind Speed :', font=('Helvetica', 15), fg='white', bg='#203243')
wind_speed.place(x=100, y=430)

description = Label(root, text = 'Description :', font=('Helvetica', 15), fg='white', bg='#203243')
description.place(x=100, y=480)

#tphwd
t = Label(root, font=('Helvetica', 15), fg='white', bg='#203243')
t.place(x=280, y=280)

p = Label(root, font=('Helvetica', 15), fg='white', bg='#203243')
p.place(x=280, y=330)

h = Label(root, font=('Helvetica', 15), fg='white', bg='#203243')
h.place(x=280, y=380)

w = Label(root, font=('Helvetica', 15), fg='white', bg='#203243')
w.place(x=280, y=430)

d = Label(root, font=('Helvetica', 15), fg='white', bg='#203243')
d.place(x=280, y=480)

#Bottom box
forecasting = Label(root, image=forecastrectangle)
forecasting.place(x=-10, y=550)

#Bottom boxes for forecasting
label1 =Label(root, image=firstbox, bg='#203243')
label1.place(x=10, y=585)

label2 =Label(root, image=secondbox, bg='#203243')
label2.place(x=200, y=600)

label2 =Label(root, image=secondbox, bg='#203243')
label2.place(x=340, y=600)

label2 =Label(root, image=secondbox, bg='#203243')
label2.place(x=480, y=600)

label2 =Label(root, image=secondbox, bg='#203243')
label2.place(x=200, y=780)

label2 =Label(root, image=secondbox, bg='#203243')
label2.place(x=340, y=780)

label2 =Label(root, image=secondbox, bg='#203243')
label2.place(x=480, y=780)

#first cell
day1 = Label(root, font=('arial', 20), fg='white', bg='#a6a6a6' )
day1.place(x=47, y=650)

firstimage = Label(root, bg='#a6a6a6')
firstimage.place(x=47, y=690)

day1temp = Label(root, font=('arial', 15, 'bold'), fg='#fff', bg='#a6a6a6' )
day1temp.place(x=27, y=800)

#second cell
day2 = Label(root, fg='white', bg='#a6a6a6' )
day2.place(x=218, y=610)

secondimage = Label(root, bg='#a6a6a6')
secondimage.place(x=218, y=630)

day2temp = Label(root, fg='#fff', bg='#a6a6a6' )
day2temp.place(x=210, y=690)

#third cell
day3 = Label(root, fg='white', bg='#a6a6a6' )
day3.place(x=358, y=610)

thirdimage = Label(root, bg='#a6a6a6')
thirdimage.place(x=358, y=630)

day3temp = Label(root, fg='#fff', bg='#a6a6a6' )
day3temp.place(x=350, y=690)

#fourth cell
day4 = Label(root, fg='white', bg='#a6a6a6' )
day4.place(x=498, y=610)

fourthimage = Label(root, bg='#a6a6a6')
fourthimage.place(x=498, y=630)

day4temp = Label(root, fg='#fff', bg='#a6a6a6' )
day4temp.place(x=490, y=690)

#fifth cell
day5 = Label(root, fg='white', bg='#a6a6a6' )
day5.place(x=218, y=790)

fifthimage = Label(root, bg='#a6a6a6')
fifthimage.place(x=218, y=810)

day5temp = Label(root, fg='#fff', bg='#a6a6a6' )
day5temp.place(x=210, y=870)

#sixth cell
day6 = Label(root, fg='white', bg='#a6a6a6' )
day6.place(x=358, y=790)

sixthimage = Label(root, bg='#a6a6a6')
sixthimage.place(x=358, y=810)

day6temp = Label(root, fg='#fff', bg='#a6a6a6' )
day6temp.place(x=350, y=870)
#seventh cell
day7 = Label(root, fg='white', bg='#a6a6a6' )
day7.place(x=498, y=790)

seventhimage = Label(root, bg='#a6a6a6')
seventhimage.place(x=498, y=810)

day7temp = Label(root, fg='#fff', bg='#a6a6a6' )
day7temp.place(x=490, y=870)


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
