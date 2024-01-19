# Google Search Web Scraper
# Author: Reid Baris

import requests
from bs4 import BeautifulSoup
from ai import GptBotson, Botson

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Botson")
root.configure(background="light blue")
root.minsize(800,800)


canvas1 = Canvas(root, width=200, height=300, bg="light blue", highlightbackground="light blue")
canvas1.pack()

entry1 = Entry(root)
canvas1.create_window(200, 140, window=entry1)
entry1.place(relx = .5, rely = .15, anchor = 'center')

currAnswer = StringVar()
# label2 = Label(root, text=currAnswer).pack()
#                 canvas1.create_window(200, 180, window=label2)

def respond(botson: Botson):
    question = entry1.get()
    answer = botson.respond(question)
    currAnswer.set(answer)

                
text = Label(root, text="Enter a question:",
        fg = "#6b3e2e",
        bg = "light blue",
        font=("Georgia", 60)
).place(
    relx = 0.5,
    rely = .05,
    anchor = 'center')


botson = GptBotson()
button1 = Button(text='Search!', command=lambda: respond(botson))
canvas1.create_window(200, 180, window=button1)
button1.place(relx = .5, rely = .2, anchor = 'center')

 
label2 = Label(root, textvariable=currAnswer).pack()
canvas1.create_window(200, 180, window=label2)

img = ImageTk.PhotoImage(Image.open("botson.png"))
label = Label(root, image = img)
label.pack()


root.mainloop()
    
