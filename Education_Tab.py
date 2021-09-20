import tkinter as tk

class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def load_content(self,education_option_selected,educatuin_tab):
        print("Test")


def Activate_Content(education_option_selected, educatuin_tab):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab)

    education_option_selected.bind('<<ListboxSelect>>', load_content)