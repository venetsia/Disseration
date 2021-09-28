import re
import sys
from tkinter import END
import atari_py
import gym

games_available = ['SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0","Breakout-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo"]
game_evaluation_choice = ["Single-Processing", "Multi-Processing"]
network_type_choice = ["Feed-forward", "Recurrent"]
render_window_choice = ["True", "False"]
choose_config_file_choice = ["From Text Editor", "Choose file from directory"]
game_list = atari_py.list_games()

class Validate_Neat(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self,widget_name,label, style, widget):
        sys.__stdout__
        sys.__stderr__
        text = widget.get()
        bg = style.lookup('TFrame', 'background')
        if widget_name == "game_selection":
            if str(text) in games_available:
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                label.config(fg="red")
        if widget_name == "game_evaluation":
            if str(text) in game_evaluation_choice:
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "network_type":
            if text in network_type_choice:
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "render_window":
            if text in render_window_choice:
                if str(bg) == "grey75":
                    print(bg)
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "choose_config_file":
            if text in choose_config_file_choice:
                if str(bg) == "grey75":
                    print(bg)
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "game_checkpoint":
            if text.find("-") == 0:
                text = text.replace("-", "")
            if text == "":
                label.config(fg="red")
                return
            if re.search('[a-zA-Z]', text):
                widget.set("")
                label.config(fg="red")
                return
            if text.isdigit():
                if int(text) > 0:
                    widget.set(int(text))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                elif int(text) == 0:
                    widget.set("0")
                else:
                    widget.set("")
                    label.config(fg="red")
            else:
                if float(text) or text == "0.0":
                    widget.set(int(float(text)))
                else:
                    widget.set("")
                    label.config(fg="red")

    def validate_spinbox_game(self, widget_name, label, style, widget, input, output):
        text = widget.get()
        if widget_name == "game_selection_config":
            try:
                env = gym.make(text)
                output.set(env.action_space)
                if text in game_list:
                    input.set("1092")
            except:
                print("Error")
def ValidateInputNEAT(widget, label, style):
    toolTip = Validate_Neat(widget)
    widget_name = widget._name

    def leave(event):
        toolTip.validate_spinbox(widget_name,label, style, widget)

    widget.bind('<FocusOut>', leave)
def Validate_Gym_Game(widget, label, style, input, output):
    toolTip = Validate_Neat(widget)
    widget_name = widget._name

    def leave(event):
        toolTip.validate_spinbox_game(widget_name, label, style, widget, input, output)

    widget.bind('<FocusOut>', leave)



