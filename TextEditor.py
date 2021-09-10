import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, LEFT, VERTICAL
from tkinter import ttk, INSERT
from tkinter.font import BOLD
from tkinter.messagebox import showinfo
import CreateHelpMessage
from ttkthemes import ThemedStyle

import ValidateInput
import Build_in_Console

text_editor = ("[NEAT]\nfitness_criterion = \nfitness_threshold = \nno_fitness_termination = \n"
               "pop_size = \nreset_on_extinction = \n\n"
               "[DefaultStagnation]\nspecies_fitness_func = \n"
               "max_stagnation = \nspecies_elitism = \n\n"
               "[DefaultReproduction]\n"
               "elitism = \nsurvival_threshold = \nmin_species_size = \n\n"
               "[DefaultGenome]\n"
               "# Activation options\n"
               "activation_default = \n"
               "activation_mutate_rate = \nactivation_options = \n\n"
               "# Aggregation options\naggregation_default = \n"
               "aggregation_mutate_rate = \naggregation_options = \n\n"
               "# Bias options\nbias_init_mean = \n"
               "bias_init_stdev = \nbias_init_type = \nbias_max_value = \n"
               "bias_min_value = \nbias_mutate_rate = \nbias_replace_rate = \n\n"
               "# Compatibility options\n"
               "compatibility_threshold = \ncompatibility_disjoint_coefficient = \n"
               "compatibility_weight_coefficient = \n\n"
               "# Connection options\nconn_add_prob = \n"
               "conn_delete_prob = \nenabled_default = \nenabled_mutate_rate = \n"
               "enabled_rate_to_false_add = \nenabled_rate_to_true_add = \nnode_add_prob = \n"
               "node_delete_prob =\n\n"
               "# Network parameters\nfeed_forward = \n"
               "initial_connection = \nnum_hidden = \nnum_inputs = \nnum_outputs = \n\n"
               "# Response options\nresponse_init_mean = \nresponse_init_stdev = \nresponse_init_type = \n"
               "response_max_value = \nresponse_min_value = \nresponse_mutate_power = \n"
               "response_mutate_rate = \nresponse_replace_rate = \n\n"
               "# Structure options\nsingle_structural_mutation = \nstructural_mutation_surer = \n\n"
               "# Weight options\nweight_init_mean = \nweight_init_stdev = \nweight_init_type = \nweight_max_value = \n"
               "weight_min_value = \nweight_mutate_power = \nweight_mutate_rate = \n"
               "weight_replace_rate = \n")
default_text_editor = ("[NEAT]\nfitness_criterion = \nfitness_threshold = \nno_fitness_termination = False\n"
               "pop_size = \nreset_on_extinction = \n\n"
               "[DefaultStagnation]\nspecies_fitness_func = mean\n"
               "max_stagnation = 15\nspecies_elitism = 0\n\n"
               "[DefaultReproduction]\n"
               "elitism = 0\nsurvival_threshold = 0.2\nmin_species_size = 0.2\n\n"
               "[DefaultGenome]\n"
               "# Activation options\n"
               "activation_default = \n"
               "activation_mutate_rate = \nactivation_options = sigmoid\n\n"
               "# Aggregation options\naggregation_default = \n"
               "aggregation_mutate_rate = \naggregation_options = sum\n\n"
               "# Bias options\nbias_init_mean = \n"
               "bias_init_stdev = \nbias_init_type = \nbias_max_value = \n"
               "bias_min_value = \nbias_mutate_rate = \nbias_replace_rate = \n\n"
               "# Compatibility options\n"
               "compatibility_threshold = \ncompatibility_disjoint_coefficient = \n"
               "compatibility_weight_coefficient = \n\n"
               "# Connection options\nconn_add_prob = \n"
               "conn_delete_prob = \nenabled_default = \nenabled_mutate_rate = \n"
               "enabled_rate_to_false_add = \nenabled_rate_to_true_add = \nnode_add_prob = \n"
               "node_delete_prob =\n\n"
               "# Network parameters\nfeed_forward = \n"
               "initial_connection = unconnected\nnum_hidden = \nnum_inputs = \nnum_outputs = \n\n"
               "# Response options\nresponse_init_mean = \nresponse_init_stdev = \nresponse_init_type = gaussian\n"
               "response_max_value = \nresponse_min_value = \nresponse_mutate_power = \n"
               "response_mutate_rate = \nresponse_replace_rate = \n\n"
               "# Structure options\nsingle_structural_mutation = False\nstructural_mutation_surer = default\n\n"
               "# Weight options\nweight_init_mean = \nweight_init_stdev = \nweight_init_type = gaussian\nweight_max_value = \n"
               "weight_min_value = \nweight_mutate_power = \nweight_mutate_rate = \n"
               "weight_replace_rate = \n")
labels_list = ["neat_section_L", "fitness_criterion_l", "fitness_threshold_l", "no_fitness_termination_l", "pop_size_l",
               "reset_on_extinction_L", "default_stagnation_l", "species_fitness_func_l", "max_stagnation_l",
               "species_elitism_l",
               "default_reproduction_l", "elitism_l", "survival_threshold_l", "min_species_size_l", "genome_Section_l",
               "network_Parameters_l",
               "num_inputs_l", "num_outputs_l", "num_hidden_l", "initial_connection_L", "initial_conection_value_l",
               "feed_forward_L",
               "activation_n_aggregation_o", "activation_default_L", "activation_mutate_rate_L", "activation_options_L",
               "aggregation_mutate_rate_L", "aggregation_default_L", "aggregation_options_L", "node_bias_o",
               "bias_init_mean_l", "bias_init_stdev_l"
    , "bias_init_type_l", "bias_max_value_l", "bias_min_value_l", "bias_mutate_power_l", "bias_mutate_rate_l",
               "bias_replace_rate_l",
               "genome_compatibility_o", "compatibility_threshold_l", "compatibility_disjoint_coefficient_l",
               "compatibility_weight_coefficient_l", "connection_options_l", "conn_add_prob_l", "conn_delete_prob_l",
               "enabled_default_L",
               "enabled_mutate_rate_l", "enabled_rate_to_false_add_l", "enabled_rate_to_true_add_l", "node_add_prob_l",
               "node_delete_prob_l",
               "response_l", "response_init_mean_l", "response_init_stdev_l", "response_init_type_L",
               "response_max_value_l",
               "response_min_value_l", "response_mutate_power_l", "response_mutate_rate_l", "response_replace_rate_l",
               "single_structural_mutation_L",
               "structural_mutation_surer_L", "weight_l", "weight_init_mean_l", "weight_init_stdev_l",
               "weight_init_type_L",
               "weight_max_value_l", "weight_min_value_l", "weight_mutate_power_l", "weight_mutate_rate_l",
               "weight_replace_rate_l", "random_from_form_l", "game_selection_l", "setup_neat_l", "winner_file_name_l", "game_evaluation_l", "game_checkpoint_l"]
buttons_list = ["btn_open", "btn_save", "reset_btn", "default_config_btn", "update_btn"]

form_values_list = ["fitness_criterion", "fitness_threshold", "no_fitness_termination", "pop_size",
                    "reset_on_extinction",
                    "species_fitness_func", "max_stagnation", "species_elitism", "survival_threshold", "elitism",
                    "min_species_size"
    , "num_inputs", "num_outputs", "num_hidden", "initial_connection", "initial_connection_value", "feed_forward",
                    "activation_default", "activation_mutate_rate", "aggregation_mutate_rate", "aggregation_default",
                    "bias_init_mean", "bias_init_stdev", "bias_init_type", "bias_max_value", "bias_min_value",
                    "bias_mutate_power", "bias_mutate_rate", "bias_replace_rate", "compatibility_threshold",
                    "compatibility_disjoint_coefficient",
                    "compatibility_weight_coefficient", "conn_add_prob", "conn_delete_prob", "enabled_default",
                    "enabled_mutate_rate",
                    "enabled_rate_to_false_add", "enabled_rate_to_true_add", "node_add_prob", "node_delete_prob",
                    "response_init_mean",
                    "response_init_stdev", "response_init_type", "response_max_value", "response_min_value",
                    "response_mutate_power",
                    "response_mutate_rate", "response_replace_rate", "single_structural_mutation",
                    "structural_mutation_surer", "weight_init_mean",
                    "weight_init_stdev", "weight_init_type", "weight_max_value", "weight_min_value",
                    "weight_mutate_power", "weight_mutate_rate",
                    "weight_replace_rate"]
form_Main_label_list = ["neat_section_L", "default_stagnation_l",
                        "default_reproduction_l", "genome_Section_l"]
form_sublabels_label_list = ["network_Parameters_l", "activation_n_aggregation_o",
                             "node_bias_o", "genome_compatibility_o",
                             "connection_options_l", "response_l",
                             "weight_l"]
neat_selection = ["fitness_criterion", "fitness_threshold", "no_fitness_termination", "pop_size", "reset_on_extinction"]
default_stagnation = ["species_fitness_func", "max_stagnation", "species_elitism"]
default_reproduction = ["elitism", "survival_threshold", "min_species_size"]
genome_section = ["num_inputs", "num_outputs", "num_hidden", "initial_connection", "initial_connection_value",
                  "feed_forward",
                  "activation_default", "activation_mutate_rate", "activation_options", "aggregation_mutate_rate",
                  "aggregation_default",
                  "aggregation_options", "bias_init_mean", "bias_init_stdev", "bias_init_type", "bias_max_value",
                  "bias_min_value",
                  "bias_mutate_power", "bias_mutate_rate", "bias_replace_rate", "compatibility_threshold",
                  "compatibility_disjoint_coefficient",
                  "compatibility_weight_coefficient", "conn_add_prob", "conn_delete_prob", "enabled_default",
                  "enabled_mutate_rate",
                  "enabled_rate_to_false_add", "enabled_rate_to_true_add", "node_add_prob", "node_delete_prob",
                  "response_init_mean",
                  "response_init_stdev", "response_init_type", "response_max_value", "response_min_value",
                  "response_mutate_power",
                  "response_mutate_power", "response_replace_rate", "single_structural_mutation",
                  "structural_mutation_surer", "weight_init_mean",
                  "weight_init_stdev", "weight_init_type", "weight_max_value", "weight_min_value",
                  "weight_mutate_power", "weight_mutate_rate",
                  "weight_replace_rate"]
