import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("french_words.csv")
word_dic = word_data.to_dict(orient="records")
random_item = {}

def generate_word():
    global random_item, flip_timer
    window.after_cancel(flip_timer)
    random_item = random.choice(word_dic)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(word_text, text=random_item['French'], fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    flip_timer = window.after(3000, generate_eng_word)

def known_word():
    word_dic.remove(random_item)
    data = pandas.DataFrame(word_dic)
    data.to_csv("words_to_learn.csv", index=False)
    generate_word()

def generate_eng_word():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(word_text, text=random_item['English'], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=generate_eng_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)

cross_img = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_img, bd=0, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR,
                       activebackground=BACKGROUND_COLOR, command=generate_word)
unknown_button.grid(column=0, row=1)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, bd=0, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR, command=known_word)
right_button.grid(column=1, row=1)

title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

generate_word()

window.mainloop()



