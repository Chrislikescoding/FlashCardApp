from tkinter import*
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    print("type")
    print(type(current_card))
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back)

def remove_word():
   to_learn.remove(current_card)
   next_card()
   print(len(to_learn))
   data=pandas.DataFrame(to_learn)
   data.to_csv("data/words_to_learn.csv",index=False)



window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("PyFlash")
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title=canvas.create_text(400,150, font=("Ariel",40, "italic"))
card_word=canvas.create_text(400,263, font=("Ariel",60, "bold"))

right = PhotoImage(file="images/right.png")
right_button =Button(image=right,highlightthickness=0,command=remove_word)
right_button.grid(row=2,column=1)
wrong = PhotoImage(file="images/wrong.png")
wrong_button =Button(image=wrong,highlightthickness=0,command=next_card)
wrong_button.grid(row=2,column=0)
canvas.grid(row = 0,column =0,columnspan=2,rowspan=2,sticky="we")

# word= Entry(text = "Word")
# word.configure(font=("Arial",30,"bold"))
# word.grid(column=0,row=1,columnspan=2)


next_card()




window.mainloop()