network_parameters = ["num_inputs", "num_outputs", "num_hidden", "initial_connection", "initial_connection_value",
                      "feed_forward"]
activation_section = ["activation_default", "activation_mutate_rate", "activation_options"]
aggregation_section = ["aggregation_mutate_rate", "aggregation_default", "aggregation_options"]
node_bias_section = ["bias_init_mean", "bias_init_stdev", "bias_init_type", "bias_max_value", "bias_min_value",
                     "bias_mutate_power", "bias_mutate_rate", "bias_replace_rate"]
genome_comp_option = ["compatibility_threshold", "compatibility_disjoint_coefficient",
                      "compatibility_weight_coefficient"]
connection_options = ["conn_add_prob", "conn_delete_prob", "enabled_default", "enabled_mutate_rate",
                      "enabled_rate_to_false_add", "enabled_rate_to_true_add", "node_add_prob", "node_delete_prob"]
response_options = ["response_init_mean",
                    "response_init_stdev", "response_init_type", "response_max_value", "response_min_value",
                    "response_mutate_power",
                    "response_mutate_power", "response_replace_rate"]
weight_values = ["weight_init_mean",
                 "weight_init_stdev", "weight_init_type", "weight_max_value", "weight_min_value", "weight_mutate_power",
                 "weight_mutate_rate",
                 "weight_replace_rate"]
structure_options = ["single_structural_mutation", "structural_mutation_surer"]

# Open File
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)


def items_selected(event):
    """ handle item selected event
    """
    # get selected indices
    selected_indices = activation_listbox.curselection()
    selected_indices_aggregation = listbox_aggregation_options.curselection()
    if len(selected_indices) != 0:
        # get selected items
        selected_langs = ",".join([activation_listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'

        showinfo(
            title='Information',
            message=msg)
        return selected_langs
    elif len(selected_indices_aggregation) != 0:
        # get selected items
        selected_langs_aggregation = ",".join(
            [listbox_aggregation_options.get(i) for i in selected_indices_aggregation])
        msg = f'You selected: {selected_langs_aggregation}'

        showinfo(
            title='Information',
            message=msg)
        return selected_langs_aggregation


def reset_Editor():
    txt_edit.delete("1.0", "end")
    txt_edit.insert(INSERT, default_text_editor)


def default_config():
    txt_edit.delete("1.0", "end")
    txt_edit.insert(INSERT, text_editor)


def insert(line, value_to_be_added):
    # print(value_to_be_added)
    try:
        txt_edit.insert(float(line) + 1.0,
                        value_to_be_added + " = " + eval(str(value_to_be_added) + ".get()") + "\n")
    except AttributeError:
        if value_to_be_added == "aggregation_options":
            aggregation_value = [listbox_aggregation_options.get(idx) for idx in
                                 listbox_aggregation_options.curselection()]
            aggregation_option_values = ', '.join(aggregation_value)
            txt_edit.insert(float(line) + 1.0, "aggregation_options = " + aggregation_option_values + "\n")
        elif value_to_be_added == "activation_options":
            activation_values = [activation_listbox.get(idx) for idx in activation_listbox.curselection()]
            activation_option_values = ', '.join(activation_values)
            txt_edit.insert(float(line) + 1.0, "activation_options = " + activation_option_values + "\n")


def update_editor():
    thetext = txt_edit.get("1.0", 'end')
    non_added_values = []
    added_values = []
    # print(listbox.get(listbox.curselection()))
    activation_values = [activation_listbox.get(idx) for idx in activation_listbox.curselection()]
    activation_option_values = ', '.join(activation_values)
    # print(len(activation_option_values))
    # print(activation_option_values)
    aggregation_value = [listbox_aggregation_options.get(idx) for idx in listbox_aggregation_options.curselection()]
    aggregation_option_values = ', '.join(aggregation_value)
    # print(len(aggregation_option_values))
    try:
        for form_input in form_values_list:
            num_line = 0
            # print(form_input)
            # print(len(eval(str(form_input) + ".get()")) if len(eval(str(form_input) + ".get()")) != 0 else 0)
            if form_input == "initial_connection":
                if (eval(str(form_input) + ".get()") == "partial_nodirect" or eval(
                        str(form_input) + ".get()") == "partial_direct"):
                    for line in thetext.split("\n"):
                        num_line += 1
                        if line.find(form_input + " = ") == 0:
                            if form_input not in added_values:
                                txt_edit.delete(float(num_line), float(num_line) + 1.0)
                                txt_edit.insert(float(num_line),
                                                "initial_connection = " + eval(str(form_input) + ".get()") + " " + initial_connection_value.get() + "\n")
                            added_values.append(form_input)
                            if form_input in non_added_values:
                                non_added_values.remove(form_input)
                            break
                        else:
                            if form_input not in non_added_values:
                                non_added_values.append(form_input)
                else:
                    for line in thetext.split("\n"):
                        num_line += 1
                        if line.find(form_input + " = ") == 0:
                            if form_input not in added_values:
                                txt_edit.delete(float(num_line), float(num_line) + 1.0)
                                txt_edit.insert(float(num_line),
                                                form_input + " = " + eval(str(form_input) + ".get()") + "\n")
                            added_values.append(form_input)
                            if form_input in non_added_values:
                                non_added_values.remove(form_input)
                            break
                        else:
                            if form_input not in non_added_values:
                                non_added_values.append(form_input)
            if form_input == "elitism" and eval(str(form_input) + ".get()") != 0:  # if statement created for elitism
                for line in thetext.split("\n"):
                    num_line += 1
                    if line.find("elitism = ") == 0:
                        txt_edit.delete(float(num_line), float(num_line) + 1.0)
                        txt_edit.insert(float(num_line), "elitism = " + elitism.get() + "\n")
                        added_values.append(form_input)
                        if form_input in non_added_values:
                            non_added_values.remove(form_input)
                        break
                    else:
                        if form_input not in non_added_values:
                            non_added_values.append(form_input)
            if form_input == "species_elitism" and eval(
                    str(form_input) + ".get()") != 0:  # if statement created for elitism
                for line in thetext.split("\n"):
                    num_line += 1
                    if line.find("species_elitism = ") == 0:
                        txt_edit.delete(float(num_line), float(num_line) + 1.0)
                        txt_edit.insert(float(num_line), "species_elitism = " + elitism.get() + "\n")
                        added_values.append(form_input)
                        if form_input in non_added_values:
                            non_added_values.remove(form_input)
                        break
                    else:
                        if form_input not in non_added_values:
                            non_added_values.append(form_input)
            if len(eval(
                    str(form_input) + ".get()")) != 0 and (form_input != "elitism" or form_input == "activation_options" or form_input != "initial_connection"):
                for line in thetext.split("\n"):
                    num_line += 1
                    if form_input in line:
                        if form_input not in added_values:
                            if line.find(form_input + " = ") == 0:
                                txt_edit.delete(float(num_line), float(num_line) + 1.0)
                                txt_edit.insert(float(num_line),
                                                form_input + " = " + eval(str(form_input) + ".get()") + "\n")
                        added_values.append(form_input)
                        if form_input in non_added_values:
                            non_added_values.remove(form_input)
                        break
                    else:
                        if form_input not in non_added_values:
                            non_added_values.append(form_input)
    except AttributeError:
        pass
    if len(activation_option_values) > 0:
        num_line = 0
        for line in thetext.split("\n"):
            num_line += 1
            if line.find("activation_options = ") == 0:
                # print("Found in line" + line)
                if "activation_options" not in added_values:
                    txt_edit.delete(float(num_line), float(num_line) + 1.0)
                    txt_edit.insert(float(num_line), "activation_options = " + activation_option_values + "\n")
                added_values.append("activation_options")
                if "activation_options" in non_added_values:
                    non_added_values.remove("activation_options")
                break
            else:
                if "activation_options" not in non_added_values:
                    non_added_values.append("activation_options")
    if len(aggregation_option_values) > 0:
        num_line = 0
        for line in thetext.split("\n"):
            num_line += 1
            if line.find("aggregation_options = ") == 0:
                if "aggregation_options" not in added_values:
                    txt_edit.delete(float(num_line), float(num_line) + 1.0)
                    txt_edit.insert(float(num_line), "aggregation_options = " + aggregation_option_values + "\n")
                    added_values.append("aggregation_options")
                    # print("Added to added values")
                if "aggregation_options" in non_added_values:
                    non_added_values.remove("aggregation_options")
                    # print("Added to not added values")
                break
            else:
                if ("aggregation_options" not in non_added_values):
                    non_added_values.append("aggregation_options")
    non_added_values.reverse()
    while len(non_added_values) != 0:
        for non_added_value in non_added_values:
            if non_added_value in neat_selection:
                num_line_0 = 0
                for line in thetext.split("\n"):
                    num_line_0 += 1
                    if line.endswith("[NEAT]"):
                        insert(num_line_0, non_added_value)
            elif non_added_value in default_stagnation:
                num_line_0 = 0
                for line in thetext.split("\n"):
                    num_line_0 += 1
                    if line.endswith("[DefaultStagnation]"):
                        insert(num_line_0, non_added_value)
            elif non_added_value in default_reproduction:
                num_line_0 = 0
                for line in thetext.split("\n"):
                    num_line_0 += 1
                    if line.endswith("[DefaultReproduction]"):
                        if form_input == "elitism_v":
                            txt_edit.delete(float(num_line_0), float(num_line_0) + 1.0)
                            # txt_edit.insert(float(num_line), line  + fitness_criterion.get() + "\n")
                            txt_edit.insert(float(num_line_0),
                                            "elitism = " + eval(str(non_added_value) + ".get()") + "\n")
                        else:
                            insert(num_line_0, non_added_value)
            elif non_added_value in genome_section:
                num_line_0 = 0
                for line in thetext.split("\n"):
                    num_line_0 += 1
                    # if line.endswith("[DefaultGenome]"):
                    if line.endswith("# Activation options") and non_added_value in activation_section:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Aggregation options") and non_added_value in aggregation_section:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Bias options") and non_added_value in node_bias_section:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Compatibility options") and non_added_value in genome_comp_option:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Connection options") and non_added_value in connection_options:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Network parameters") and non_added_value in network_parameters:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Response options") and non_added_value in response_options:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Structure options") and non_added_value in structure_options:
                        insert(num_line_0, non_added_value)
                    elif line.endswith("# Weight options") and non_added_value in weight_values:
                        insert(num_line_0, non_added_value)
                    # break
            non_added_values.remove(non_added_value)
            break


