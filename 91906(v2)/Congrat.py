from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import random

def display_congratulatory_page(result_data):
    global cur_width, expanded  # Make these variables global

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

    def on_quiz_click(event):
        # Function to handle the signup button click event
        quiz_page()

    root = Tk()
    root.geometry("600x950+50+50")

    displaybar = ImageTk.PhotoImage(Image.open('assest/rectangle.png').resize((450, 530)), Image.ANTIALIAS)
    congrat = ImageTk.PhotoImage(Image.open('assest/congrat.png').resize((500, 240)), Image.ANTIALIAS)

    menu_bar = Frame(root, width=600, height=80, background='#34ebba')
    menu_bar.place(x=0, y=0)

    title = Label(menu_bar, text='QUIZ', font=('Helvetica', 20, 'bold'), bg='#34ebba')
    title.place(x=260, y=25)

    congrats_image = Label(root, image=congrat)
    congrats_image.place(x=40, y=80)

    display_bar = Label(root, image=displaybar)
    display_bar.place(x=70, y=250)

    text1 = Label(root, text='YOU GOT', font=('Helvetica', 20, 'bold'), bg='#203243', fg='white')
    text1.place(x=220, y=290)

    # Display the quiz result data
    score_label = Label(root, text=f"Score: {result_data['score']}0%", font=('Helvetica', 40, 'bold'), bg='#203243', fg='green')
    score_label.place(x=150, y=350)

    correct_count_label = Label(root, text=f"Quiz completed successfully\nyou attempted 10 questions\nand from that {result_data['score']}/10 questions\nwas correct", font=('Helvetica', 20, 'bold'), bg='#203243', fg='white')
    correct_count_label.place(x=103, y=450)

    onemoretime = Label(root, text="One more time?", font=("Helvetica", 20, "bold underline"), foreground="blue", bg="#203243", cursor="hand2", bd=0, relief='flat')
    onemoretime.place(x=180, y=720)

    # Bind the function to the label's click event
    onemoretime.bind("<Button-1>", on_quiz_click)
    
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