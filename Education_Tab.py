import random
import tkinter as tk
import numpy as np
from PIL import ImageTk

import CreateHelpMessage
import train_chat_BOT
import enum
import NEAT_Single_Processing
import train_chat_BOT
education_mode_labels = ["label1", "label2", "chat_bot_dynamic_learn"]
AI_tab = ["label1"]
AI_categories_tab = ["label2"]
label1 =""
label2 =""
agent_label1 =""
clicks = 0
chat_bot_dynamic_learn =""
response_enter =""
chatbot_next =""
neuron_tab_pic = ""
neuron_tab_label =""
perceptron_image = ""
perceptron_label = ""
check_answer = ""
Introduction_tab = False
Artificial_intelligence_tab = False
AI_Categories_tab = False
Intelligent_Agents_tab = False
Neuron_tab = False
Perceptron_tab = False
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
    def check_answer(self,value,widget):
        input = widget.get("1.0", tk.END)
        input = input.lower()
        if value == "Neural Network":
            if input in "hidden layer" or input.lower() in "hidden-layer" or input.find("hidden-layer") == 0 or input.find("hidden layer") == 0:
                widget.config(bg="green")
            else:
                widget.config(bg="red")
        elif value == "Learning Types":
            if input.find("reinforcement learning (rl)") == 0 or input.find("reinforcement learning (rl)") == 0 or input.find("reinforcement learning") == 0 or input.find("reinforcement learning") == 0 or input.find("rl") == 0 or input.find("rl") == 0 or input.find("reinforcement") == 0 or input.find("reinforcement") == 0 :
                widget.config(bg="green")
            else:
                widget.config(bg="red")
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
        global  Artificial_intelligence_tab
        global AI_Categories_tab
        global Intelligent_Agents_tab
        global neuron_tab_pic
        global neuron_tab_label
        global perceptron_image
        global perceptron_label
        global Neuron_tab
        global check_answer
        if value == "Artificial Intelligence":
            Artificial_intelligence_tab = True
            if label2 != "":
                self.hide_old_widgets(label2)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if neuron_tab_label != "":
                self.hide_old_widgets(neuron_tab_label)
            image1 = ImageTk.PhotoImage(file = "AI-Intro.png")
            label1 = tk.Label(educatuin_tab, image=image1)
            label1.image = image1
            label1.grid(row=1,column = 0)
            label1.config(fg="grey75", bg="grey75")
        elif value == "AI categories":
            if Artificial_intelligence_tab == True:
                AI_Categories_tab = True
                if label1 != "":
                    self.hide_old_widgets(label1)
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                image2 = ImageTk.PhotoImage(file="AI_second.png")
                label1 = tk.Label(educatuin_tab, image=image2)
                label1.image = image2
                label1.grid(row=1, column=0)
                label1.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text = "Please refer to Artificial Intelligence lesson first", font = ("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Intelligent Agents":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True:
                Intelligent_Agents_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if neuron_tab_pic != "":
                    self.hide_old_widgets(neuron_tab_pic)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
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
                CreateHelpMessage.CreateToolTip_For_Education_Mode(response_enter, "Dear User, Welcome to intelligent agents lessen. This chat bot is an intelligent agent trained by a neural network. We will look into this next. For now we will see what an agent is by answering two questions. You can refer back to this chat as it was trained to recognise some topics and answer some questions.")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text = "Please refer to AI categories lesson first", font = ("Courier", 20, "bold") )
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Neuron":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True:
                Neuron_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                neuron_tab_pic = ImageTk.PhotoImage(file="biological_neuron.png")
                neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
                neuron_tab_label.image = neuron_tab_pic
                neuron_tab_label.grid(row=1, column=1)
                neuron_tab_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text="Please refer to AI categories lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Neural Network":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and Neuron_tab == True:
                Perceptron_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                perceptron_image = ImageTk.PhotoImage(file="percepron.png")
                perceptron_label = tk.Label(educatuin_tab, image=perceptron_image)
                perceptron_label.image = perceptron_image
                perceptron_label.grid(row=1, column=0)
                perceptron_label.config(fg="grey75", bg="grey75")
                response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
                response_enter.grid(row=2, column=0, sticky=tk.W)
                # Run button for Neat using a thread
                check_answer = tk.Button(educatuin_tab, text="Check answer",
                                         command=lambda: self.check_answer(value,response_enter),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text="Please refer to AI categories lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Learning Types":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            neuron_tab_pic = ImageTk.PhotoImage(file="Types_of_learning.png")
            neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
            neuron_tab_label.image = neuron_tab_pic
            neuron_tab_label.grid(row=1, column=0)
            neuron_tab_label.config(fg="grey75", bg="grey75")
            response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
            response_enter.grid(row=2, column=0, sticky=tk.W)
            # Run button for Neat using a thread
            check_answer = tk.Button(educatuin_tab, text="Check answer",
                                     command=lambda: self.check_answer(value,response_enter),
                                     justify=tk.LEFT, anchor="w")
            check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        elif value == "Components of a neural network":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            neuron_tab_pic = ImageTk.PhotoImage(file="Components_of_Neural_Network.png")
            neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
            neuron_tab_label.image = neuron_tab_pic
            neuron_tab_label.grid(row=1, column=0)
            neuron_tab_label.config(fg="grey75", bg="grey75")

def Activate_Content(education_option_selected, educatuin_tab):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab)

    education_option_selected.bind('<<ListboxSelect>>', load_content)
def DarkMode():
    for education_label in education_mode_labels:
        try:
            exec(education_label + '.config(bg = "grey75")')
        except:
            pass