# Define our switch function
def switch():
    # colors found at: http://tephra.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png
    global is_on

    # DarkMode is on or off
    if is_on == True:  # Light Mode
        on_button.config(image=off)
        is_on = False
        # on_button.config(image=on)
        # is_on = True
        # Labels
        for label in labels_list:  # Loop though Labels
            exec(label + '.config(fg = "gray1", bg = "grey75")')
            if label in form_Main_label_list:
                exec(label + '.config(fg = "gray1", bg = "grey75")')
        for button in buttons_list:
            exec(button + ".configure(bg = 'purple4', fg= 'gray99')")
        txt_edit.config(bg="light grey", fg="gray1")
        fr_buttons.configure(bg="red4")
        on_button.configure(bg="red4", activebackground='red4')
        root.config(bg='red4')
        # Tab Style
        style.theme_use('default')
        style.configure('TNotebook.Tab', background="gray47")
        style.configure("TNotebook", background="gray24", borderwidth=0)
        # style.configure("TNotebook.Tab", background="green", foreground=COLOR_3,, borderwidth=2)
        # Style of form (background), no foreground
        style.configure("TFrame", background="grey75", borderwidth=5)
        style.configure("TCombobox", fieldbackground="grey85", background="red4", foreground="gray1")
        style.configure("TSpinbox", fieldbackground="grey85", background="red4", foreground="gray1")
        style.configure("TCheckbutton", fieldbackground="MediumPurple1", background="grey35",
                        foreground="white smoke")
        # this changes the background colour of the 2nd item
        for options in range(len(aggregation_options)):
            listbox_aggregation_options.itemconfig(options, {'bg': 'grey85'})
        for activation_option in range(len(activation_options_values_sec)):
            activation_listbox.itemconfig(activation_option, {'bg': "grey85"})
        # print(is_on)
    else:  # Dark Mode
        on_button.config(image=on)
        is_on = True
        # Labels
        for label in labels_list:  # Loop though Labels
            exec(label + '.config(fg = "white smoke", bg = "grey35")')
        for button in buttons_list:
            exec(button + ".configure(bg = 'dark slate gray', fg = 'white smoke')")
        txt_edit.config(bg="gray12", fg="gray84")
        fr_buttons.configure(bg="gray18")
        on_button.configure(bg="gray18", activebackground='gray18')
        root.config(bg='gray24')
        # Tab Style
        style.theme_use('default')
        style.configure('TNotebook.Tab', background="gray45")
        style.configure("TNotebook", background="gray24", borderwidth=0)
        # style.configure("TNotebook.Tab", background="green", foreground=COLOR_3,, borderwidth=2)
        # Style of form (background), no foreground
        style.configure("TFrame", background="grey35", borderwidth=5)
        style.configure("TCombobox", fieldbackground="dark slate gray", background="dark red", foreground="white smoke")
        style.configure("TSpinbox", fieldbackground="dark slate gray", background="dark red", foreground="white smoke")
        style.configure("TCheckbutton", fieldbackground="dark slate gray", background="grey35",
                        foreground="white smoke")
        # this changes the background colour of the 2nd item
        for options in range(len(aggregation_options)):
            listbox_aggregation_options.itemconfig(options, {'bg': 'gray77'})
        for activation_option in range(len(activation_options_values_sec)):
            activation_listbox.itemconfig(activation_option, {'bg': "gray77"})
        # print(is_on)
    # print(is_on)
    return is_on


root = tk.Tk()

style = ttk.Style()
is_on = False

# Easy Input

frame1 = tk.Frame(master=root, width=700, height=600)
frame1.grid(row=0, column=0)

tab_View = tk.IntVar()
tabControl = ttk.Notebook(root)
tabControl.grid(row=2)

tab1 = ttk.Frame(tabControl, width=700, height=700)
tab2 = ttk.Frame(tabControl, width=700, height=700)
tab3 = ttk.Frame(tabControl, width=1000, height=700)

ttk.Separator(tab1, orient=VERTICAL).grid(column=2, row=0, rowspan=20, sticky='nse', padx=20)

tabControl.add(tab1, text='Neat Config')

# Neat Section
neat_section_L = tk.Label(tab1, text='Neat Section', font='Helvetica 12 bold underline', justify=LEFT, anchor="w")
neat_section_L.grid(row=0, column=0, ipadx=32, pady=1)

# Fitness Criterion
fitness_criterion_l = tk.Label(tab1, text="Fitness Criterion", justify=LEFT, anchor="w")
fitness_criterion_l.grid(row=1, column=0, ipadx=37, pady=2)
CreateHelpMessage.CreateToolTip(fitness_criterion_l,
                                text='The function used to compute the termination criterion from the set of genome fitnesses. Allowable values are: min, max, and mean')

fitness_criterion = ttk.Combobox(tab1, name="fitness_criterion")
fitness_criterion['values'] = ('min', 'max', 'mean')
fitness_criterion.grid(row=1, column=1)
CreateHelpMessage.CreateToolTip(fitness_criterion,
                                text='The function used to compute the termination criterion from the set of genome fitnesses. Allowable values are: min, max, and mean')
fitness_criterion.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(fitness_criterion, fitness_criterion, fitness_criterion_l, style), "%P"))

# Fitness Threshhold
fitness_threshold_l = tk.Label(tab1, text="Fitness Threshold", justify=LEFT, anchor="w")
fitness_threshold_l.grid(row=2, column=0, ipadx=35, pady=1)
CreateHelpMessage.CreateToolTip(fitness_threshold_l,
                                text='When the fitness computed by fitness_criterion meets or exceeds this threshold, the evolution process will terminate, with a call to any registered reporting class’ found_solution method.')

fitness_threshold = ttk.Spinbox(tab1, from_=-100000000, to=100000000, increment=1, name="fitness_threshold")
fitness_threshold.grid(row=2, column=1)
CreateHelpMessage.CreateToolTip(fitness_threshold,
                                text='When the fitness computed by fitness_criterion meets or exceeds this threshold, the evolution process will terminate, with a call to any registered reporting class’ found_solution method.')
fitness_threshold.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(fitness_threshold, fitness_threshold, fitness_threshold_l, style), "%P"))

# No fitness Termination
no_fitness_termination_l = tk.Label(tab1, text="No Termination?", justify=LEFT, anchor="w")
no_fitness_termination_l.grid(row=3, column=0, ipadx=36)
CreateHelpMessage.CreateToolTip(no_fitness_termination_l,
                                text='If this evaluates to True, then the fitness_criterion and fitness_threshold are ignored for termination;\n only valid if termination by a maximum number of generations passed to population.Population.run() is enabled,\n and the found_solution method is called upon generation number termination. If it evaluates to False, then fitness is used to determine termination. This defaults to “False”.')

no_fitness_termination = ttk.Combobox(tab1, name="no_fitness_termination")
no_fitness_termination['values'] = ('True', 'False')
no_fitness_termination.grid(row=3, column=1)
CreateHelpMessage.CreateToolTip(no_fitness_termination,
                                text='If this evaluates to True, then the fitness_criterion and fitness_threshold are ignored for termination;\n only valid if termination by a maximum number of generations passed to population.Population.run() is enabled,\n and the found_solution method is called upon generation number termination. If it evaluates to False, then fitness is used to determine termination. This defaults to “False”.')
no_fitness_termination.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(no_fitness_termination, no_fitness_termination, no_fitness_termination_l, style), "%P"))

# Pop Size
pop_size_l = tk.Label(tab1, text="Population Size", justify=LEFT, anchor="w")
pop_size_l.grid(row=4, column=0, ipadx=39, pady=1)
CreateHelpMessage.CreateToolTip(pop_size_l, text='The number of individuals in each generation.')

pop_size = ttk.Spinbox(tab1, from_=0, to=100000000, increment=1, name="pop_size")
pop_size.grid(row=4, column=1)
CreateHelpMessage.CreateToolTip(pop_size, text='The number of individuals in each generation.')
pop_size.config(validate="key",
                validatecommand=(ValidateInput.ValidateInput(pop_size, pop_size, pop_size_l, style), "%P"))

# reset_on_extinction
reset_on_extinction_L = tk.Label(tab1, text="Reset on extinction?", justify=LEFT, anchor="w")
reset_on_extinction_L.grid(row=5, column=0, ipadx=27)
CreateHelpMessage.CreateToolTip(reset_on_extinction_L,
                                text='If this evaluates to True, when all species simultaneously become extinct due to stagnation,\n a new random population will be created. If False, a CompleteExtinctionException will be thrown.')

reset_on_extinction = ttk.Combobox(tab1, name="reset_on_extinction")
reset_on_extinction['values'] = ('True', 'False')
reset_on_extinction.grid(row=5, column=1)
CreateHelpMessage.CreateToolTip(reset_on_extinction,
                                text='If this evaluates to True, when all species simultaneously become extinct due to stagnation,\n a new random population will be created. If False, a CompleteExtinctionException will be thrown.')
reset_on_extinction.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(reset_on_extinction, reset_on_extinction, reset_on_extinction_L, style), "%P"))

# Default Stagnation section
default_stagnation_l = tk.Label(tab1, text='Default Stagnation', font='Helvetica 12 bold underline', justify=LEFT,
                                anchor="w")
default_stagnation_l.grid(row=6, column=0, ipadx=10, pady=2)

