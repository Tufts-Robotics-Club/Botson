# NAME: body.py
# PURPOSE: the body of the trivia bot!
# AUTHOR: Emma Bethel

import pyttsx3


class BotsonBody:
    def __init__(self):
        self.voicebox = pyttsx3.init()
    
    def speak(self, words):
        self.voicebox.say(words)
        self.voicebox.runAndWait()
    
    def start_eyes_spin(self):
        print("My eyes are spinning now")

    def stop_eyes_spin(self):
        print("My eyes have stopped spinning")

    def smile(self):
        print("I am smiling now")

    def frown(self):
        print("I am frowning now")

    def __del__(self):
        self.stop_eyes_spin()
