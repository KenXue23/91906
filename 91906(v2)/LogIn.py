from tkinter import *
from tkinter import ttk
import tkinter.font as TkFont
from PIL import ImageTk, Image
import customtkinter
import tkinter.messagebox as tkMessageBox
import pymysql
import db
import os
import sys

customtkinter.set_default_color_theme("green")

def signup_page():
    root.destroy()
    import signup

def on_signup_click(event):
    # Function to handle the signup button click event
    signup_page()

def clear():
    # Function to clear the input fields
    email_or_username_Entry.delete(0, END)
    passwordEntry.delete(0, END)

def connect_database():
    if email_or_username_Entry.get() == '' or passwordEntry.get() == '':
        # Check if the email/username and password fields are empty
        tkMessageBox.showerror('Error', 'Fields are required')
    else:
        if db.check_user(email_or_username_Entry.get(), passwordEntry.get()):
            # Check if the user exists in the database
            tkMessageBox.showinfo('Success', 'Login Successful')
            clear()
            root.destroy()
            import Home
            # Add your code here to proceed after successful login
        else:
            tkMessageBox.showerror('Error', 'Invalid credentials')

        
def hide():
    # Function to hide the password and switch to masked mode
    openeye.config(file='assest/colseeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    # Function to show the password in plain text
    openeye.config(file='assest/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def email_and_user_enter(event):
    # Function to handle the entry of email/username field
    if email_or_username_Entry.get() == 'Email/Username':
        email_or_username_Entry.delete(0, END)


def password_enter(event):
    # Function to handle the entry of password field
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


root = Tk()
root.title("welcome to Eye Weather - LogIn")
root.geometry("600x950+50+50")

bgImage = ImageTk.PhotoImage(Image.open('assest/bg1.png'), Image.ANTIALIAS)
openeye = PhotoImage(file='assest/openeye.png')
facebooklogo = ImageTk.PhotoImage(Image.open('assest/facebook.png'), Image.ANTIALIAS)
twitterlogo = ImageTk.PhotoImage(Image.open('assest/twitter.png'), Image.ANTIALIAS)
googlelogo = ImageTk.PhotoImage(Image.open('assest/google.png'), Image.ANTIALIAS)

bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

label = Label(root, text='Welcome To Eye Weather!', font=('Comic Sans MS', 23, 'bold'),background='#C2EBAA', foreground='Limegreen')
label.place(x=100, y=275)

heading = Label(root, text='USER LOGIN', font=('Comic Sans MS', 23, 'bold'),background='#C2EBAA', foreground='Limegreen')
heading.place(x=200, y=335)

email_or_username_Entry = Entry(root, width=22, font=('Comic Sans MS', 20, 'bold'), bd=0, foreground='Limegreen', background='#C2EBAA', highlightbackground='#C2EBAA')
email_or_username_Entry.place(x=125, y=397)

email_or_username_Entry.insert(0, 'Email/Username')
email_or_username_Entry.bind('<FocusIn>', email_and_user_enter)

frame1 = Frame(root, width=355, height=2, background='Limegreen')
frame1.place(x=125, y=434)

passwordEntry = Entry(root, width=22, font=('Comic Sans MS', 20, 'bold'), bd=0, foreground='Limegreen', background='#C2EBAA', highlightbackground='#C2EBAA')
passwordEntry.place(x=125, y=467)

passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(root, width=355, height=2, background='Limegreen')
frame2.place(x=125, y=504)

# Create a custom button style without the border
eyeButton = Button(root, image=openeye, bd=0, background='#C2EBAA', activebackground='#C2EBAA', cursor='hand2',command=hide)
eyeButton.place(x=450, y=470)

loginButton = customtkinter.CTkButton(root, text='Login', cursor='hand2', font=('Comic Sans MS', 15), width=350, bg_color='#C2EBAA', command = connect_database)
loginButton.place(x=125, y=540)

orLabel = Label(root, text='---------------OR----------------', font=('Open Sans', 16), foreground='Limegreen', background='#C2EBAA')
orLabel.place(x=120, y=600)

fbLabel = Label(root, image=facebooklogo, background='#C2EBAA')
fbLabel.place(x=160, y=650)

twLabel = Label(root, image=twitterlogo, background='#C2EBAA')
twLabel.place(x=280, y=650)

ggLabel = Label(root, image=googlelogo, background='#C2EBAA')
ggLabel.place(x=400, y=650)

signupLabel = Label(root, text="Don't have an account?", font=('Open Sans', 15, 'bold'), foreground='Limegreen',background='#C2EBAA')
signupLabel.place(x=180, y=720)

signupLabel = Label(root, text="Create a new one", font=("Open Sans", 15, "bold underline"),foreground="blue", background="#C2EBAA", cursor="hand2")
signupLabel.place(x=210, y=752)

# Configure the label to look like a button
signupLabel.config(relief="flat", bd=0)

# Bind the function to the label's click event
signupLabel.bind("<Button-1>", on_signup_click)
root.mainloop()