# species_fitness_func
species_fitness_func_l = tk.Label(tab1, text="Species Fitness Func", justify=LEFT, anchor="w")
species_fitness_func_l.grid(row=7, column=0, ipadx=27, pady=1)
CreateHelpMessage.CreateToolTip(species_fitness_func_l,
                                text='The function used to compute species fitness. This defaults to ``mean``. Allowed values are: max, min, mean, and median')

species_fitness_func = ttk.Combobox(tab1, name="species_fitness_func")
species_fitness_func['values'] = ('min', 'max', 'mean', 'median')
species_fitness_func.grid(row=7, column=1, pady=1)
CreateHelpMessage.CreateToolTip(species_fitness_func,
                                text='The function used to compute species fitness. This defaults to ``mean``. Allowed values are: max, min, mean, and median')
species_fitness_func.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(species_fitness_func, species_fitness_func, species_fitness_func_l, style), "%P"))

# max_stagnation
max_stagnation_l = tk.Label(tab1, text="Max Stagination", justify=LEFT, anchor="w")
max_stagnation_l.grid(row=8, column=0, ipadx=36, pady=1)
CreateHelpMessage.CreateToolTip(max_stagnation_l,
                                text='Species that have not shown improvement in more than this number of generations will be considered stagnant and removed. This defaults to 15.')

max_stagnation = ttk.Spinbox(tab1, from_=0, to=100000000, increment=1, name="max_stagnation")
max_stagnation.grid(row=8, column=1, pady=1)
CreateHelpMessage.CreateToolTip(max_stagnation,
                                text='Species that have not shown improvement in more than this number of generations will be considered stagnant and removed. This defaults to 15.')
max_stagnation.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(max_stagnation, max_stagnation, max_stagnation_l, style), "%P"))

# species_elitism
species_elitism_l = tk.Label(tab1, text="Num Protected Species", justify=LEFT, anchor="w")
species_elitism_l.grid(row=9, column=0, ipadx=18, pady=1)
CreateHelpMessage.CreateToolTip(max_stagnation,
                                text='The number of species that will be protected from stagnation;\n mainly intended to prevent total extinctions caused by all species becoming stagnant before new species arise.\n For example, a species_elitism setting of 3 will prevent the 3 species with\n the highest species fitness from being removed for stagnation regardless of the amount of time they have not shown improvement. This defaults to 0.')

species_elitism = ttk.Spinbox(tab1, from_=0, to=100000000, increment=1, name="species_elitism")
species_elitism.grid(row=9, column=1, pady=2)
CreateHelpMessage.CreateToolTip(species_elitism,
                                text='The number of species that will be protected from stagnation;\n mainly intended to prevent total extinctions caused by all species becoming stagnant before new species arise.\n For example, a species_elitism setting of 3 will prevent the 3 species with\n the highest species fitness from being removed for stagnation regardless of the amount of time they have not shown improvement. This defaults to 0.')
species_elitism.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(species_elitism, species_elitism, species_elitism_l, style), "%P"))

# Default Reproduction
default_reproduction_l = tk.Label(tab1, text='Default Reproduction', font='Helvetica 12 bold underline')
default_reproduction_l.grid(row=10, column=0, pady=5, ipadx=2)

# elitism
elitism_l = tk.Label(tab1, text="Elitism", justify=LEFT, anchor="w")
elitism_l.grid(row=11, column=0, ipadx=63, pady=2)
CreateHelpMessage.CreateToolTip(elitism_l,
                                text='The number of most-fit individuals in each species that will be preserved as-is from one generation to the next. This defaults to 0.')

elitism = ttk.Spinbox(tab1, from_=0, to=100000000, name='elitism')
elitism.grid(row=11, column=1)
CreateHelpMessage.CreateToolTip(elitism,
                                text='The number of most-fit individuals in each species that will be preserved as-is from one generation to the next. This defaults to 0.')
elitism.config(validate="key", validatecommand=(ValidateInput.ValidateInput(elitism, elitism, elitism_l, style), "%P"))

# survival_threshold
survival_threshold_l = tk.Label(tab1, text="Survival Threshold", justify=LEFT, anchor="w")
survival_threshold_l.grid(row=12, column=0, ipadx=32, pady=2)
CreateHelpMessage.CreateToolTip(survival_threshold_l,
                                text='The fraction for each species allowed to reproduce each generation. This defaults to 0.2.')

survival_threshold = ttk.Spinbox(tab1, from_=0.00, to=100000000.00, increment=0.01, name="survival_threshold")
survival_threshold.grid(row=12, column=1)  # ipady = 2)
CreateHelpMessage.CreateToolTip(survival_threshold,
                                text='The fraction for each species allowed to reproduce each generation. This defaults to 0.2.')
survival_threshold.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(survival_threshold, survival_threshold, survival_threshold_l, style), "%P"))

# min_species_size
min_species_size_l = tk.Label(tab1, text="Min N of genomes per species", justify=LEFT, anchor="w")
min_species_size_l.grid(row=13, column=0, pady=2)
CreateHelpMessage.CreateToolTip(min_species_size_l,
                                text='The minimum number of genomes per species after reproduction. This defaults to 2.')

min_species_size = ttk.Spinbox(tab1, from_=0, to=100000000, name="min_species_size")
min_species_size.grid(row=13, column=1)
CreateHelpMessage.CreateToolTip(min_species_size,
                                text='The minimum number of genomes per species after reproduction. This defaults to 2.')
min_species_size.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(min_species_size, min_species_size, min_species_size_l, style), "%P"))

# Default Genome
tabControl.add(tab2, text='Default Genome')
tabControl.add(tab3, text='Default Genome')

tabControl.tab(2, state="disabled")

# Genome
genome_Section_l = tk.Label(tab1, text='Genome Section', font='Helvetica 12 bold underline', anchor="w")
genome_Section_l.grid(row=14, column=0, pady=5, ipadx=15)

# Network Parameters
network_Parameters_l = tk.Label(tab1, text='Network Parameters', justify=LEFT, font='Helvetica 11 bold', anchor="w")
network_Parameters_l.grid(row=15, column=0, pady=2, sticky=tk.W)

# num_inputs
num_inputs_l = tk.Label(tab1, text="Number of input nodes:", anchor="w")
num_inputs_l.grid(row=16, column=0, ipadx=16)
CreateHelpMessage.CreateToolTip(num_inputs_l,
                                text='num_inputs\nThe number of input nodes, through which the network receives inputs.')

num_inputs = ttk.Spinbox(tab1, from_=1, to=1000000000, increment=1, name="num_inputs")
num_inputs.grid(row=16, column=1)
CreateHelpMessage.CreateToolTip(num_inputs,
                                text='num_inputs\nThe number of input nodes, through which the network receives inputs.')
num_inputs.config(validate="key",
                  validatecommand=(ValidateInput.ValidateInput(num_inputs, num_inputs, num_inputs_l, style), "%P"))

# num_outputs
num_outputs_l = tk.Label(tab1, text="Number of output nodes:", anchor="w")
num_outputs_l.grid(row=17, column=0, ipadx=13, pady=2)
CreateHelpMessage.CreateToolTip(num_outputs_l,
                                text='num_outputs\nThe number of output nodes, to which the network delivers outputs.')

num_outputs = ttk.Spinbox(tab1, from_=1, to=1000000000, increment=1, name="num_outputs")
num_outputs.grid(row=17, column=1)
CreateHelpMessage.CreateToolTip(num_outputs,
                                text='num_outputs\nThe number of output nodes, to which the network delivers outputs.')
num_outputs.config(validate="key",
                   validatecommand=(ValidateInput.ValidateInput(num_outputs, num_outputs, num_outputs_l, style), "%P"))

# num_hidden
num_hidden_l = tk.Label(tab1, text="Number of hidden nodes:", anchor="w")
num_hidden_l.grid(row=18, column=0, ipadx=13, pady=2)
CreateHelpMessage.CreateToolTip(num_hidden_l,
                                text='num_hidden\nThe number of hidden nodes to add to each genome in the initial population.')

num_hidden = ttk.Spinbox(tab1, from_=1, to=1000000000, increment=1, name="num_hidden")
num_hidden.grid(row=18, column=1)
CreateHelpMessage.CreateToolTip(num_hidden,
                                text='num_hidden\nThe number of hidden nodes to add to each genome in the initial population.')
num_hidden.config(validate="key",
                  validatecommand=(ValidateInput.ValidateInput(num_hidden, num_hidden, num_hidden_l, style), "%P"))

# initial_connection
initial_connection_L = tk.Label(tab1, text="Initial connection:", anchor="w")
initial_connection_L.grid(row=19, column=0, ipadx=34)
CreateHelpMessage.CreateToolTip(initial_connection_L,
                                text='initial_connection\nSpecifies the initial connectivity of newly-created genomes. (Note the effects on settings other than unconnected of the enabled_default parameter.)\nThere are seven allowed values:\nunconnected - No connections are initially present. This is the default.\nfs_neat_nohidden - One randomly-chosen input node has one connection to each output node. (This is one version of the FS-NEAT scheme; “FS” stands for “Feature Selection”.)\nfs_neat_hidden - One randomly-chosen input node has one connection to each hidden and output node. (This is another version of the FS-NEAT scheme. If there are no hidden nodes, it is the same as fs_neat_nohidden.)\nfull_nodirect - Each input node is connected to all hidden nodes, if there are any, and each hidden node is connected to all output nodes; otherwise, each input node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\nfull_direct - Each input node is connected to all hidden and output nodes, and each hidden node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\npartial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\npartial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')

initial_connection = ttk.Combobox(tab1, name="initial_connection")
initial_connection['values'] = ('unconnected', 'fs_neat_nohidden', 'fs_neat_hidden', 'full_nodirect', 'full_direct',
                                'partial_nodirect', 'partial_direct')
