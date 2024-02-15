# NAME: gui.py
# PURPOSE: where the trivia master pulls the strings
# AUTHORS: Emma Bethel and Quinn Glickman

from tkinter import Tk, Canvas, Entry, StringVar, Label, Button
from body import BotsonBody
from ai import BotsonBrain, GptBotson


class BotsonGui:
    def __init__(self, brain: BotsonBrain, body: BotsonBody):
        self.brain = brain
        self.body = body

        self.set_up_visuals()
    
    def set_up_visuals(self):
        # background
        self.root = Tk()
        self.root.title("Botson")
        self.root.configure(background="light blue")
        self.root.minsize(800,800)
        self.canvas = Canvas(self.root, width=200, height=300, bg="light blue", highlightbackground="light blue")
        self.canvas.pack()

        # answer box
        Label(self.root, text="My answer:",
            fg = "#6b3e2e",
            bg = "light blue",
            font=("Georgia", 60)
        ).place(
            relx = 0.5,
            rely = .3,
            anchor = 'center')
        self.answer = StringVar()
        self.answer_display = Label(self.root, textvariable=self.answer)
        self.canvas.create_window(200, 180, window=self.answer_display)
        self.answer_display.pack()
        
        # question entry box
        self.question_box = Entry(self.root)
        self.canvas.create_window(200, 140, window=self.question_box)
        self.question_box.place(relx = .5, rely = .15, anchor = 'center')
        Label(self.root, text="Enter a question:",
            fg = "#6b3e2e",
            bg = "light blue",
            font=("Georgia", 60)
        ).place(
            relx = 0.5,
            rely = .05,
            anchor = 'center')
        
        # ask button
        self.ask_button = Button(text='Search!', command=self.respond_to_question)
        self.canvas.create_window(200, 180, window=self.ask_button)
        self.ask_button.place(relx = .5, rely = .2, anchor = 'center')

        # reaction buttons
        Label(self.root, text="Did I get it right?",
            fg = "#6b3e2e",
            bg = "light blue",
            font=("Georgia", 60)
        ).place(
            relx = 0.5,
            rely = .5,
            anchor = 'center')
        correct_button = Button(text='Yes', command=self.body.smile)
        self.canvas.create_window(200, 180, window=correct_button)
        correct_button.place(relx = .25, rely = .6, anchor = 'center')
        incorrect_button = Button(text='No', command=self.body.frown)
        self.canvas.create_window(200, 180, window=incorrect_button)
        incorrect_button.place(relx = .75, rely = .6, anchor = 'center')
    
    def respond_to_question(self):
        question = self.question_box.get()
        answer = self.brain.respond(question)

        self.answer.set(answer)
        self.answer_display.after(5, lambda: self.body.speak(answer))

    def start(self):
        self.body.smile()
        self.body.start_eyes_spin()
        self.root.mainloop()


if __name__ == '__main__':
    gui = BotsonGui(GptBotson(), BotsonBody())
    gui.start()