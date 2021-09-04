import tkinter as tk

from main import TextEditor


class Validate(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self, text, label, isLightMode):
        bg = isLightMode.lookup('TFrame', 'background')
        value = text.get()
        if text._name == "fitness_criterion":
            # value = text.get()
            if (value == "max" or value == "min" or value == "mean"):
                if str(bg) == "grey75":
                    print(bg)
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("")
                label.config(fg="red")
        elif text._name == "fitness_threshold":
            # value = text.get()
            print(value.isdigit())
            print(len(value) if len(value) > 0 else "no")
            if value.find("-") == 0:
                temp_value = value.replace("-", "")
                if int(temp_value):
                    if temp_value.isdigit():
                        temp_value = int(temp_value)
                        text.set("-" + str(temp_value))
                        if str(bg) == "grey75":
                            print(bg)
                            label.config(fg="black")
                        else:
                            print(bg)
                            label.config(fg="white")
                    else:
                        text.set("")
                        label.config(fg="red")
            elif value.isdigit():
                if int(value):
                    text.set(int(value))
                    if str(bg) == "grey75":
                        print(bg)
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
        elif text._name == "no_fitness_termination" or text._name == "reset_on_extinction":
            if value == "True" or value == "False":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("")
                label.config(fg="red")
        elif text._name == "pop_size":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
            else:
                text.set("")
                label.config(fg="red")
        elif text._name == "species_fitness_func":
            if value == "max" or value == "min" or value == "mean" or  value == "median":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("mean")
        elif text._name == "max_stagnation":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("15")
            else:
                text.set("15")
        elif text._name == "species_elitism":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("0")
            else:
                text.set("0")
        elif text._name == "elitism":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("0")
            else:
                text.set("0")
        elif text._name == "survival_threshold":
            if value.find("-") == 0:
                value = value.replace("-", "")
            print(value)
            try:
                if float(value):
                    value = float(value)
                    if isinstance(value, float):
                        text.set(float(value))
                        if str(bg) == "grey75":
                            label.config(fg="black")
                        else:
                            print(bg)
                            label.config(fg="white")
                    else:
                        text.set("0.2")
            except ValueError:
                text.set("0.2")
            else:
                text.set("0.2")
        elif text._name == "min_species_size":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("2")
            else:
                text.set("2")
        elif text._name == "num_inputs":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
            else:
                text.set("")
                label.config(fg="red")
        elif text._name == "num_outputs":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
            else:
                text.set("")
                label.config(fg="red")
        elif text._name == "num_hidden":
            if value.find("-") == 0:
                value = value.replace("-", "")
            if value.isdigit():
                if int(value) > 0:
                    text.set(int(value))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
            else:
                text.set("")
                label.config(fg="red")
        elif text._name == "initial_connection":
            if value == "unconnected" or value == "fs_neat_nohidden"\
                    or value == "fs_neat_hidden" or value == "full_nodirect" \
                    or value == "full_direct" or  value == "partial_direct" or  value == "partial_nodirect":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("unconnected")
        elif text._name == "initial_connection_value":
            print(text._name)
            value = text.get()
            if value.find("-") == 0:
                value = value.replace("-", "")
            print(value + " Not in try")
            try:
                print("In try statement")
                if float(value):
                    print("In first if")
                    value = float(value)
                    if isinstance(value, float) and (1.0 >= value >= 0.0):
                        print("In second if")
                        text.set(float(value))
                        if str(bg) == "grey75":
                            print("In third if")
                            label.config(fg="black")
                        else:
                            print(bg)
                            label.config(fg="white")
                    else:
                        text.set("")
                        label.config(fg="red")
                elif value.find("0.0"):
                    text.set("0.0")
                    if str(bg) == "grey75":
                        print("In third if")
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
            except ValueError:
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