initial_connection.grid(row=19, column=1)
CreateHelpMessage.CreateToolTip(initial_connection,
                                text='initial_connection\nSpecifies the initial connectivity of newly-created genomes. (Note the effects on settings other than unconnected of the enabled_default parameter.)\nThere are seven allowed values:\nunconnected - No connections are initially present. This is the default.\nfs_neat_nohidden - One randomly-chosen input node has one connection to each output node. (This is one version of the FS-NEAT scheme; “FS” stands for “Feature Selection”.)\nfs_neat_hidden - One randomly-chosen input node has one connection to each hidden and output node. (This is another version of the FS-NEAT scheme. If there are no hidden nodes, it is the same as fs_neat_nohidden.)\nfull_nodirect - Each input node is connected to all hidden nodes, if there are any, and each hidden node is connected to all output nodes; otherwise, each input node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\nfull_direct - Each input node is connected to all hidden and output nodes, and each hidden node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\npartial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\npartial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')
initial_connection.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(initial_connection, initial_connection, initial_connection_L, style), "%P"))

# initial_conection
initial_conection_value_l = tk.Label(tab1, text="Initial Connection probability:", anchor="w")
initial_conection_value_l.grid(row=20, column=0, ipadx=3)
CreateHelpMessage.CreateToolTip(initial_conection_value_l,
                                text='initial_conection #\npartial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\npartial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')

initial_connection_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="initial_connection_value")
initial_connection_value.grid(row=20, column=1)
CreateHelpMessage.CreateToolTip(initial_connection_value,
                                text='initial_conection #\npartial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\npartial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')
initial_connection_value.config(state='disabled')
CreateHelpMessage.Validate(initial_connection, initial_connection_value)
initial_connection_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(initial_connection_value, initial_connection_value, initial_conection_value_l, style),
"%P"))

# feed_forward
feed_forward_L = tk.Label(tab1, text="Feed Forward?", anchor="w")
feed_forward_L.grid(row=21, column=0, ipadx=43)
CreateHelpMessage.CreateToolTip(feed_forward_L,
                                text='feed_forward\nIf this evaluates to True, generated networks will not be\nallowed to have recurrent connections (they will be feedforward).\nOtherwise they may be (but are not forced to be) recurrent.')

feed_forward = ttk.Combobox(tab1, name='feed_forward')
feed_forward['values'] = ('True', 'False')
feed_forward.grid(row=21, column=1)
CreateHelpMessage.CreateToolTip(feed_forward,
                                text='feed_forward\nIf this evaluates to True, generated networks will not be\nallowed to have recurrent connections (they will be feedforward).\nOtherwise they may be (but are not forced to be) recurrent.')
feed_forward.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(feed_forward, feed_forward, feed_forward_L, style), "%P"))

# Node Activation and Aggregation options

# activation_default
random_from_form_l = tk.Label(tab1, text="Enable random selector:", font='Helvetica 9 italic')
random_from_form_l.grid(row=0, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(random_from_form_l,
                                text='Enabling this will allow the user to see assign random choices if none selected directly on form so can see later which one is used')

random_from_form = ttk.Combobox(tab1, name='random_from_form')
random_from_form['values'] = ('True', 'False')
random_from_form.grid(row=0, column=4)
CreateHelpMessage.CreateToolTip(random_from_form,
                                text='Enabling this will allow the user to see assign random choices if none selected directly on form so can see later which one is used')

# Network Parameters
activation_n_aggregation_o = tk.Label(tab1, text='Node act & aggr opt:', font='Helvetica 11 bold', anchor="e")
activation_n_aggregation_o.grid(row=1, column=3, pady=5, sticky=tk.W)

# activation_default
activation_default_L = tk.Label(tab1, text="Default Activation Func:")
activation_default_L.grid(row=2, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_default_L,
                                text='activation_default\nThe default activation function attribute assigned to new nodes.\n If none is given, or “random” is specified, one of the activation_options will be chosen at random.')

activation_default = ttk.Combobox(tab1, name="activation_default")
activation_default['values'] = ('abs', 'clamped', 'cube', 'exp', 'gauss',
                                'hat', 'identity', 'inv', 'log', 'relu', 'elu',
                                'lelu', 'selu', 'sigmoid', 'sin', 'softplus', 'square', 'tanh')
activation_default.grid(row=2, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_default,
                                text='activation_default\nThe default activation function attribute assigned to new nodes.\n If none is given, or “random” is specified, one of the activation_options will be chosen at random.')
activation_default.config(validate="key", validatecommand=(
ValidateInput.ValidateInputWithRandom(activation_default, activation_default, activation_default_L, style,
                                      random_from_form), "%P"))

# Activation Mutate rate
activation_mutate_rate_L = tk.Label(tab1, text="Activation Mutate rate:", anchor="w")
activation_mutate_rate_L.grid(row=3, column=3, ipadx=1, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_mutate_rate_L,
                                text='activation_mutate_rate\nThe probability that mutation will replace the node’s activation\n function with a randomly-determined member of the activation_options. Valid values are in [0.0, 1.0].')

activation_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="activation_mutate_rate")
activation_mutate_rate.grid(row=3, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_mutate_rate,
                                text='activation_mutate_rate\nThe probability that mutation will replace the node’s activation\n function with a randomly-determined member of the activation_options. Valid values are in [0.0, 1.0].')
activation_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(activation_mutate_rate, activation_mutate_rate, activation_mutate_rate_L, style), "%P"))

# Activation Option
activation_options_L = tk.Label(tab1, text="Activation Func:", anchor="w")
activation_options_L.grid(row=4, column=3, ipadx=18, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_options_L,
                                text='activation_options\nA space-separated list of the activation functions that may be used by nodes. This defaults to sigmoid.\n The built-in available functions can be found in Overview of builtin activation functions; more can be added as described in Customizing Behavior.')

activation_options_values_sec = ('abs', 'clamped', 'cube', 'exp', 'gauss',
                                 'hat', 'identity', 'inv', 'log', 'relu', 'elu',
                                 'lelu', 'selu', 'sigmoid', 'sin', 'softplus', 'square', 'tanh')
langs_var = tk.StringVar(value=activation_options_values_sec)
activation_listbox = tk.Listbox(tab1, height=3, listvariable=langs_var, selectmode='extended',
                                name="activation_options", exportselection=0)
activation_listbox.grid(row=4, column=4, pady=2, sticky=tk.W)
activation_options_selected = activation_listbox.bind('<<ListboxSelect>>', items_selected)

# print(activation_options_selected)
# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=activation_listbox.yview
)

activation_listbox['yscrollcommand'] = scrollbar.set

# Aggregation_mutate_rate
aggregation_mutate_rate_L = tk.Label(tab1, text="Aggregation mutate rate:", anchor="e")
aggregation_mutate_rate_L.grid(row=5, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_mutate_rate_L,
                                text='aggregation_mutate_rate\nThe probability that mutation will replace the node’s aggregation\n function with a randomly-determined member of the aggregation_options. Valid values are in [0.0, 1.0].')

aggregation_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="aggregation_mutate_rate")
aggregation_mutate_rate.grid(row=5, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_mutate_rate,
                                text='aggregation_mutate_rate\nThe probability that mutation will replace the node’s aggregation\n function with a randomly-determined member of the aggregation_options. Valid values are in [0.0, 1.0].')
aggregation_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(aggregation_mutate_rate, aggregation_mutate_rate, aggregation_mutate_rate_L, style), "%P"))

# aggregation_default
aggregation_default_L = tk.Label(tab1, text="Aggregation default:", anchor="w")
aggregation_default_L.grid(row=6, column=3, ipadx=8, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_default_L,
                                text='aggregation_default\nThe default aggregation function attribute assigned to new nodes. If none is given, or “random” is specified, one of the aggregation_options will be chosen at random.')

aggregation_default = ttk.Combobox(tab1, name="aggregation_default")
aggregation_default['values'] = ('sum', 'product', 'min', 'max', 'mean', 'median', 'maxabs')
aggregation_default.grid(row=6, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_default_L,
                                text='aggregation_default\nThe default aggregation function attribute assigned to new nodes. If none is given, or “random” is specified, one of the aggregation_options will be chosen at random.')
aggregation_default.config(validate="key", validatecommand=(
ValidateInput.ValidateInputWithRandom(aggregation_default, aggregation_default, aggregation_default_L, style,
                                      random_from_form), "%P"))

# aggregation_options
aggregation_options_L = tk.Label(tab1, text="Aggregatrions Func/s:", anchor="w")
aggregation_options_L.grid(row=7, column=3, ipadx=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_options_L,
                                text='aggregation_options\nA space-separated list of the aggregation functions that may be used by nodes. This defaults to “sum”. The available functions (defined in aggregations) are: sum, product, min, max, mean, median, and maxabs (which returns the input value with the greatest absolute value; the returned value may be positive or negative). New aggregation functions can be defined similarly to new activation functions. (Note that the function needs to take a list or other iterable; the reduce function, as in aggregations, may be of use in this.)')

aggregation_options = ('sum', 'product', 'min', 'max', 'mean', 'median', 'maxads')
langs_var_aggregation_options = tk.StringVar(value=aggregation_options)
listbox_aggregation_options = tk.Listbox(tab1, height=4, listvariable=langs_var_aggregation_options,
                                         selectmode='extended', name="aggregation_options", exportselection=0)
listbox_aggregation_options.grid(row=7, column=4, sticky=tk.W)
aggregation_options_selected = listbox_aggregation_options.bind('<<ListboxSelect>>', items_selected)
print(aggregation_options_selected)
# link a scrollbar to a list
scrollbar_aggregation_option = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox_aggregation_options.yview
)

listbox_aggregation_options['yscrollcommand'] = scrollbar_aggregation_option.set

# Node Bian Options
node_bias_o = tk.Label(tab1, text='Node Bias options', font='Helvetica 11 bold')
node_bias_o.grid(row=8, column=3, pady=5, sticky=tk.W)

# bias_init_mean
bias_init_mean_l = tk.Label(tab1, text="Bias init mean:")
bias_init_mean_l.grid(row=9, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_mean_l,
                                text='bias_init_mean\nThe mean of the normal/gaussian distribution, if it is used to select bias attribute values for new nodes.')

