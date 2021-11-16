import tkinter as tk
import random
import re
from main import TextEditor
activation_options_list = ['abs', 'clamped', 'cube','exp', 'gauss',
                                'hat','identity', 'inv', 'log','relu','elu',
                                'lelu','selu', 'sigmoid','sin', 'softplus', 'square', 'tanh']
aggregation_options_list=['sum','product', 'min', 'max', 'mean', 'median', 'maxabs']

response_weight_bias_types = ['gaussian', 'normal', 'uniform']

list_response_weight_bias = ["enabled_rate_to_true_add","enabled_rate_to_false_add","enabled_rate_to_false_add","compatibility_weight_coefficient","compatibility_threshold","compatibility_disjoint_coefficient","bias_init_mean","bias_init_stdev", "bias_max_value", "bias_min_value" ,"bias_mutate_power","bias_mutate_rate" ,"bias_replace_rate","response_init_stdev","response_max_value", "response_min_value",
                             "response_mutate_power" ,"response_mutate_rate" ,"response_replace_rate", "response_init_mean" , "weight_init_mean","weight_init_stdev",
                             "weight_max_value","weight_min_value" ,"weight_mutate_power", "weight_mutate_rate","weight_replace_rate"]

class Validate(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self, text, label, isLightMode):
        bg = isLightMode.lookup('TFrame', 'background')
        if text._name != "activation_option":
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
            if value == "":
                label.config(fg="red")
                return
            # value = text.get()
            print(value.isdigit())
            print(len(value) if len(value) > 0 else "no")
            if value == "0" or value == "0.0":
                label.config(fg="black")
                return
            if re.search('[a-zA-Z]', value):
                text.set("")
                label.config(fg="red")
                return
            try:
                if value.find("-") == 0:
                    temp_value = value.replace("-", "")
                    if int(temp_value):
                        print("Int with minus")
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
                    elif float(temp_value):
                        print("Float with minus")
                        temp_value = float(temp_value)
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
                else:
                    if value.isdigit():
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
                    elif float(value):
                        text.set(float(value))
                        if str(bg) == "grey75":
                            print(bg)
                            label.config(fg="black")
                        else:
                            print(bg)
                            label.config(fg="white")
                    else:
                        text.set("")
                        label.config(fg="red")
            except ValueError:
                try:
                    if float(value):
                        print("Float with minus")
                        temp_value = float(value)
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
                except ValueError:
                    text.set("")
                    label.config(fg="red")
        elif text._name == "no_fitness_termination"  or text._name == "enabled_default" or text._name =="single_structural_mutation":
            if value == "True" or value == "False":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("False")
                #label.config(fg="red")
        elif text._name == "structural_mutation_surer":
            if value == "True" or value == "False":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                text.set("default")
                # label.config(fg="red")
        elif text._name == "reset_on_extinction" or text._name == "feed_forward":
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
            if value == "0":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
                return
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
            if value =="0" or value == "0.0":
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
                return
            if value.find("-") == 0:
                value = value.replace("-", "")
            print(value)
            try:
                if float(value):
                    print("In first if: " + str(float(value)))
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
        elif text._name == "initial_connection_value" or text._name == "activation_mutate_rate" \
                or text._name == "aggregation_mutate_rate" or text._name =="node_add_prob" or text._name =="node_delete_prob"\
                or text._name == "enabled_mutate_rate" or text._name == "conn_add_prob" or text._name == "conn_delete_prob":
            print(text._name)
            value = text.get()
            if value == "0" or value == "0.0":
                if str(bg) == "grey75":
                    # print("In third if")
                    label.config(fg="black")
                else:
                    # print(bg)
                    label.config(fg="white")
                value.set("0.0")
                return
            if value.find("-") == 0:
                value = value.replace("-", "")
            #print(value + " Not in try")
            try:
                #print("In try statement")
                if float(value):
                    #print("In first if")
                    value = float(value)
                    if isinstance(value, float) and (1.0 >= value >= 0.0):
                        #print("In second if")
                        text.set(float(value))
                        if str(bg) == "grey75":
                            #print("In third if")
                            label.config(fg="black")
                        else:
                            #print(bg)
                            label.config(fg="white")
                    else:
                        text.set("")
                        label.config(fg="red")
                elif value == "0.0":
                    text.set("0.0")
                    if str(bg) == "grey75":
                        #print("In forth if")
                        label.config(fg="black")
                    else:
                        #print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
            except ValueError:
                print("Exception")
                if  value == "0.0":
                    text.set("0.0")
                    if str(bg) == "grey75":
                        #print("In third if")
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="red")
                # make for bias_init_type and response_init_type and weight_init_type
        elif text._name in list_response_weight_bias:
            minus_detected = False
            if value.find("-") == 0:
                tempvalue = value.replace("-", "")
                minus_detected = True
            else:
                tempvalue = value
            try:
                if float(tempvalue):
                    #print("In first if: " + str(float(value)))
                    #print(minus_detected)
                    if minus_detected is True:
                        #print("WTF")
                        text.set("-" + str(float(tempvalue)))
                    else:
                        #print("WHAT")
                        text.set(float(tempvalue))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                elif value == "0.0" or  value == "0":
                    #print("here")
                    if str(bg) == "grey75":
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
        elif text._name == "bias_init_type" or text._name == "weight_init_type" or text._name == "response_init_type":
            #print("wtf1")
            if value in response_weight_bias_types:
                #print("WTF2")
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    print(bg)
                    label.config(fg="white")
            else:
                #print("WTF3")
                text.set("gaussian")
        else:
            print("not digit")
            print(text)
            print(text._name)

    def validate_spinbox_with_Random(self, text,label,isLightMode, random_Enabled):
        bg = isLightMode.lookup('TFrame', 'background')
        value = text.get()
        random_Enabled_value = random_Enabled.get()
        if random_Enabled_value == "True":
            if text._name == "activation_default":
                if (value == "abs" or value == "clamped" or value == "cube" or
                        value == "exp" or value == "hat" or value == "identity" or
                        value == "inv" or value == "log" or value == "relu" or
                        value == "elu" or value == "lelu" or value == "selu" or
                        value == "sigmoid" or value == "sin" or value == "softplus" or
                        value == "square" or value == "tanh"):
                    if str(bg) == "grey75":
                        print(bg)
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set(random.choice(activation_options_list))
                    label.config(fg="blue")
            if text._name == "aggregation_default":
                if (value == "sum" or value == "product" or value == "min" or
                        value == "max" or value == "mean" or value == "median" or
                        value == "maxabs"):
                    if str(bg) == "grey75":
                        print(bg)
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set(random.choice(aggregation_options_list))
                    label.config(fg="blue")
        else:
            if text._name == "activation_default":
                if (value == "abs" or value == "clamped" or value == "cube" or
                        value == "exp" or value == "hat" or value == "identity" or
                        value == "inv" or value == "log" or value == "relu" or
                        value == "elu" or value == "lelu" or value == "selu" or
                        value == "sigmoid" or value == "sin" or value == "softplus" or
                        value == "square" or value == "tanh"):
                    if str(bg) == "grey75":
                        print(bg)
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="blue")
            if text._name == "aggregation_default":
                if (value == "sum" or value == "product" or value == "min" or
                        value == "max" or value == "mean" or value == "median" or
                        value == "maxabs"):
                    if str(bg) == "grey75":
                        print(bg)
                        label.config(fg="black")
                    else:
                        print(bg)
                        label.config(fg="white")
                else:
                    text.set("")
                    label.config(fg="blue")

def ValidateInput(widget, text, label, isLightMode):
    toolTip = Validate(widget)

    def leave(event):
        toolTip.validate_spinbox(text, label, isLightMode)

    widget.bind('<FocusOut>', leave)

def ValidateInputWithRandom(widget, text, label, isLightMode, random_Enabled):
    toolTip = Validate(widget)

    def leave(event):
        toolTip.validate_spinbox_with_Random(text, label, isLightMode, random_Enabled)

    widget.bind('<FocusOut>', leave)