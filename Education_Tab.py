import tkinter as tk

from PIL import ImageTk


import NEAT_Single_Processing

AI_tab = ["label1"]
AI_categories_tab = ["label2"]
label1 =""
label2 =""
clicks = 0
class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def hide_old_widgets(self, widget):
        widget.grid_remove()
    def next_button(self, chat_bot_dynamic_learn):
        global clicks
        if clicks == 0:
            clicks += 1
            chat_bot_dynamic_learn.insert(tk.END, "Q: What is an agent?\n")
        if clicks == 1:
            clicks += 1
            chat_bot_dynamic_learn.insert(tk.END, "A: Anything that can be viewed as perceiving its environment though sensors and acting upon that environment though effectors.\n")
        return clicks
    def nada(self):
       return
    def load_content(self,education_option_selected,educatuin_tab):
        selected_indices = education_option_selected.curselection()
        value = education_option_selected.get(selected_indices[0])
        global label1
        global label2
        if value == "Artificial Intelligence":
            if label2 != "":
                self.hide_old_widgets(label2)
            image1 = ImageTk.PhotoImage(file = "AI-Intro.png")
            label1 = tk.Label(educatuin_tab, image=image1)
            label1.image = image1
            label1.grid(row=1,column = 0)
            label1.config(fg="grey75", bg="grey75")
        elif value == "AI categories":
            if label1 != "":
                self.hide_old_widgets(label1)
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
            chat_bot_dynamic_learn = tk.Text(educatuin_tab, name="chat_bot_dynamic_learn", height=50, width=150)
            chat_bot_dynamic_learn.grid(row=1, column=0, sticky=tk.W)
            response_enter = tk.Text(educatuin_tab, name="response_enter", height=5, width=150)
            response_enter.grid(row=2, column=0, sticky=tk.W)
            # Run button for Neat using a thread
            chatbot_next = tk.Button(educatuin_tab, text="Understood",
                                     command=lambda : self.next_button(chat_bot_dynamic_learn),
                                     justify=tk.LEFT, anchor="w")
            chatbot_next.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

def Activate_Content(education_option_selected, educatuin_tab):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab)

    education_option_selected.bind('<<ListboxSelect>>', load_content)