bias_init_mean = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=0.1, name="bias_init_mean")
bias_init_mean.grid(row=9, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_mean,
                                text='bias_init_mean\nThe mean of the normal/gaussian distribution, if it is used to select bias attribute values for new nodes.')
bias_init_mean.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_init_mean, bias_init_mean, bias_init_mean_l, style), "%P"))

# bias_init_stdev
bias_init_stdev_l = tk.Label(tab1, text="Bias init standard:")
bias_init_stdev_l.grid(row=10, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_stdev_l,
                                text='bias_init_stdev\nThe standard deviation of the normal/gaussian distribution, if it is used to select bias values for new nodes.')

bias_init_stdev = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_init_stdev")
bias_init_stdev.grid(row=10, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_stdev,
                                text='bias_init_stdev\nThe standard deviation of the normal/gaussian distribution, if it is used to select bias values for new nodes.')
bias_init_stdev.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_init_stdev, bias_init_stdev, bias_init_stdev_l, style), "%P"))

# bias_init_type
bias_init_type_l = tk.Label(tab1, text="Bias init type:")
bias_init_type_l.grid(row=11, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_type_l,
                                text='bias_init_type\nIf set to gaussian or normal, then the initialization is to\n a normal/gaussian distribution. If set to uniform, a uniform distribution from max(bias_min_value,\n(bias_init_mean−(bias_init_stdev∗2))) to min(bias_max_value,(bias_init_mean+(bias_init_stdev∗2))).\n (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288\n (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')

bias_init_type = ttk.Combobox(tab1, name="bias_init_type")
bias_init_type['values'] = ('gaussian', 'normal', 'uniform')
bias_init_type.grid(row=11, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_type,
                                text='bias_init_type\nIf set to gaussian or normal, then the initialization is to\n a normal/gaussian distribution. If set to uniform, a uniform distribution from max(bias_min_value,\n(bias_init_mean−(bias_init_stdev∗2))) to min(bias_max_value,(bias_init_mean+(bias_init_stdev∗2))).\n (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288\n (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')
bias_init_type.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_init_type, bias_init_type, bias_init_type_l, style), "%P"))

# bias_max_value
bias_max_value_l = tk.Label(tab1, text="Bias Maximum allowed bias value:")
bias_max_value_l.grid(row=12, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_max_value_l,
                                text='bias_max_value\nThe maximum allowed bias value. Biases above this value will be clamped to this value.')

bias_max_value = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_max_value")
bias_max_value.grid(row=12, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_max_value,
                                text='bias_max_value\nThe maximum allowed bias value. Biases above this value will be clamped to this value.')
bias_max_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_max_value, bias_max_value, bias_max_value_l, style), "%P"))

# bias_min_value
bias_min_value_l = tk.Label(tab1, text="Bias Minimum allowed bias value:")
bias_min_value_l.grid(row=13, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_min_value_l,
                                text='bias_min_value\nThe minimum  allowed bias value. Biases above this value will be clamped to this value.')

bias_min_value = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_min_value")
bias_min_value.grid(row=13, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_min_value,
                                text='The minimum  allowed bias value. Biases above this value will be clamped to this value.')
bias_min_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_min_value, bias_min_value, bias_min_value_l, style), "%P"))

# bias_mutate_power
bias_mutate_power_l = tk.Label(tab1, text="Bias mutation power:")
bias_mutate_power_l.grid(row=14, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_min_value_l,
                                text='bias_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a bias value mutation is drawn.')

bias_mutate_power = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_mutate_power")
bias_mutate_power.grid(row=14, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_mutate_power,
                                text='bias_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a bias value mutation is drawn.')
bias_mutate_power.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_mutate_power, bias_mutate_power, bias_mutate_power_l, style), "%P"))

# bias_mutate_rate
bias_mutate_rate_l = tk.Label(tab1, text="Bias mutation rate:")
bias_mutate_rate_l.grid(row=15, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_mutate_rate_l,
                                text='bias_mutate_rate\The probability that mutation will change the bias of a node by adding a random value.')

bias_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_mutate_rate")
bias_mutate_rate.grid(row=15, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_mutate_rate,
                                text='bias_mutate_rate\nThe probability that mutation will change the bias of a node by adding a random value.')
bias_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_mutate_rate, bias_mutate_rate, bias_mutate_rate_l, style), "%P"))

# bias_replace_rate
bias_replace_rate_l = tk.Label(tab1, text="Bias replace rate:")
bias_replace_rate_l.grid(row=16, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_replace_rate_l,
                                text='bias_replace_rate\nThe probability that mutation will replace the bias of a node with a newly chosen random value (as if it were a new node).')

bias_replace_rate = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_replace_rate")
bias_replace_rate.grid(row=16, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_replace_rate,
                                text='bias_replace_rate\nThe probability that mutation will replace the bias of a node with a newly chosen random value (as if it were a new node).')
bias_replace_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_replace_rate, bias_replace_rate, bias_replace_rate_l, style), "%P"))

# Genome Compatibility Options
genome_compatibility_o = tk.Label(tab1, text='Genome Comp. Options', font='Helvetica 11 bold')
genome_compatibility_o.grid(row=17, column=3, pady=5, sticky=tk.W)

# compatibility_threshold
compatibility_threshold_l = tk.Label(tab1, text="Compatibility Threshold:")
compatibility_threshold_l.grid(row=18, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_threshold_l,
                                text='compatibility_threshold\nIndividuals whose genomic distance is less than this threshold are considered to be in the same species.')

compatibility_threshold = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name="compatibility_threshold")
compatibility_threshold.grid(row=18, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_threshold,
                                text='compatibility_threshold\nIndividuals whose genomic distance is less than this threshold are considered to be in the same species.')
compatibility_threshold.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(compatibility_threshold, compatibility_threshold, compatibility_threshold_l, style), "%P"))

# compatibility_disjoint_coefficient
compatibility_disjoint_coefficient_l = tk.Label(tab1, text="Compatibility Disjoint coefficient:")
compatibility_disjoint_coefficient_l.grid(row=19, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_disjoint_coefficient_l,
                                text='compatibility_disjoint_coefficient\nThe coefficient for the disjoint and excess gene counts’ contribution to the genomic distance.')

compatibility_disjoint_coefficient = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1,
                                                 name="compatibility_disjoint_coefficient")
compatibility_disjoint_coefficient.grid(row=19, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_disjoint_coefficient,
                                text='compatibility_disjoint_coefficient\nThe coefficient for the disjoint and excess gene counts’ contribution to the genomic distance.')
compatibility_disjoint_coefficient.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(compatibility_disjoint_coefficient, compatibility_disjoint_coefficient,
                            compatibility_disjoint_coefficient_l, style), "%P"))

# compatibility_weight_coefficient
compatibility_weight_coefficient_l = tk.Label(tab1, text="Compatibility weight coefficient:")
compatibility_weight_coefficient_l.grid(row=20, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_weight_coefficient_l,
                                text='compatibility_weight_coefficient\nThe coefficient for each weight, bias, or response multiplier difference’s contribution to the\ngenomic distance (for homologous nodes or connections). This is also used as the value to\nadd for differences in activation functions, aggregation functions, or enabled/disabled status.')

compatibility_weight_coefficient = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1,
                                               name="compatibility_weight_coefficient")
compatibility_weight_coefficient.grid(row=20, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_weight_coefficient,
                                text='compatibility_weight_coefficient\nThe coefficient for each weight, bias, or response multiplier difference’s contribution to the\ngenomic distance (for homologous nodes or connections). This is also used as the value to\nadd for differences in activation functions, aggregation functions, or enabled/disabled status.')
compatibility_disjoint_coefficient.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(compatibility_weight_coefficient, compatibility_weight_coefficient,
                            compatibility_weight_coefficient_l, style), "%P"))

# Connection options
connection_options_l = tk.Label(tab1, text='Connection options', font='Helvetica 11 bold')
connection_options_l.grid(row=0, column=5, pady=5, sticky=tk.W)

# conn_add_prob
conn_add_prob_l = tk.Label(tab1, text="Connection add probability:")
conn_add_prob_l.grid(row=1, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(conn_add_prob_l,
                                text='conn_add_prob\nThe probability that mutation will add a connection between existing nodes. Valid values are in [0.0, 1.0].')

conn_add_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="conn_add_prob")
conn_add_prob.grid(row=1, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(conn_add_prob_l,
                                text='conn_add_prob\nThe probability that mutation will add a connection between existing nodes. Valid values are in [0.0, 1.0].')
conn_add_prob.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(conn_add_prob, conn_add_prob, conn_add_prob_l, style), "%P"))

# conn_delete_prob
conn_delete_prob_l = tk.Label(tab1, text="Connection delete probability:")
conn_delete_prob_l.grid(row=2, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(conn_delete_prob_l,
                                text='conn_delete_prob\nThe probability that mutation will delete an existing connection. Valid values are in [0.0, 1.0].')

conn_delete_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="conn_delete_prob")
conn_delete_prob.grid(row=2, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(conn_delete_prob,
                                text='conn_delete_prob\nThe probability that mutation will delete an existing connection. Valid values are in [0.0, 1.0].')
conn_delete_prob.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(conn_delete_prob, conn_delete_prob, conn_delete_prob_l, style), "%P"))

# enabled_default
enabled_default_L = tk.Label(tab1, text="Enabled default")
enabled_default_L.grid(row=3, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_default_L,
                                text='enabled_default\nThe default enabled attribute of newly created connections. Valid values are True and False.')

enabled_default = ttk.Combobox(tab1, name="enabled_default")
enabled_default['values'] = ('True', 'False')
enabled_default.grid(row=3, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_default,
                                text='enabled_default\nThe default enabled attribute of newly created connections. Valid values are True and False.')
enabled_default.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(enabled_default, enabled_default, enabled_default_L, style), "%P"))

# enabled_mutate_rate
enabled_mutate_rate_l = tk.Label(tab1, text="Enabled Mutate Rate:")
enabled_mutate_rate_l.grid(row=4, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_mutate_rate_l,
                                text='enabled_mutate_rate\nThe probability that mutation will replace (50/50 chance of True or False)\nthe enabled status of a connection. Valid values are in [0.0, 1.0].')

