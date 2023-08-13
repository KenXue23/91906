from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import random
import Congrat

file_name = 'Quiz.txt'
f = open(file_name, 'r')
lines = f.readlines()
f.close()

questions = []
options = []
correct_answers = []
score = []
wrong = []

for line in lines:
    line = line.strip()
    if line:
        parts = line.split(',')
        questions.append(parts[0])
        options.append(parts[1:5])
        correct_answers.append(parts[5])

def update_timer():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")

def start_timer():
    global remaining_time
    remaining_time = 10 * 60  # 5 minutes in seconds
    update_timer()

def display_question():
    global current_question, question_number
    question_number_label.config(text=f"{question_number}).", font=("Helvetica", 20), anchor='w')
    question_number_label.place(x=100, y=160)   

    # Randomly select a question index
    random_question_index = random.randint(0, len(questions) - 1)
    
    question_label.config(text=questions[random_question_index], font=("Helvetica", 16), wraplength=440, anchor='w')
    question_label.place(x=80, y=220)
    
    # Update options and correct answer for the randomly selected question
    opt_selected.set(0)
    option_a.config(text=options[random_question_index][0])
    option_b.config(text=options[random_question_index][1])
    option_c.config(text=options[random_question_index][2])
    option_d.config(text=options[random_question_index][3])
    
    # Update the current_question index
    current_question = random_question_index
    
def check_ans():
    global current_question, correct_answers, question_number, score

    option_letter_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    random_question_index = random.randint(0, len(questions) - 1)
    selected_option_value = opt_selected.get()
    selected_option_letter = option_letter_mapping.get(selected_option_value)
    if selected_option_letter == correct_answers[random_question_index]:
        score.append(1)
    else:
        wrong.append(1)

    reveal_correct_answer()

def reveal_correct_answer():
    global current_question
    
    correct_option = correct_answers[current_question]  # Get the correct answer

    correct_label.config(text=f"Correct Answer: {correct_option}", fg="green")
    correct_label.place(x=100, y=665)
    
    next_button.place(x=330 , y=635)  # Display Next button

def next_question():
    global question_number, score
    
    question_number += 1
    if question_number <= 10:
        display_question()
        correct_label.config(text="", fg="black")  # Clear correct answer label
        next_button.place_forget()  # Hide Next button if not needed
    else:
        result_data = {
            "score": len(score),  # Pass the calculated score
        }
        root.destroy()
        Congrat.display_congratulatory_page(result_data)


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

displaybar = ImageTk.PhotoImage(Image.open('assest/Rounded Rectangle 3.png').resize((500, 100)), Image.ANTIALIAS)
nextbutton = ImageTk.PhotoImage(Image.open('assest/next.png').resize((200, 90)), Image.ANTIALIAS)

menu_bar = Frame(root, width=600, height=80, background='#34ebba')
menu_bar.place(x=0, y=0)

title = Label(menu_bar, text='QUIZ', font=('Helvetica', 20, 'bold'), bg='#34ebba')
title.place(x=260, y=25)

timer_label = Label(root, text="", font=("Helvetica", 20))
timer_label.place(x=400, y=160)
start_timer()

frame = Frame(root, width=450, height=2, background='#203243')
frame.place(x=70, y=200)

opt_selected = IntVar()
current_question = 0
question_number = 1

question_number_label = Label(root, text="")
question_label = Label(root, text="", font=("Helvetica", 16), wraplength=440, anchor='w')

option_a = Radiobutton(root, text="", variable=opt_selected, value=1, font=("Helvetica", 14))
option_a.place(x=100, y=300)

option_b = Radiobutton(root, text="", variable=opt_selected, value=2, font=("Helvetica", 14))
option_b.place(x=100, y=340)

option_c = Radiobutton(root, text="", variable=opt_selected, value=3, font=("Helvetica", 14))
option_c.place(x=100, y=380)

option_d = Radiobutton(root, text="", variable=opt_selected, value=4, font=("Helvetica", 14))
option_d.place(x=100, y=420)

check_button = Button(root, text="Check Answer", command=check_ans, width=15, bg="blue", fg="white", font=("Helvetica", 16, "bold"))
check_button.place(x=190, y=500)

display_bar = Label(root, image=displaybar)
display_bar.place(x=50, y=630)

correct_label = Label(root, font=("Helvetica", 16, "bold"), bg='#203243' )

next_button =Button(root, text="Next", image=nextbutton,highlightthickness=0,bg='#203243', bd=0, activebackground='#203243', command=next_question,)

display_question()

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