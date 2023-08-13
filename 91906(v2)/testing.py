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
            "score": score,  # Pass the calculated score
        }
        root.destroy()
        Congrat.display_congratulatory_page(result_data)

root = Tk()
root.geometry("600x950+50+50")

displaybar = ImageTk.PhotoImage(Image.open('assest/Rounded Rectangle 3.png').resize((500, 100)), Image.LANCZOS)
nextbutton = ImageTk.PhotoImage(Image.open('assest/next.png').resize((200, 90)), Image.LANCZOS)

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