enabled_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name='enabled_mutate_rate')
enabled_mutate_rate.grid(row=4, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_mutate_rate,
                                text='enabled_mutate_rate\nThe probability that mutation will replace (50/50 chance of True or False)\nthe enabled status of a connection. Valid values are in [0.0, 1.0].')
enabled_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(enabled_mutate_rate, enabled_mutate_rate, enabled_mutate_rate_l, style), "%P"))

# enabled_rate_to_false_add
enabled_rate_to_false_add_l = tk.Label(tab1, text="enabled_rate_to_false_add:")
enabled_rate_to_false_add_l.grid(row=5, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_rate_to_false_add_l,
                                text='enabled_rate_to_false_add\nAdds to the enabled_mutate_rate if the connection is currently enabled.')

enabled_rate_to_false_add = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name="enabled_rate_to_false_add")
enabled_rate_to_false_add.grid(row=5, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_rate_to_false_add,
                                text='enabled_rate_to_false_add\nAdds to the enabled_mutate_rate if the connection is currently enabled.')
enabled_rate_to_false_add.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(enabled_rate_to_false_add, enabled_rate_to_false_add, enabled_rate_to_false_add_l, style),
"%P"))

# enabled_rate_to_true_add
enabled_rate_to_true_add_l = tk.Label(tab1, text="enabled_rate_to_true_add:")
enabled_rate_to_true_add_l.grid(row=6, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_rate_to_true_add_l,
                                text='enabled_rate_to_true_add\nAdds to the enabled_mutate_rate if the connection is currently not enabled..')

enabled_rate_to_true_add = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name="enabled_rate_to_true_add")
enabled_rate_to_true_add.grid(row=6, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_rate_to_true_add,
                                text='enabled_rate_to_true_add\nAdds to the enabled_mutate_rate if the connection is currently not enabled..')
enabled_rate_to_true_add.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(enabled_rate_to_true_add, enabled_rate_to_true_add, enabled_rate_to_true_add_l, style),
"%P"))

# node_add_prob
node_add_prob_l = tk.Label(tab1, text="Add node by mutation probability:")
node_add_prob_l.grid(row=7, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(node_add_prob_l,
                                text='node_add_prob\nThe probability that mutation will add a new node (essentially replacing an existing connection, the enabled status of which will be set to False). Valid values are in [0.0, 1.0].')

node_add_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="node_add_prob")
node_add_prob.grid(row=7, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(node_add_prob,
                                text='node_add_prob\nThe probability that mutation will add a new node (essentially replacing an existing connection, the enabled status of which will be set to False). Valid values are in [0.0, 1.0].')
node_add_prob.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(node_add_prob, node_add_prob, node_add_prob_l, style), "%P"))

# node_delete_prob
node_delete_prob_l = tk.Label(tab1, text="Delete node by mutation probability:")
node_delete_prob_l.grid(row=8, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(node_delete_prob_l,
                                text='node_delete_prob\nThe probability that mutation will delete an existing node (and all connections to it). Valid values are in [0.0, 1.0].')

node_delete_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="node_delete_prob")
node_delete_prob.grid(row=8, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(node_delete_prob,
                                text='node_delete_prob\nThe probability that mutation will delete an existing node (and all connections to it). Valid values are in [0.0, 1.0].')
node_delete_prob.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(node_delete_prob, node_delete_prob, node_delete_prob_l, style), "%P"))

# Response
response_l = tk.Label(tab1, text='Response options', font='Helvetica 11 bold')
response_l.grid(row=9, column=5, pady=5, sticky=tk.W)

# response_init_mean
response_init_mean_l = tk.Label(tab1, text="Mean response deviation: ")
response_init_mean_l.grid(row=10, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_mean_l,
                                text='The mean of the normal/gaussian distribution, if it is used to select response multiplier attribute values for new nodes.')

response_init_mean = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_init_mean")
response_init_mean.grid(row=10, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_mean,
                                text='The mean of the normal/gaussian distribution, if it is used to select response multiplier attribute values for new nodes.')
response_init_mean.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_init_mean, response_init_mean, response_init_mean_l, style), "%P"))

# response_init_stdev
response_init_stdev_l = tk.Label(tab1, text="Standard response deviation:")
response_init_stdev_l.grid(row=11, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_stdev_l,
                                text='The standard deviation of the normal/gaussian distribution, if it is used to select response multipliers for new nodes.')

response_init_stdev = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_init_stdev")
response_init_stdev.grid(row=11, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_stdev,
                                text='The standard deviation of the normal/gaussian distribution, if it is used to select response multipliers for new nodes.')
response_init_stdev.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_init_stdev, response_init_stdev, response_init_stdev_l, style), "%P"))

# response_init_type
response_init_type_L = tk.Label(tab1, text="Response type:")
response_init_type_L.grid(row=12, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_type_L,
                                text='If set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(response_min_value,(response_init_mean−(response_init_stdev∗2))) to min(response_max_value,(response_init_mean+(response_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')

response_init_type = ttk.Combobox(tab1, name="response_init_type")
response_init_type['values'] = ('normal', 'uniform', 'gaussian')
response_init_type.grid(row=12, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_type,
                                text='If set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(response_min_value,(response_init_mean−(response_init_stdev∗2))) to min(response_max_value,(response_init_mean+(response_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')
response_init_type.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_init_type, response_init_type, response_init_type_L, style), "%P"))

# response_max_value
response_max_value_l = tk.Label(tab1, text="Max response value:")
response_max_value_l.grid(row=13, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_max_value_l,
                                text='The maximum allowed response multiplier. Response multipliers above this value will be clamped to this value.')

response_max_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_max_value")
response_max_value.grid(row=13, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_max_value,
                                text='The maximum allowed response multiplier. Response multipliers above this value will be clamped to this value.')
response_max_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_max_value, response_max_value, response_max_value_l, style), "%P"))

# response_min_value
response_min_value_l = tk.Label(tab1, text="Min response value:")
response_min_value_l.grid(row=14, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_min_value_l,
                                text='The minimum allowed response multiplier. Response multipliers below this value will be clamped to this value.')

response_min_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_min_value")
response_min_value.grid(row=14, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_min_value,
                                text='The minimum allowed response multiplier. Response multipliers below this value will be clamped to this value.')
response_min_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_min_value, response_min_value, response_min_value_l, style), "%P"))

# response_mutate_power
response_mutate_power_l = tk.Label(tab1, text="Mutate response power:")
response_mutate_power_l.grid(row=15, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_power_l,
                                text='The standard deviation of the zero-centered normal/gaussian distribution from which a response multiplier mutation is drawn.')

response_mutate_power = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_mutate_power")
response_mutate_power.grid(row=15, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_power,
                                text='The standard deviation of the zero-centered normal/gaussian distribution from which a response multiplier mutation is drawn.')
response_mutate_power.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_mutate_power, response_mutate_power, response_mutate_power_l, style), "%P"))

# response_mutate_rate
response_mutate_rate_l = tk.Label(tab1, text="Mutate response rate:")
response_mutate_rate_l.grid(row=16, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_rate_l,
                                text='The probability that mutation will change the response multiplier of a node by adding a random value.')

response_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_mutate_rate")
response_mutate_rate.grid(row=16, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_power,
                                text='The probability that mutation will change the response multiplier of a node by adding a random value.')
response_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_mutate_rate, response_mutate_rate, response_mutate_rate_l, style), "%P"))

# response_replace_rate
response_replace_rate_l = tk.Label(tab1, text="Response response rate:")
response_replace_rate_l.grid(row=17, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_replace_rate_l,
                                text='The probability that mutation will change the response multiplier of a node by adding a random value.')

response_replace_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_replace_rate")
response_replace_rate.grid(row=17, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_replace_rate,
                                text='The probability that mutation will change the response multiplier of a node by adding a random value.')
response_replace_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_replace_rate, response_replace_rate, response_replace_rate_l, style), "%P"))

# single_structural_mutation
single_structural_mutation_L = tk.Label(tab1, text="Singe structural mutation?")
single_structural_mutation_L.grid(row=18, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(single_structural_mutation_L,
                                text='If this evaluates to True, only one structural mutation (the addition or removal of a node or connection) will be allowed per genome per generation. (If the probabilities for conn_add_prob, conn_delete_prob, node_add_prob, and node_delete_prob add up to over 1, the chances of each are proportional to the appropriate configuration value.) This defaults to “False”.')

single_structural_mutation = ttk.Combobox(tab1, name="single_structural_mutation")
single_structural_mutation['values'] = ('True', 'False')
single_structural_mutation.grid(row=18, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(single_structural_mutation,
                                text='If this evaluates to True, only one structural mutation (the addition or removal of a node or connection) will be allowed per genome per generation. (If the probabilities for conn_add_prob, conn_delete_prob, node_add_prob, and node_delete_prob add up to over 1, the chances of each are proportional to the appropriate configuration value.) This defaults to “False”.')
single_structural_mutation.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(single_structural_mutation, single_structural_mutation, single_structural_mutation_L,
                            style), "%P"))

# structural_mutation_surer
structural_mutation_surer_L = tk.Label(tab1, text="Structural mutation surer?")
structural_mutation_surer_L.grid(row=19, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(structural_mutation_surer_L,
                                text='f this evaluates to True, then an attempt to add a node to a genome lacking connections will result in adding a connection instead; furthermore, if an attempt to add a connection tries to add a connection that already exists, that connection will be enabled. If this is set to default, then it acts as if it had the same value as single_structural_mutation (above). This defaults to “default”.')

structural_mutation_surer = ttk.Combobox(tab1, name="structural_mutation_surer")
structural_mutation_surer['values'] = ('True', 'False', 'default')
structural_mutation_surer.grid(row=19, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(structural_mutation_surer_L,
                                text='f this evaluates to True, then an attempt to add a node to a genome lacking connections will result in adding a connection instead; furthermore, if an attempt to add a connection tries to add a connection that already exists, that connection will be enabled. If this is set to default, then it acts as if it had the same value as single_structural_mutation (above). This defaults to “default”.')
structural_mutation_surer.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(structural_mutation_surer, structural_mutation_surer, structural_mutation_surer_L, style),
"%P"))

