import tkinter as tk


from main import TextEditor


class Validate(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self,text):
        if text.get() == "max":
            print("ok")
        else:
            print("not digit")
            print(text)
            print(text._name)


def ValidateInput(widget, text):
    toolTip = Validate(widget)
    def enter(event):
        toolTip.validate_spinbox(text)
    def leave(event):
        toolTip.validate_spinbox(text)
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

