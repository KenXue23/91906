from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import random
import Congrat

# Set the file name to 'Quiz.txt'
file_name = 'Quiz.txt'  

# Open the file in read mode
f = open(file_name, 'r') 

# Read all lines from the file
lines = f.readlines() 

 # Close the file
f.close() 

# Initialize an empty list to store questions
questions = []  
 # Initialize an empty list to store options for each question
options = []  
# Initialize an empty list to store correct answers
correct_answers = [] 
# Initialize an empty list to store scores
score = []  
# Initialize an empty list to store wrong answers
wrong = []  

# Loop through each line and process the data
for line in lines:
    # Remove leading/trailing whitespace
    line = line.strip()  
    if line:
         # Split the line into parts using ',' as a delimiter
        parts = line.split(',')  
        # Add the question to the questions list
        questions.append(parts[0])  
        # Add the options to the options list
        options.append(parts[1:5])  
        # Add the correct answer to the correct_answers list
        correct_answers.append(parts[5])  

# Update the timer label to display the remaining time
def update_timer():
    # Access the global variable remaining_time
    global remaining_time 
    # If there is remaining time
    if remaining_time > 0:  
        # Decrease the remaining time by 1 second
        remaining_time -= 1  
        # Calculate minutes from remaining seconds
        minutes = remaining_time // 60  
        # Calculate seconds from remaining seconds
        seconds = remaining_time % 60 
        # Update the timer label
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")  
        # Call this function again after 1000ms (1 second)
        root.after(1000, update_timer)  
    else:
        # If time is up, display "Time's up!"
        timer_label.config(text="Time's up!")
        root.destroy()  # Close the GUI window
        Congrat.display_congratulatory_page()  


def start_timer():
    # Access the global variable remaining_time
    global remaining_time  
    # Set the remaining time to 10 minutes (converted to seconds)
    remaining_time = 10 * 60  
    # Start the timer countdown
    update_timer()  

def display_question():
    # Access global variables
    global current_question, question_number  
    # Update the question number label
    question_number_label.config(text=f"{question_number}).", font=("Helvetica", 20), anchor='w')  
    # Set the position of the question number label
    question_number_label.place(x=100, y=160)  

    # Select a random question index
    random_question_index = random.randint(0, len(questions) - 1)  
    # Update the question label
    question_label.config(text=questions[random_question_index], font=("Helvetica", 16), wraplength=440, anchor='w')  
    # Set the position of the question label
    question_label.place(x=80, y=220)  

    opt_selected.set(0)  # Set the selected option to 0 (none selected)
    option_a.config(text=options[random_question_index][0])  # Update option A label
    option_b.config(text=options[random_question_index][1])  # Update option B label
    option_c.config(text=options[random_question_index][2])  # Update option C label
    option_d.config(text=options[random_question_index][3])  # Update option D label

    # Update the current question index
    current_question = random_question_index  

def check_ans():
    # Access global variables
    global current_question, correct_answers, question_number, score  

    # Mapping of option values to letters
    option_letter_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}  
    # Select a random question index
    random_question_index = random.randint(0, len(questions) - 1)  
    # Get the selected option value
    selected_option_value = opt_selected.get()  
    # Get the corresponding letter for the selected option
    selected_option_letter = option_letter_mapping.get(selected_option_value)  
    # If the selected option is correct
    if selected_option_letter == correct_answers[random_question_index]:  
        # Add 1 to the score list (correct answer)
        score.append(1)  
    else:
        # Add 1 to the wrong list (wrong answer)
        wrong.append(1)  
    # Call the function to reveal the correct answer
    reveal_correct_answer()  

def reveal_correct_answer():
    # Access global variable
    global current_question  

    # Get the correct answer for the current question
    correct_option = correct_answers[current_question] 
    # Update the correct answer label
    correct_label.config(text=f"Correct Answer: {correct_option}", fg="green")  
    # Set the position of the correct answer label
    correct_label.place(x=100, y=665)  
    # Set the position of the Next button
    next_button.place(x=330 , y=635)  

def next_question():
    # Access global variables
    global question_number, score  
    # Increment the question number
    question_number += 1  
    # If there are more questions remaining
    if question_number <= 10:  
        # Display the next question
        display_question() 
        # Clear the correct answer label
        correct_label.config(text="", fg="black")  
        # Hide the Next button if not needed
        next_button.place_forget()  
    else:
        result_data = {
            # Calculate and store the score
            "score": len(score),  
        }
        # Close the GUI window
        root.destroy()  
        # Display congratulatory page with the score
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

