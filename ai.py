# NAME: ai.py
# PURPOSE: the brain of the trivia bot!
# AUTHORS: Reid Baris and Emma Bethel


from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import os


class Botson:
    def respond(self, question):
        raise NotImplementedError("Trivia bots need a response function!")


# created by Reid Baris, w/ minor refactoring from Emma Bethel
class WebScraperBotson(Botson):
    def respond(self, question):
        words = question.split(' ')
        question_reformatted = ""
        for word in words:
            question_reformatted += word + "+"
        question_reformatted = question[:-1]

        # Get all of the HTML code from the website
        URL = "https://www.google.com/search?q=" + question_reformatted + "&rlz=1C1CHBF_enUS892US892&oq=what+day+is+it&aqs=chrome.0" \
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
                    return answer

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

                    return answer
                    
                else:
                    return "I couldn't find an answer :("


# created by Emma Bethel
class GptBotson(Botson):
    def __init__(self):
        api_key = os.environ.get('OPENAI_API_KEY')
        if api_key is None:
            raise Exception("No OpenAI API key set!")
    
        self.client = OpenAI(api_key=api_key)

    def respond(self, question):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"In 3 words or less, {question}"}]
        )

        return response.choices[0].message.content

