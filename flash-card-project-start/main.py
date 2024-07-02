

from tkinter import*

window=Tk()
window.config(padx=50,pady=50)
window.title("")

canvas=Canvas(width=800,height=526,background=BACKGROUND_COLOR)
card_back = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_front = PhotoImage(file="flash-card-project-start/images/card_front.png")
right = PhotoImage(file="flash-card-project-start/images/right.png")
wrong = PhotoImage(file="flash-card-project-start/images/wrong.png")


canvas.create_image(400, 236, image=card_front)
canvas.grid(row = 0,column =0,columnspan=2,rowspan=2,sticky="we")


#canvas.create_image(30, 30, image=right)

tick=Button(image=right, highlightthickness=0)
tick.grid(column=2,row=2)
cross=Button(image=wrong, highlightthickness=0)
cross.grid(column=0,row=2)

title=Label(text = "Title")
title.configure(font=("Arial",40, "italic"))
title.grid(column=0,row=0,columnspan=2)

word= Entry(text = "Word")
word.configure(font=("Arial",30,"bold"))
word.grid(column=0,row=1,columnspan=2)

window.mainloop()