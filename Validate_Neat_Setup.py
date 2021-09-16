import re

games_available = ['SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0","Breakout-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo"]
game_evaluation_choice = ["Single-Processing", "Multi-Processing"]
class Validate_Neat(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self,widget_name, text,label, style, widget):
        bg = style.lookup('TFrame', 'background')
        if widget_name == "game_selection":
            if text in games_available:
                if str(bg) == "grey75":
                    print(bg)
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                label.config(fg="red")
        if widget_name == "game_evaluation":
            if text in game_evaluation_choice:
                if str(bg) == "grey75":
                    print(bg)
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("")
                label.config(fg="red")

def ValidateInput(widget, label, style):
    toolTip = Validate_Neat(widget)
    widget_name = widget._name
    text = widget.get()
    def leave(event):
        toolTip.validate_spinbox(widget_name, text,label, style, widget)

    widget.bind('<FocusOut>', leave)