import tkinter as tk


from main import TextEditor


class Validate(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self,text, label, isLightMode):
        bg = isLightMode.lookup('TFrame', 'background')
        if text._name == "fitness_criterion":
            value = text.get()
            if (value == "max" or value =="min" or value =="mean"):
                if str(bg) == "grey75":
                    print(bg)
                    label.config(fg = "black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("")
                label.config(fg="red")
        else:
            print("not digit")
            print(text)
            print(text._name)


def ValidateInput(widget, text, label, isLightMode):
    toolTip = Validate(widget)
    def leave(event):
        toolTip.validate_spinbox(text, label, isLightMode)
    widget.bind('<FocusOut>', leave)
