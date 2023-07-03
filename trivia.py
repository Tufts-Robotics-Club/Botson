# Google Search Web Scraper
# Author: Reid Baris

import requests
from bs4 import BeautifulSoup

# Keep asking questions
# question = ""
# while question.lower() != 'q' and question.lower() != "quit":
# # Get the question, format it into a Google search
# words = input("Enter a question: ").split(' ')
# question = ""
# for word in words:
#     question += word + "+"
# question = question[:-1]
# 
# # Get all of the HTML code from the website
# URL = "https://www.google.com/search?q=" + question + "&rlz=1C1CHBF_enUS892US892&oq=what+day+is+it&aqs=chrome.0" \
#                                                       ".0i512l4j0i131i433j0i512l5.7446j0j1&sourceid=chrome&ie=UTF-8"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html5lib')
# 
# answer_keys_1 = ["<div class=\"BNeawe iBp4i AP7Wnd\"><div><div class=\"BNeawe iBp4i AP7Wnd\">",
#                  "<div class=\"BNeawe s3v9rd AP7Wnd\"><span class=\"atOwb UMOHqf\">",
#                  ]
# answer_keys_2 = ["</div>", "</span", "</div>"]
# wiki_key_1 = "<h3 class=\"zBAuLc l97dzf\"><div class=\"BNeawe vvjwJb AP7Wnd\">"
# wiki_key_2 = "</div>"
# 
# found = False
# 
# if question.lower() != 'q' and question.lower() != "quit":
#     # Try a range of techniques
#     for i in range(0, len(answer_keys_1)):
#         data = str(soup)
# 
#         key_1 = answer_keys_1[i]
#         key_2 = answer_keys_2[i]
# 
#         data = data[data.find(key_1) + len(key_1):]
#         answer = data[:data.find(key_2)].replace("&amp;", "&")
# 
#         # If the answer seems reasonable
#         if len(answer) < 1000:
#             found = True
#             print(answer)
#             break
# 
#     if not found:
#         # Make a second guess in case no results were found
#         data = str(soup)
#         shortest_answer = ""
#         while data.find(wiki_key_1) != -1:
#             data = data[data.find(wiki_key_1) + len(wiki_key_1):]
#             answer = data[:data.find(wiki_key_2)].replace("&amp;", "&").replace(" - Wikipedia", "")
# 
#             if shortest_answer == "" or len(answer) < len(shortest_answer):
#                 shortest_answer = answer
#                 found = True
# 
#         if found:
#             print(shortest_answer)
#         else:
#             print("I couldn't find an answer :(")

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


def respond():
        # Get the question, format it into a Google search
    question = entry1.get()
    words = question.split(' ')
    question = ""
    for word in words:
        question += word + "+"
    question = question[:-1]

    # Get all of the HTML code from the website
    URL = "https://www.google.com/search?q=" + question + "&rlz=1C1CHBF_enUS892US892&oq=what+day+is+it&aqs=chrome.0" \
                                                          ".0i512l4j0i131i433j0i512l5.7446j0j1&sourceid=chrome&ie=UTF-8"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html5lib')

    answer_keys_1 = ["<div class=\"BNeawe iBp4i AP7Wnd\"><div><div class=\"BNeawe iBp4i AP7Wnd\">",
                     "<div class=\"BNeawe s3v9rd AP7Wnd\"><span class=\"atOwb UMOHqf\">",
                     ]
    answer_keys_2 = ["</div>", "</span", "</div>"]
    wiki_key_1 = "<h3 class=\"zBAuLc l97dzf\"><div class=\"BNeawe vvjwJb AP7Wnd\">"
    wiki_key_2 = "</div>"

    found = False

    if question.lower() != 'q' and question.lower() != "quit":
        # Try a range of techniques
        for i in range(0, len(answer_keys_1)):
            data = str(soup)

            key_1 = answer_keys_1[i]
            key_2 = answer_keys_2[i]

            data = data[data.find(key_1) + len(key_1):]
            answer = data[:data.find(key_2)].replace("&amp;", "&")

            # If the answer seems reasonable
            if len(answer) < 1000:
                found = True
                #label2 = Label(root, text=answer).pack()
                #canvas1.create_window(200, 180, window=label2)
                currAnswer.set(answer)
                break

        if not found:
            # Make a second guess in case no results were found
            data = str(soup)
            shortest_answer = ""
            while data.find(wiki_key_1) != -1:
                data = data[data.find(wiki_key_1) + len(wiki_key_1):]
                answer = data[:data.find(wiki_key_2)].replace("&amp;", "&").replace(" - Wikipedia", "")

                if shortest_answer == "" or len(answer) < len(shortest_answer):
                    shortest_answer = answer
                    found = True

            if found:
                #print(shortest_answer)
                #label2 = Label(root, text=shortest_answer).pack()
                #canvas1.create_window(200, 180, window=label2)

                currAnswer.set(shortest_answer)
                
            else:
                print("I couldn't find an answer :(")
                
text = Label(root, text="Enter a question:",
        fg = "#6b3e2e",
        bg = "light blue",
        font=("Georgia", 60)
).place(
    relx = 0.5,
    rely = .05,
    anchor = 'center')


button1 = Button(text='Search!', command=respond)
canvas1.create_window(200, 180, window=button1)
button1.place(relx = .5, rely = .2, anchor = 'center')

 
label2 = Label(root, textvariable=currAnswer).pack()
canvas1.create_window(200, 180, window=label2)

img = ImageTk.PhotoImage(Image.open("botson.png"))
label = Label(root, image = img)
label.pack()


root.mainloop()
    
