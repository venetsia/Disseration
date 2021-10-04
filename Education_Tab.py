import random
import tkinter as tk
import numpy as np
from PIL import ImageTk
import train_chat_BOT

import NEAT_Single_Processing
import train_chat_BOT

AI_tab = ["label1"]
AI_categories_tab = ["label2"]
label1 =""
label2 =""
agent_label1 =""
clicks = 0
chat_bot_dynamic_learn =""
response_enter =""
chatbot_next =""
class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def hide_old_widgets(self, widget):
        widget.grid_remove()
        return
    def next_button(self, chat_bot_dynamic_learn, response_enter, educatuin_tab):
        global agent_label1
        input = response_enter.get("1.0", tk.END)
        response_enter.delete('1.0', tk.END)
        results = train_chat_BOT.model.predict([train_chat_BOT.bag_of_words(input, train_chat_BOT.words)])[0]
        results_index = np.argmax(results)
        tag = train_chat_BOT.classes[results_index]
        if results[results_index] > 0.7:
            for tg in train_chat_BOT.intents["intents"]:
                if tg["tag"] == tag:
                    responses = tg["responses"]
            if tag =="evaluate":
                image_agent = ImageTk.PhotoImage(file="agent.png")
                agent_label1 = tk.Label(educatuin_tab, image=image_agent)
                agent_label1.image = image_agent
                agent_label1.grid(row=1, column=1)
                agent_label1.config(fg="grey75", bg="grey75")
            elif tag != "evaluate":
                if agent_label1 != "":
                    self.hide_old_widgets(agent_label1)
                    #chat_bot_dynamic_learn.window_create(tk.END, window = tk.Label(chat_bot_dynamic_learn, image = img_agent))
            chat_bot_dynamic_learn.insert(tk.END,"You: " + input + "Agent: " + random.choice(responses) + "\n")
        else:
            chat_bot_dynamic_learn.insert(tk.END,"I didn't get that, try again please.")
    def nada(self):
       return
    def load_content(self,education_option_selected,educatuin_tab):
        selected_indices = education_option_selected.curselection()
        value = education_option_selected.get(selected_indices[0])
        global label1
        global label2
        global chat_bot_dynamic_learn
        global response_enter
        global chatbot_next
        if value == "Artificial Intelligence":
            if label2 != "":
                self.hide_old_widgets(label2)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            image1 = ImageTk.PhotoImage(file = "AI-Intro.png")
            label1 = tk.Label(educatuin_tab, image=image1)
            label1.image = image1
            label1.grid(row=1,column = 0)
            label1.config(fg="grey75", bg="grey75")
        elif value == "AI categories":
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            image2 = ImageTk.PhotoImage(file="AI_second.png")
            label2 = tk.Label(educatuin_tab, image=image2)
            label2.image = image2
            label2.grid(row=1, column=0)
            label2.config(fg="grey75", bg="grey75")
        elif value == "Intelligent Agents":
            if label1 != "":
                self.hide_old_widgets(label1)
            if label2 != "":
                self.hide_old_widgets(label2)
            chat_bot_dynamic_learn = tk.Text(educatuin_tab, name="chat_bot_dynamic_learn", height=50, width=70)
            chat_bot_dynamic_learn.grid(row=1, column=0, sticky=tk.W)
            response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
            response_enter.grid(row=2, column=0, sticky=tk.W)
            chat_bot_dynamic_learn.bind('<Key>', lambda e: 'break')
            chat_bot_dynamic_learn.insert(tk.END, "Welcome, I am a chat bot and I am here to answer some questions.\nFor this specific tab you may want to ask questions such as:"
                                                  "\n\"What is an agent?\"\n\"How and when do we evauate an agent?\"\nYou can refer back to this whenever you would like to ask a question. I am trained in answering a few questions.\n")
            # Run button for Neat using a thread
            chatbot_next = tk.Button(educatuin_tab, text="Send",
                                     command=lambda : self.next_button(chat_bot_dynamic_learn, response_enter, educatuin_tab),
                                     justify=tk.LEFT, anchor="w")
            chatbot_next.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

def Activate_Content(education_option_selected, educatuin_tab):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab)

    education_option_selected.bind('<<ListboxSelect>>', load_content)