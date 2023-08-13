from tkinter import *
from PIL import Image, ImageTk

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

menu_bar = Frame(root, width=700, height=80, bg='#34ebba')
menu_bar.place(x=0, y=0)

title = Label(menu_bar, text='ABOUT US', font=('Helvetica', 20, 'bold' ), bg='#34ebba')
title.place(x=240,y=25)

about_frame = Frame(root, height=650, width=500, bg='#203243')
about_frame.place(x=50, y=180)

about_text1 = 'At Eye Weather, we understand the importance of staying informed about the weather conditions in your area. Our app is designed to provide you with accurate and up-to-date weather forecasts, so you can plan your day accordingly. Whether you are heading out for work, planning a weekend getaway, or simply want to stay informed, our app has you covered.'
about_text2 = 'We are committed to safeguarding user data and privacy, adhering to industry-standard security practices and protocols. Our terms of use and privacy policy outline our approach to data collection, usage, and sharing, ensuring that your personal information is handled with the utmost care and in accordance with applicable laws.'
about_text3 = 'We invite you to join the growing EyeWeather community and embark on a journey of weather discovery, preparedness, and engagement. Download our app today and experience the future of weather forecasting. Stay informed, stay EyeWeather'
about_text4 = 'Note: The content provided above is fictional and created for the purpose of the query. Any resemblance to actual products or services is purely coincidental.'

about_content1 = Label(about_frame, text=about_text1, font=('Helvetica', 15), bg='#203243',fg='white', wraplength=400, justify='center')
about_content1.place(x=50, y=25)

about_content2 = Label(about_frame, text=about_text2, font=('Helvetica', 15), bg='#203243',fg='white', wraplength=400, justify='center')
about_content2.place(x=50, y=250)

about_content3 = Label(about_frame, text=about_text3, font=('Helvetica', 15), bg='#203243',fg='white', wraplength=400, justify='center')
about_content3.place(x=50, y=450)

about_content4 = Label(root, text=about_text4, font=('Helvetica', 10),fg='red', wraplength=500)
about_content4.place(x=50, y=850)

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