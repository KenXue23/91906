from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
import db


# Function to navigate to the login page
def login_page():
    signup_window.destroy()
    import LogIn

# Event handler for the login link click
def on_login_click(event):
    login_page()

# Function to clear the input fields
def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirm_passwordEntry.delete(0, END)
    emailEntry.delete(0, END)

# Function to connect to the database and perform registration
def connect_database():
    if usernameEntry.get() == '' or passwordEntry.get() == '' or confirm_passwordEntry.get() == '' or emailEntry.get() == '':
        tkMessageBox.showerror('Error', 'Fields are required')
    elif passwordEntry.get() != confirm_passwordEntry.get():
        tkMessageBox.showerror('Error', 'Password mismatch')
    elif '@' not in emailEntry.get() or '.' not in emailEntry.get():
        tkMessageBox.showerror('Error', 'Invalid email format')
    else:
        if db.insert_user(usernameEntry.get(), passwordEntry.get(), emailEntry.get()):
            tkMessageBox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import LogIn
        else:
            tkMessageBox.showerror('Error', 'Failed to register')

# Event handler for username entry focus
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

# Event handler for email entry focus
def email_enter(event):
    if emailEntry.get() == 'Email':
        emailEntry.delete(0, END)

# Event handler for password entry focus
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
        passwordEntry.config(show='*')

# Event handler for confirm password entry focus
def confirmpassword_enter(event):
    if confirm_passwordEntry.get() == 'Confirm Password':
        confirm_passwordEntry.delete(0, END)
        confirm_passwordEntry.config(show='*')


signup_window = Tk()
signup_window.title("Welcome to Eye Weather - Sign Up")
signup_window.geometry("600x950+50+50")

bgImage = ImageTk.PhotoImage(Image.open('assest/bg2.png'), Image.ANTIALIAS)
signup = ImageTk.PhotoImage(Image.open('assest/signup.png').resize((330, 100)), Image.ANTIALIAS)

bgLabel = Label(signup_window, image=bgImage)
bgLabel.place(x=0, y=0)

label = Label(signup_window, text='CREATE AN ACCOUNT', font=('Comic Sans MS', 23, 'bold'),background='#C2EBAA', foreground='Limegreen')
label.place(x=125, y=300)

usernameEntry = Entry(signup_window, width=22, font=('Comic Sans MS', 20, 'bold'), bd=0,foreground='Limegreen', background='#C2EBAA', highlightbackground='#C2EBAA')
usernameEntry.place(x=135, y=367)

usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(signup_window, width=332, height=2, background='Limegreen')
frame1.place(x=135, y=405)

emailEntry = Entry(signup_window, width=22, font=('Comic Sans MS', 20, 'bold'), bd=0,foreground='Limegreen', background='#C2EBAA', highlightbackground='#C2EBAA')
emailEntry.place(x=135, y=437)

emailEntry.insert(0, 'Email')
emailEntry.bind('<FocusIn>', email_enter)

frame2 = Frame(signup_window, width=332, height=2, background='Limegreen')
frame2.place(x=135, y=475)

passwordEntry = Entry(signup_window, width=22, font=('Comic Sans MS', 20, 'bold'), bd=0,foreground='Limegreen', background='#C2EBAA', highlightbackground='#C2EBAA')
passwordEntry.place(x=135, y=507)

passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame3 = Frame(signup_window, width=332, height=2, background='Limegreen')
frame3.place(x=135, y=545)

confirm_passwordEntry = Entry(signup_window, width=22, font=('Comic Sans MS', 20, 'bold'), bd=0,foreground='Limegreen', background='#C2EBAA', highlightbackground='#C2EBAA')
confirm_passwordEntry.place(x=135, y=577)

confirm_passwordEntry.insert(0, 'Confirm Password')
confirm_passwordEntry.bind('<FocusIn>', confirmpassword_enter)

frame4 = Frame(signup_window, width=332, height=2, background='Limegreen')
frame4.place(x=135, y=615)

signup_button = Button(signup_window, image=signup, bd=0, cursor="hand2",highlightthickness=0,bg='white', activebackground='#C2EBAA', command=connect_database)
signup_button.place(x=135, y=660)

loginLabel = Label(signup_window, text='Already have an account?', font=('Comic Sans MS', 15, 'bold'),background='#C2EBAA', foreground='Limegreen')
loginLabel.place(x=170, y=770)

loginLink = Label(signup_window, text='Click here to login', font=('Comic Sans MS', 15, 'bold', 'underline'),background='#C2EBAA', foreground='blue')
loginLink.place(x=200, y=800)

loginLink.bind('<Button-1>', on_login_click)

signup_window.mainloop()