# Weight Values
weight_l = tk.Label(tab1, text='Weight Values', font='Helvetica 11 bold')
weight_l.grid(row=20, column=5, pady=5, sticky=tk.W)

# weight_init_mean
weight_init_mean_l = tk.Label(tab1, text="Mean weight:")
weight_init_mean_l.grid(row=21, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_mean_l,
                                text='The mean of the normal/gaussian distribution used to select weight attribute values for new connections.')

weight_init_mean = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_init_mean")
weight_init_mean.grid(row=21, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_mean,
                                text='The mean of the normal/gaussian distribution used to select weight attribute values for new connections.')
weight_init_mean.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_init_mean, weight_init_mean, weight_init_mean_l, style), "%P"))

# weight_init_stdev
weight_init_stdev_l = tk.Label(tab1, text="Standard weight:")
weight_init_stdev_l.grid(row=22, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_stdev_l,
                                text='The standard deviation of the normal/gaussian distribution used to select weight values for new connections.')

weight_init_stdev = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_init_stdev")
weight_init_stdev.grid(row=22, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_stdev,
                                text='The standard deviation of the normal/gaussian distribution used to select weight values for new connections.')
weight_init_stdev.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_init_stdev, weight_init_stdev, weight_init_stdev_l, style), "%P"))

# weight_init_type
weight_init_type_L = tk.Label(tab1, text="Weight Type")
weight_init_type_L.grid(row=23, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_type_L,
                                text='If set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(weight_min_value,(weight_init_mean−(weight_init_stdev∗2))) to min(weight_max_value,(weight_init_mean+(weight_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')

weight_init_type = ttk.Combobox(tab1, name="weight_init_type")
weight_init_type['values'] = ('gaussian', 'normal', 'uniform')
weight_init_type.grid(row=23, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_type,
                                text='If set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(weight_min_value,(weight_init_mean−(weight_init_stdev∗2))) to min(weight_max_value,(weight_init_mean+(weight_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')
weight_init_type.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_init_type, weight_init_type, weight_init_type_L, style), "%P"))

# weight_max_value
weight_max_value_l = tk.Label(tab1, text="Max weight:")
weight_max_value_l.grid(row=24, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_max_value_l,
                                text='The maximum allowed weight value. Weights above this value will be clamped to this value.')

weight_max_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_max_value")
weight_max_value.grid(row=24, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(weight_max_value,
                                text='The maximum allowed weight value. Weights above this value will be clamped to this value.')
weight_max_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_max_value, weight_max_value, weight_max_value_l, style), "%P"))

# weight_min_value
weight_min_value_l = tk.Label(tab1, text="Min weight:")
weight_min_value_l.grid(row=25, column=5, sticky=tk.W, ipady=2)
CreateHelpMessage.CreateToolTip(weight_min_value_l,
                                text='The minimum allowed weight value. Weights below this value will be clamped to this value.')

weight_min_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_min_value")
weight_min_value.grid(row=25, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(weight_min_value_l,
                                text='The minimum allowed weight value. Weights below this value will be clamped to this value.')
weight_min_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_min_value, weight_min_value, weight_min_value_l, style), "%P"))

# weight_mutate_power
weight_mutate_power_l = tk.Label(tab1, text="Weight Mutate power:")
weight_mutate_power_l.grid(row=26, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_power_l,
                                text='The standard deviation of the zero-centered normal/gaussian distribution from which a weight value mutation is drawn.')

weight_mutate_power = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_mutate_power")
weight_mutate_power.grid(row=26, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_power,
                                text='The standard deviation of the zero-centered normal/gaussian distribution from which a weight value mutation is drawn.')
weight_mutate_power.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_mutate_power, weight_mutate_power, weight_mutate_power_l, style), "%P"))

# weight_mutate_rate
weight_mutate_rate_l = tk.Label(tab1, text="Weight Mutate rate:")
weight_mutate_rate_l.grid(row=27, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_rate_l,
                                text='The probability that mutation will change the weight of a connection by adding a random value.')

weight_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_mutate_rate")
weight_mutate_rate.grid(row=27, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_rate,
                                text='The probability that mutation will change the weight of a connection by adding a random value.')
weight_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_mutate_rate, weight_mutate_rate, weight_mutate_rate_l, style), "%P"))

# weight_replace_rate
weight_replace_rate_l = tk.Label(tab1, text="Weight replace rate:")
weight_replace_rate_l.grid(row=28, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_replace_rate_l,
                                text='The probability that mutation will replace the weight of a connection with a newly chosen random value (as if it were a new connection).')

weight_replace_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_replace_rate")
weight_replace_rate.grid(row=28, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_replace_rate,
                                text='The probability that mutation will replace the weight of a connection with a newly chosen random value (as if it were a new connection).')
weight_replace_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_replace_rate, weight_replace_rate, weight_replace_rate_l, style), "%P"))

tabControl.grid(row=0, column=0)

# Editor
frame2 = tk.Frame(master=root, width=500, height=600)
frame2.grid(row=0, column=2)

frame2.rowconfigure(0, minsize=900, weight=1)  # row where buttons are
frame2.columnconfigure(1, minsize=900, weight=1)  # column where buttons are

txt_edit = tk.Text(frame2)

fr_buttons = tk.Frame(frame2, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
reset_btn = tk.Button(fr_buttons, text="Default Config", command=reset_Editor)
default_config_btn = tk.Button(fr_buttons, text="Config Layout", command=default_config)
update_btn = tk.Button(fr_buttons, text="Update Config", command=update_editor)

# Keep track of the button state on/off
# global is_on


# Define Our Images
on = tk.PhotoImage(file="on.png")
off = tk.PhotoImage(file="off.png")

# Create A Button
on_button = tk.Button(fr_buttons, image=off, bd=0,
                      command=switch)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
reset_btn.grid(row=2, column=0, sticky="ew", padx=5)
default_config_btn.grid(row=3, column=0, sticky="ew", padx=5)
update_btn.grid(row=4, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
on_button.grid(row=5, column=0, sticky="ne")


# Tab 2 --- Set up
tabControl.add(tab2, text = "NEAT Setup")

# Setup label
setup_neat_l = tk.Label(tab2, text='Setup label', font='Helvetica 12 bold underline', justify=LEFT, anchor="w")
setup_neat_l.grid(row=0, column=0, ipadx=32, pady=1)

# Select game
game_selection_l = tk.Label(tab2, text="Gym Game:", justify=LEFT, anchor="w")
game_selection_l.grid(row=1, column=0,ipadx=37, pady=2)

game_selection = ttk.Combobox(tab2, name="game_selection")
game_selection['values'] = ('SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0","Breakout-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo")
game_selection.grid(row=1, column=1)

# Select evalutation
game_evaluation_l = tk.Label(tab2, text="Evaluate Genomes:", justify=LEFT, anchor="w")
game_evaluation_l.grid(row=2, column=0,ipadx=37, pady=2)

game_evaluation = ttk.Combobox(tab2, name="game_evaluation")
game_evaluation['values'] = ("Single-Processing", "Multi-Processing")
game_evaluation.grid(row=2, column=1)

# Winner file name
winner_file_name_l = tk.Label(tab2, text="Winner file name:", justify=LEFT, anchor="w")
winner_file_name_l.grid(row=3, column=0,ipadx=37, pady=2)

winner_file_name = tk.Text(tab2, name="winner_file_name", height = 0.5, width =17)
winner_file_name.grid(row=3, column=1)

# Checkpoints
game_checkpoint_l = tk.Label(tab2, text="Save Checkpoint:", justify=LEFT, anchor="w")
game_checkpoint_l.grid(row=4, column=0,ipadx=37, pady=2)

game_checkpoint = ttk.Spinbox(tab2, from_=0, to=100000000, increment=1, name = "game_evaluation")
game_checkpoint.grid(row=4, column=1)

# Console
console_l = tk.Label(tab2, text="Enter command:", justify=LEFT, anchor="w")
console_l.grid(row=6, column=0,ipadx=37, pady=2)

build_in_console = tk.Text(tab2, name="build_in_console", height = 10, width =25)
build_in_console.grid(row=7, column=0)
build_in_console.bind("<Return>",Build_in_Console.Get_Console_input(build_in_console, game_selection))


# Reccurent / FeedForward network
network_type_l = tk.Label(tab2, text="Network Type:", justify=LEFT, anchor="w")
network_type_l.grid(row=5, column=0,ipadx=37, pady=2)

network_type = ttk.Combobox(tab2, name="network_type")
network_type['values'] = ("Feed-forward ", "Recurrent")
network_type.grid(row=5, column=1)

# Color LightMode program
for label in labels_list:  # Loop though Labels
    exec(label + '.config(fg = "gray1", bg = "grey75")')
for button in buttons_list:
    exec(button + ".configure(bg = 'purple4', fg= 'gray99')")
txt_edit.config(bg="light grey", fg="gray1")
fr_buttons.configure(bg="red4")
on_button.configure(bg="red4", activebackground='red4')
root.config(bg='red4')
# Tab Style
style.theme_use('default')
style.configure('TNotebook.Tab', background="gray47")
style.configure("TNotebook", background="gray24", borderwidth=0)
# style.configure("TNotebook.Tab", background="green", foreground=COLOR_3,, borderwidth=2)
# Style of form (background), no foreground
style.configure("TFrame", background="grey75", borderwidth=5)
style.configure("TCombobox", fieldbackground="grey85", background="red4", foreground="gray1")
style.configure("TSpinbox", fieldbackground="grey85", background="red4", foreground="gray1")
style.configure("TCheckbutton", fieldbackground="MediumPurple1", background="grey35",
                foreground="white smoke")
# this changes the background colour of the 2nd item
for options in range(len(aggregation_options)):
    listbox_aggregation_options.itemconfig(options, {'bg': 'grey85'})
for activation_option in range(len(activation_options_values_sec)):
    activation_listbox.itemconfig(activation_option, {'bg': "grey85"})

root.mainloop()
