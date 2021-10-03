import tkinter as tk

from PIL import ImageTk


class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def nada(self):
       return
    def load_content(self,education_option_selected,educatuin_tab):
        selected_indices = education_option_selected.curselection()
        value = education_option_selected.get(selected_indices[0])
        if value == "Artificial Intelligence":
            image1 = ImageTk.PhotoImage(file = "AI.png")
            label1 = tk.Label(educatuin_tab, image=image1)
            label1.image = image1
            label1.grid(row=1,column = 0)
            label1.config(fg="#272726", bg="#9bdbae")


def Activate_Content(education_option_selected, educatuin_tab):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab)

    education_option_selected.bind('<<ListboxSelect>>', load_content)