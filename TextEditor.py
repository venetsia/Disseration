import logging
import os
import re
import sys
import threading
import tkinter as tk
from multiprocessing import Pool
from pathlib import Path
from tkinter.filedialog import askopenfilename, asksaveasfilename, LEFT#, VERTICAL
from tkinter import ttk, INSERT, END, SE, filedialog
from tkinter.messagebox import showinfo
from tkinter import messagebox

import StickyNote
import gym
#import pyautogui
import CreateHelpMessage
from time import gmtime, strftime
import ctypes  # An included library with Python install.
import Education_Tab
import Get_Directory_For_Neat
import NEAT_Single_Processing
import ProcessImages
import Run_winner
import ValidateInput
import Build_in_Console
import Validate_Neat_Setup
#import pyglet
from concurrent.futures import ThreadPoolExecutor
from CustonText import CustomText
import gym.envs.classic_control
import gym.envs.box2d
import atari_py.ale_interface
import atari_py.ale_python_interface
import atari_py
import gym.envs.atari.atari_env
import gym.envs.atari
from StickyNote import StickyNotes

game_list_2D = ["LunarLander-v2", "CartPole-v1"]
game_list_atari = ['SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0", 'Freeway-v0',
                   'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo", "Pong-v0",
                   "Alien-v0", "Asterix-v0", "Asteroids-v0", "Amidar-v0",
                   "Assault-v0", "Atlantis-v0", "BattleZone-v0", "Carnival-v0",
                   "Centipede-v0", "DemonAttack-v0", "JourneyEscape-v0",
                   "Phoenix-v0", "Pooyan-v0", "StarGunner-v0",
                   "TimePilot-v0", "UpNDown-v0"]
Start_NEAT_Config = False
NEAT_Config_Beginner_Level = False

# Create at startup
education_mode = False
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

# Label list used to modify DarkMode and Light Mode
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
               "weight_replace_rate_l", "random_from_form_l"]
other_tabs_labels = ["game_selection_l", "setup_neat_l", "winner_file_name_l","game_evaluation_l", "game_checkpoint_l", "console_l", "network_type_l", "choose_config_file_l",
               "directory_value_l", "directory_value_l", "render_window_l", "setup_neat_l_Winner", "winner_file_name_l_winner", "game_checkpoint_l_winner",
               "checkpoint_directory_value_l_winner", "network_type_l_winner", "directory_value_l_winner" , "choose_config_file_l_winner",
               "setup_neat_l_Winner", "game_selection_l_Winner", "game_selection_config_l", "runs_per_network_l", "config_file_check", "num_generations_l", "random_from_form_l", "number_of_genomes_l"]
# Button list used to modify Dark Mode and Light Mode
buttons_list = ["btn_open", "btn_save", "default_values_config_btn", "get_empty_config_btn", "update_btn", "btn_run_neat", "btn_run_neat_winner", "btnFind" , "btnFind_winner"]
# Used for looping though all Editor form values
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
                    "weight_replace_rate", "random_from_form", "game_selection_config"]
education_mode_labels = ["label1", "label2", "chat_bot_dynamic_learn"]
education_mode_button = ["chatbot_next", "check_answer", "neuron_tab_label", "perceptron_label"]

# NEAT Sections separated into different List for smarter assignment when values do not exist in Config
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
                    "response_mutate_power", "response_replace_rate", "response_mutate_rate"]
weight_values = ["weight_init_mean",
                 "weight_init_stdev", "weight_init_type", "weight_max_value", "weight_min_value", "weight_mutate_power",
                 "weight_mutate_rate",
                 "weight_replace_rate"]
structure_options = ["single_structural_mutation", "structural_mutation_surer"]
logging.basicConfig(filename="logfilename.log", level=logging.INFO)
run_NEAT_thread = ""
load_winner_thread =""
games_available = ['SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo", "LunarLander-v2", "Pong-v0", "CartPole-v1"]

workers = 1

thread_pool_executor = ThreadPoolExecutor(max_workers=1)

# Print how many inputs are expected from the game in RUN neat so user knows what is changed to what
def print_selection():
    if game_selection.get() != "":
        text = game_selection.get()
        env = gym.make(text)
        outputs = env.action_space
        int_output = re.search(r'\d+', str(outputs)).group()
        if (var1.get() == 1) & (var2.get() == 0):
            if text in games_available:
                build_in_console.delete('1.0', END)
                if text in game_list_2D:
                    start = ', ('
                    end = ',)'
                    env_ob_space = env.observation_space
                    string_space = str(env_ob_space)
                    int_input = string_space[str(string_space).find(start) + len(start):str(string_space).rfind(end)]
                    build_in_console.insert(END,"Input for game: " + text +"\nInputs: " + int_input + "\nOutputs: " + str(int_output) + "\nThe config file will be checked inputs and outputs")
                else:
                    build_in_console.insert(END,
                                            "Input for game: " + text + "\nInputs: 1092\nOutputs: " + str(
                                                int_output) + "\nThe config file will be checked inputs and outputs")

# Delete any special symbols from winner name that will be used on writing time (real time)
def Validate_Text_Widget_Neat(event):
    #print(event.widget._name)
    if event.widget._name == "winner_file_name":
        winner_file_name_text = re.sub(r'[^\w]', '', winner_file_name.get("1.0", END))
        winner_file_name.delete('1.0', END)
        winner_file_name.insert(END, winner_file_name_text)
    elif event.widget._name == "winner_file_name_winner":
        winner_file_name_text1 = re.sub(r'[^\w]', '', winner_file_name_winner.get("1.0", END))
        winner_file_name_winner.delete('1.0', END)
        winner_file_name_winner.insert(END, winner_file_name_text1)

# Open File
# Restricts to .txt files
# Groups all of the config values and puts them together in a nice way,
# this also helps user see what is where and helps algorithm to easily find values after
def open_file():
    """Open a file for editing."""

    # Restrict to .txt files
    # askopenfilename opens a File Dialog (from Tkinter)
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # Lists that are empty prior and will be filled with values existing in config file loaded
    # Will be compared with lists containing forms so they are assigned correctly to list
    neat_s_list =[]
    default_stagnation_list = []
    activation_list = []
    default_reproduction_list=[]
    network_parameters_list = []
    aggregation_list = []
    node_bias_list = []
    genome_comp_list = []
    connection_list = []
    response_list = []
    weight_list = []
    structure_list = []

    # If File path does not exist - return
    if not filepath:
        return

    # Delete whatever is in text_edit (Editor Text Widget)
    txt_edit.delete(1.0, tk.END)

    # Open file
    with open(filepath, "r") as input_file:
        text = input_file.read() # Read file
        # Loop though form values
        for form_input in form_values_list:
            num_line = 0
            # Split lines in text editor via new line
            for line in text.split("\n"):
                num_line += 1
                # If a form input is found in line
                if line.find(form_input) == 0:
                    # all of the if and else statement seperate form inputs into a list
                    # form input is checked whether or not it exists in lists created
                    # (lists are separated for smarter separation)
                    if form_input in neat_selection:
                        neat_s_list.append(line + "\n")
                    elif form_input in default_stagnation:
                        default_stagnation_list.append(line + "\n")
                    elif form_input in default_reproduction:
                        default_reproduction_list.append(line + "\n")
                    elif form_input in network_parameters or "num_inputs" in line:
                        network_parameters_list.append(line + "\n")
                    elif form_input in activation_section:
                        activation_list.append(line + "\n")
                    elif form_input in aggregation_section:
                        aggregation_list.append(line + "\n")
                    elif form_input in node_bias_section:
                        node_bias_list.append(line + "\n")
                    elif form_input in genome_comp_option:
                        genome_comp_list.append(line + "\n")
                    elif form_input in connection_options:
                        connection_list.append(line + "\n")
                    elif form_input in response_options:
                        response_list.append(line + "\n")
                    elif form_input in weight_values:
                        weight_list.append(line + "\n")
                    elif form_input in structure_options:
                        structure_list.append(line + "\n")

        # Reverse lists
        neat_s_list.reverse()
        default_stagnation_list.reverse()
        default_reproduction_list.reverse()
        network_parameters_list.reverse()
        activation_list.reverse()
        aggregation_list.reverse()
        node_bias_list.reverse()
        genome_comp_list.reverse()
        connection_list.reverse()
        response_list.reverse()
        weight_list.reverse()
        structure_list.reverse()

        # List that will contain all form inputs and assigned values
        # (Includes the whole line if form value is found)
        # This list is filled with the form values and how they are separated
        # via sections either [] or #

        # NEAT
        global_list_values = ["[NEAT]\n"]
        # using list comprehension to combine into a string
        neat_list_string = ' '.join(map(str, neat_s_list))
        # Add to global list
        global_list_values.append(neat_list_string)
        # Default Stagnation
        global_list_values.append("\n[DefaultStagnation]\n")
        # using list comprehension to combine into a string
        default_stagnation_list_string = ' '.join(map(str, default_stagnation_list))
        global_list_values.append(default_stagnation_list_string)
        global_list_values.append("\n[DefaultReproduction]\n")
        # using list comprehension to combine into a string
        reproduction_list_string = ' '.join(map(str, default_reproduction_list))
        global_list_values.append(reproduction_list_string)
        global_list_values.append("\n[DefaultGenome]\n")
        global_list_values.append("# Activation options\n")
        # using list comprehension to combine into a string
        activation_list_string = ' '.join(map(str, activation_list))
        global_list_values.append(activation_list_string)
        global_list_values.append("\n# Aggregation options\n")
        # using list comprehension to combine into a string
        aggregation_list_string = ' '.join(map(str, aggregation_list))
        global_list_values.append(aggregation_list_string)
        global_list_values.append("\n# Bias options\n")
        # using list comprehension to combine into a string
        bias_list_string = ' '.join(map(str, node_bias_list))
        global_list_values.append(bias_list_string)
        global_list_values.append("\n# Compatibility options\n")
        # using list comprehension to combine into a string
        compatibility_list_string = ' '.join(map(str, genome_comp_list))
        global_list_values.append(compatibility_list_string)
        global_list_values.append("\n# Connection options\n")
        # using list comprehension to combine into a string
        connection_list_string = ' '.join(map(str, connection_list))
        global_list_values.append(connection_list_string)
        global_list_values.append("\n# Network parameters\n")
        # using list comprehension to combine into a string
        netowork_list_string = ' '.join(map(str, network_parameters_list))
        global_list_values.append(netowork_list_string)
        global_list_values.append("\n# Response options\n")
        # using list comprehension to combine into a string
        response_list_string = ' '.join(map(str, response_list))
        global_list_values.append(response_list_string)
        global_list_values.append("\n# Structure options\n")
        # using list comprehension to combine into a string
        structure_list_string = ' '.join(map(str, structure_list))
        global_list_values.append(structure_list_string)
        global_list_values.append("\n# Weight options\n")
        # using list comprehension to combine into a string
        weight_list_string = ' '.join(map(str, weight_list))
        global_list_values.append(weight_list_string)

        # using list comprehension to combine into a string
        listToStr = ' '.join(map(str, global_list_values))

        # Remove any whitespaces in the beginning of the line
        emptylisttostring = ""
        for line in listToStr.split("\n"):
            line = line.lstrip()
            emptylisttostring = emptylisttostring + line + "\n"

        txt_edit.insert(tk.END, emptylisttostring)

# When user presses X on Window it will ask if he/she wants to quit
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()
        root.destroy()
        exit()

# Save the config file from Editor
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

# Notifies user what values he/ she has chosen from listboxes (aggregation_list and actication_list)
def items_selected(event):
    """ handle item selected event
    """
    # get selected indices
    selected_indices = activation_listbox.curselection()
    selected_indices_aggregation = listbox_aggregation_options.curselection()
    selected_education_list = Education_listbox.curselection()
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

        #ttk.update_idletasks()

# Add Default assigned value to editor (Information gained from NEAT Python website)
def default_values_config():
    # Delete whole txt box
    txt_edit.delete("1.0", "end")
    # Insert the text
    txt_edit.insert(INSERT, default_text_editor)

# Get Editor Config - empty config file
def get_empty_config():
    # Delete whole txt box
    txt_edit.delete("1.0", "end")
    # Insert the text
    txt_edit.insert(INSERT, text_editor)

# values that are not found in Editor are added via this insert function on a specific line (grouped - check the lists)
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

# RUN NEAT - pre-processing
def run_NEAT(Output_Console,game_selection, game_evaluation, winner_file_name, game_checkpoint, network_type, directory_value, render_window, runs_per_network, num_generations, choose_config_file):
    # Make sure the algorithm does not start if these are empty (game, evaluation, wiinner file name or directory where config is
    if game_selection.get() == "" or game_evaluation.get() == "" or winner_file_name.compare("end-1c", "==",
                                                                                             "1.0") or directory_value.get(
            "1.0", END) == "":
        return
    # Get path for config file
    config_path = directory_value.get("1.0", END)
    # Fix path string
    path_new = NEAT_Single_Processing.raw(config_path)
    new_file_content = ""
    # The whole if statement is used for modifying the config file
    if game_selection.get() != "" and game_selection.get() in games_available: # If the game is valid:
        text = game_selection.get() # Get text from form box
        env = gym.make(text)    # Make Game
        outputs = env.action_space # Get Output - actions available
        env_ob_space = env.observation_space # Inputs
        string_space = str(env_ob_space) # Convert to string
        # Get Integers from the value
        int_output = re.search(r'\d+', str(outputs)).group()
        # If CheckBox is selected - if yes, then config file will be modified
        if (var1.get() == 1) & (var2.get() == 0):
            Output_Console.insert(END, "Config file is being modified (inputs and outputs). One moment please")
            if text in games_available: # If the game is valid
                # Open file to read it
                file = open(path_new, "r")
                # For each line in file
                for line in file:
                    # Check if num_inputs is found
                    if 'num_inputs' in line:
                        # Check if game is a Box2D game
                        if text in game_list_2D:
                            # Moderate the input string
                            start = ', ('
                            end = ',)'
                            # Get string between ", (" and ",)"
                            int_input= string_space[str(string_space).find(start) + len(start):str(string_space).rfind(end)]
                            # Replace the line with the correct inputs needed
                            new_line = line.replace(line, "num_inputs = " + int_input + "\n")
                            # Add new line into the file content
                            new_file_content += new_line
                        else:
                            # If game is not a Box2D game it is most likely an Atari Game
                            # Algorithm has been written to use 1092 inputs for Atari games
                            new_line = line.replace(line,"num_inputs = 1092\n")
                            # Add new line into the file content
                            new_file_content += new_line
                    # Check if num_output is found in line
                    elif 'num_outputs' in line:
                        # Replace the line with correct output value needed
                        new_line = line.replace(line,"num_outputs = " + int_output + "\n")
                        # Add new line to file
                        new_file_content += new_line
                    else:
                        # Add other non-modified lines as well
                        new_file_content += line
                # Open same file but in write mode
                writing_file = open(path_new, "w")
                # Replace the whole text with new content
                writing_file.write(new_file_content)
                # close file
                writing_file.close()


    global run_NEAT_thread
    run_NEAT_thread = threading.current_thread()

    # If nothing is chosen do not render
    if render_window.get() == "":
        render_window.set("False")
    # If nothing is chosen, do Feed-Forward
    if network_type.get() == "":
        network_type.set("Feed-forward")
    # If nothing is chosen, choose 0
    if game_checkpoint.get() == "":
        game_checkpoint.set("0")
    if num_generations.winfo_ismapped() == True:
        if num_generations.get() == "":
            num_generations.set("1")
    else:
        num_generations.set("0")

    # Logging information
    logging.info(f'Time: {strftime("%Y-%m-%d %H:%M:%S", gmtime())}')
    logging.info(f'Game selection is: {game_selection.get()}')
    logging.info(f'Game evaluation is: {game_evaluation.get()}')
    logging.info(f'Winner file name is: {NEAT_Single_Processing.raw(winner_file_name.get("1.0", END))}')
    logging.info(f'The network type is: {network_type.get()}')
    logging.info(f'Checkpoints after {str(game_checkpoint.get())} generations')
    logging.info(f'Config file is located in: {NEAT_Single_Processing.raw(directory_value.get("1.0", END))}\n\n')

    # Check if evaluation is Single Processing and game is either an Atari or Box2D game
    if game_evaluation.get() == "Single-Processing" and (game_selection.get() in game_list_atari or game_selection.get() in game_list_2D):
        NEAT_Single_Processing.run_Program(Output_Console, game_selection, winner_file_name, game_checkpoint,
                                           network_type,
                                           directory_value, render_window, runs_per_network, num_generations, choose_config_file)

    return

# Submit task to threadpool so Main app still works
# ThreadPool only has one thread because of the rendering library
# Once rendering library is applied to a thread it cannot be moved acros so if
# thread is closed for example, rendering will not be able to happen
# That is why we are submitting the task onto a threadpool with one thread
# that is designed for rendering
# RUN Neat - Train Neural Network
def submit_to_thread_pool_run_neat(Output_Console,game_selection, game_evaluation, winner_file_name, game_checkpoint, network_type, directory_value, render_window, runs_per_network, num_generations, choose_config_file):
    thread_pool_executor.submit(run_NEAT,Output_Console,game_selection, game_evaluation, winner_file_name, game_checkpoint, network_type, directory_value, render_window, runs_per_network, num_generations, choose_config_file)

# Function to load Winner and Checkpoints from NEAT
def load_winner(Output_Console_winner, game_selection_winner, winner_file_name_winner, num_of_episodes_per_genome_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner, number_of_genomes):
    # Change print statement to go to normal console
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    # if Game is empty, winner file name is empty or the directory - do not continue
    if game_selection_winner.get() == "" or winner_file_name_winner.compare("end-1c", "==",
                                                                            "1.0") or directory_value_winner.get(
        "1.0", END) == "":
        return
    # This is Number of Episodes per Genome if none is selected it should be set to 1
    if num_of_episodes_per_genome_winner.get() is None or len(num_of_episodes_per_genome_winner.get()) == 0 or num_of_episodes_per_genome_winner.get() == "0" or num_of_episodes_per_genome_winner.index("end") == 0:
        num_of_episodes_per_genome_winner.set("1")

    #Run Winner Genome
    Run_winner.pre_process_data(Output_Console_winner, game_selection_winner, winner_file_name_winner, num_of_episodes_per_genome_winner,
                                checkpoint_directory_value_winner, network_type_winner, directory_value_winner, number_of_genomes)
    # Change print statement to go to normal console
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    return

# Submit task to threadpool so Main app still works
# ThreadPool only has one thread because of the rendering library
# Once rendering library is applied to a thread it cannot be moved acros so if
# thread is closed for example, rendering will not be able to happen
# That is why we are submitting the task onto a threadpool with one thread
# that is designed for rendering
# Run Winner Genome and checkpoints if any
def submit_to_thread_pool_load_winner(Output_Console_winner,game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner, number_of_genomes ):
    thread_pool_executor.submit(load_winner, Output_Console_winner,game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner, number_of_genomes)

# Loading files sorted by alphabet and number
# Credits to https://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python
# Martijn Pieters♦
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
# Applies values from one tab to another tab so it is more automated
def on_tab_change(event):
    # Load configuration.
    local_dir = os.path.dirname(__file__)
    current_directory = os.path.abspath(os.getcwd())
    checkpoint_directory_value_winner.delete('1.0', END)
    game_checkpoint_winner.set("1")
    hidden_level_value = hidden_level_text.get(1.0, tk.END)
    if tabControl.index(tabControl.select()) == 3:
        try:
            if game_selection.get() != "":
                game_selection_winner.set(game_selection.get())
            if network_type.get() != "":
                network_type_winner.set(network_type.get())
            if checkpoint_directory_value_winner.get("1.0", END) == "" and hidden_level_value != "LoadWinnerExample\n" and hidden_level_value == "LoadWinnerExample2\n":
                arr = os.listdir(current_directory)
                # Gets all the checkpints in the directory and sepeartes them
                for file in (sorted(arr, key=numericalSort)):
                    if file.find("neat-checkpoint") == 0:
                        checkpoint_winners = os.path.join(current_directory, file)
                        checkpoint_directory_value_winner.insert(END,"~ " + checkpoint_winners + "\n")
            choose_config_file_winner.set("Automatic")
            if directory_value.get("1.0", END) != "":
                directory_value_winner.configure(state='normal')
                directory_value_winner.delete('1.0', END)
                directory_value_winner.insert(INSERT, directory_value.get("1.0",END))
                directory_value_winner.configure(state='disabled')
            if winner_file_name.compare("end-1c", "!=", "1.0"):
                winner_file_name_winner.delete('1.0', END)
                winner_file_name_winner.insert(INSERT, winner_file_name.get("1.0", END))
        except:
            pass

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
                elitism_value = eval(str(form_input) + ".get()")
                if elitism_value != "":
                    for line in thetext.split("\n"):
                        num_line += 1
                        if line.find("elitism") == 0:
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
                elitism_value = eval(str(form_input) + ".get()")
                if elitism_value != "":
                    for line in thetext.split("\n"):
                        num_line += 1
                        if line.find("species_elitism") == 0:
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
                            txt_edit.delete(float(num_line), float(num_line) + 1.0)
                            txt_edit.insert(float(num_line), form_input + " = " + eval(str(form_input) + ".get()") + "\n")
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
                            txt_edit.insert(float(num_line_0),
                                            "elitism = " + eval(str(non_added_value) + ".get()") + "\n")
                        else:
                            insert(num_line_0, non_added_value)
            elif non_added_value in genome_section:
                num_line_0 = 0
                for line in thetext.split("\n"):
                    num_line_0 += 1
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
# switches from Normal view to Education and back
def switch_modes():
    global education_mode
    if education_mode == True:
        education_mode = False
        education_mode_normal_mode.config(image=education_mode_pic)
        frame_Education.grid_remove()
        education_L.grid_remove()
        Education_listbox.grid_remove()
        save_progress_btn.grid_remove()
        reset_progress_btn.grid_remove()
        tabControl.tab(tab_education, state="disabled")

        for label in labels_list:
            try:
                exec(label + '.grid()')
            except:
                pass
        for form_value in form_values_list:
            try:
                exec(form_value + '.grid()')
            except:
                pass

        root.mainloop()
    else:
        education_mode = True
        progress_Bar_Education = ttk.Progressbar(
            frame_Education,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        education_mode_normal_mode.config(image=normal_mode_pic)
        frame_Education.grid()
        education_L.grid()
        tabControl.tab(tab_education, state="normal")
        Education_listbox.grid()
        # Run button for Neat using a thread
        save_progress_btn.grid()

        # Run button for Neat using a thread
        reset_progress_btn.grid()

        root.mainloop()
def getFolderPath():
    try:
        folder_selected = filedialog.askdirectory()
        local_dir = folder_selected
        checkpoint_directory_value_winner.delete('1.0', END)
        arr = os.listdir(local_dir)
        # Gets all the checkpints in the directory and sepeartes them
        if len(arr) != 0:
            number_of_genomes_l.grid()
            number_of_genomes.grid()
        for file in (sorted(arr, key=numericalSort)):
            if file.find("neat-checkpoint") == 0:
                checkpoint_winners = os.path.join(local_dir, file)
                checkpoint_directory_value_winner.insert(END, "~ " + checkpoint_winners + "\n")
    except:
        pass
def getFolderPath_and_File():
    file_selected = filedialog.askopenfilename()
    local_dir = file_selected

    winner_file_name_winner.delete(1.0, END)
    winner_file_name_winner.insert(END, local_dir)
# Define our switch function - switches between Dark mode and Light Mode
def switch():
    # colors found at: http://tephra.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png
    global is_on
    #global education_mode
    # DarkMode is on or off
    if is_on == True:  # Light Mode
        on_button.config(image=off)
        is_on = False
        # on_button.config(image=on)
        # is_on = True
        # Labels
        # Color LightMode program
        # Color LightMode program
        for label in labels_list:  # Loop though Labels
            exec(label + '.config(fg = "gray1", bg = "grey75")')
        for label_o in other_tabs_labels:  # Loop though Labels
            exec(label_o + '.config(fg = "gray1", bg = "grey75")')
        for button in buttons_list:
            exec(button + ".configure(bg = '#32285b', fg= 'gray99')")

        config_file_check.configure(activebackground="grey75")
        txt_edit.config(bg="light grey", fg="gray1")
        winner_file_name.config(bg="#e5e5e5", fg="gray1")
        directory_value.config(bg="#e5e5e5", fg="gray1")
        build_in_console.config(bg="#e5e5e5", fg="gray1")
        Output_Console.config(bg="#e5e5e5", fg="gray1")
        winner_file_name_winner.config(bg="#e5e5e5", fg="gray1")
        checkpoint_directory_value_winner.config(bg="#e5e5e5", fg="gray1")
        directory_value_winner.config(bg="#e5e5e5", fg="gray1")
        Output_Console_winner.config(bg="#e5e5e5", fg="gray1")
        fr_buttons.configure(bg="#d9001f")
        on_button.configure(bg="#d9001f", activebackground='#d9001f')
        education_mode_normal_mode.configure(bg="#d9001f", activebackground='#d9001f')
        root.config(bg='#d9001f')
        # Tab Style
        style.theme_use('default')
        style.configure('TNotebook.Tab', background="#5d797e")
        style.configure("TNotebook", background="#333333", borderwidth=0)
        # style.configure("TNotebook.Tab", background="green", foreground=COLOR_3,, borderwidth=2)
        # Style of form (background), no foreground
        style.configure("TFrame", background="grey75", borderwidth=5)
        style.configure("TCombobox", fieldbackground="#e5e5e5", background="#d9001f", foreground="gray1")
        style.configure("TSpinbox", fieldbackground="#e5e5e5", background="#d9001f", foreground="gray1")
        style.configure("TCheckbutton", fieldbackground="#dcdcdc", bg="#dcdcdc",
                        foreground="gray1")
        # this changes the background colour of the 2nd item
        for options in range(len(aggregation_options)):
            listbox_aggregation_options.itemconfig(options, {'bg': '#dcdcdc'})
        for activation_option in range(len(activation_options_values_sec)):
            activation_listbox.itemconfig(activation_option, {'bg': "#dcdcdc"})

        # print(is_on)
    elif is_on == False:  # Dark Mode
        on_button.config(image=on)
        is_on = True
        # Labels
        for button in buttons_list:
            exec(button + ".configure(bg = 'dark slate gray', fg = '#dddbd9')")
        config_file_check.configure(activebackground="grey35")
        txt_edit.config(bg="#272726", fg="#dddbd9")
        winner_file_name.config(bg="#272726", fg="#dddbd9")
        build_in_console.config(bg="gray12", fg="#dddbd9")
        Output_Console.config(bg="#272726", fg="#dddbd9")
        winner_file_name_winner.config(bg="#272726", fg="#dddbd9")
        checkpoint_directory_value_winner.config(bg="#272726", fg="#dddbd9")
        directory_value_winner.config(bg="#272726", fg="#dddbd9")
        directory_value.config(bg="#272726", fg="#dddbd9")
        Output_Console_winner.config(bg="#272726", fg="#dddbd9")
        fr_buttons.configure(bg="gray18")
        on_button.configure(bg="gray18", activebackground='gray18')
        education_mode_normal_mode.configure(bg="gray18", activebackground='gray18')
        root.config(bg='gray24')
        # Tab Style
        style.theme_use('default')
        #style.configure('TNotebook.Tab', background="gray45")
        style.configure('TNotebook.Tab', background="#5d797e")
        #style.configure("TNotebook", background="#333333", borderwidth=0)
        style.configure("TNotebook", background="gray24", borderwidth=0)

        if education_mode == True:
            Education_Tab.DarkMode()
            for label in labels_list:  # Loop though Labels
                exec(label + '.config(fg = "grey1", bg = "grey75")')
            for label_o in other_tabs_labels:  # Loop though Labels
                exec(label_o + '.config(fg = "grey1", bg = "grey75")')
        else:
            for label in labels_list:  # Loop though Labels
                exec(label + '.config(fg = "white smoke", bg = "grey35")')
            for label_o in other_tabs_labels:  # Loop though Labels
                exec(label_o + '.config(fg = "white smoke", bg = "grey35")')
            style.configure("TFrame", background="grey35", borderwidth=5)
        # style.configure("TNotebook.Tab", background="green", foreground=COLOR_3,, borderwidth=2)
        # Style of form (background), no foreground

        #style.configure("TFrame", background="grey35", borderwidth=5)

       # style.configure("TFrame", background="grey75", borderwidth=5)
        style.configure("TCombobox", fieldbackground="#697676", background="#e5233f", foreground="#dddbd9")
        style.configure("TSpinbox", fieldbackground="#697676", background="#e5233f", foreground="#dddbd9")
        style.configure("TCheckbutton", fieldbackground="#697676", background="#dddbd9",
                        foreground="#cbc8c3")
        # this changes the background colour of the 2nd item
        for options in range(len(aggregation_options)):
            listbox_aggregation_options.itemconfig(options, {'bg': 'gray77'})
        for activation_option in range(len(activation_options_values_sec)):
            activation_listbox.itemconfig(activation_option, {'bg': "gray77"})

def onModification(event):
    current_directory = os.path.abspath(os.getcwd())
    chars = len(event.widget.get("1.0", "end-1c"))
    print(chars)
    hidden_level_value = hidden_level_text.get(1.0, tk.END)
    if hidden_level_value == "False\n" and education_mode == True:
        pass
    elif hidden_level_value == "Start_Go_to_Neat\n" and education_mode == True:

        for label in labels_list:
            exec(label + '.grid_remove()')
        for form_value in form_values_list:
            exec(form_value + '.grid_remove()')
        activation_listbox.grid_remove()
        listbox_aggregation_options.grid_remove()

        neat_section_L.grid()
        fitness_criterion_l.grid()
        fitness_criterion.grid()
        fitness_threshold_l.grid()
        fitness_threshold.grid()
        pop_size_l.grid()
        pop_size.grid()
        genome_Section_l.grid()
        network_Parameters_l.grid()
        num_inputs_l.grid()
        num_inputs.grid()
        num_outputs_l.grid()
        num_outputs.grid()
        game_selection_config_l.grid()
        game_selection_config.grid()

        # Set Focus on tab Neat Config
        tabControl.select(tab1)

        # Change selected List Box to be 'Load Winner/Checkpoints E1'
        Education_listbox.selection_clear(0, END)
        Education_listbox.selection_set(13)
        Education_listbox.event_generate("<<ListboxSelect>>")
    elif hidden_level_value == "LoadCartPoleExample\n" and education_mode == True:
        # Set Focus on tab Load Winner
        tabControl.select(tab3)
        # Load everything
        for label in labels_list:
            try:
                exec(label + '.grid()')
            except:
                pass
        for form_value in form_values_list:
            try:
                exec(form_value + '.grid()')
            except:
                pass
        activation_listbox.grid()
        listbox_aggregation_options.grid()

    elif hidden_level_value == "LoadLunarLanderExample\n" and education_mode == True:
        # Set Focus on tab Load Winner
        tabControl.select(tab3)

    elif hidden_level_value == "RunNeatExampleCartPole\n" and education_mode == True:
        # Set Focus on tab Load Winner
        tabControl.select(tab2)
        # Set Values in Load Winner for CartPole example
        game_selection.set("CartPole-v1")
        game_evaluation.set("Single-Processing")
        game_checkpoint.set("0")
        network_type.set("Feed-forward")
        directory_value.delete(1.0, tk.END)
        target_path_1 = current_directory + "/CartPoleExample/config-feedforwardCartPoleExample.txt"
        directory_value.configure(state='normal')
        directory_value.delete('1.0', END)
        directory_value.insert(END, target_path_1)
        directory_value.configure(state='disabled')
        runs_per_network_l.grid()
        runs_per_network.grid()
        runs_per_network.set("1")
        next_button = tk.Button(tab2, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "ExampleLevel1\n" and education_mode == True:
        fitness_criterion.set("max")
        fitness_threshold.set("500")
        pop_size.set("100")
        game_selection_config.set("CartPole-v1")
        num_inputs.set("4")
        num_outputs.set("2")
        next_button = tk.Button(tab1, text="Next",
                                 command=lambda: next_button_action(hidden_level_value),
                                 justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "LoadWinnerExample\n" and education_mode == True:
        next_button = tk.Button(tab3, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "LoadWinnerExample2\n" and education_mode == True:
        next_button = tk.Button(tab3, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "NoFitnessTerminationExample\n" and education_mode == True:
        for label in labels_list:
            exec(label + '.grid_remove()')
        for form_value in form_values_list:
            exec(form_value + '.grid_remove()')
        activation_listbox.grid_remove()
        listbox_aggregation_options.grid_remove()


        neat_section_L.grid()
        fitness_criterion_l.grid()
        fitness_criterion.grid()
        fitness_threshold_l.grid()
        fitness_threshold.grid()
        pop_size_l.grid()
        pop_size.grid()
        genome_Section_l.grid()
        network_Parameters_l.grid()
        num_inputs_l.grid()
        num_inputs.grid()
        num_outputs_l.grid()
        num_outputs.grid()
        game_selection_config_l.grid()
        game_selection_config.grid()
        no_fitness_termination_l.grid()
        no_fitness_termination.grid()
        no_fitness_termination.set("True")
        # Set Focus on tab Neat Config
        tabControl.select(tab1)
        num_generations_l.grid()
        num_generations.grid()
        game_selection.set("CartPole-v1")
        game_evaluation.set("Single-Processing")
        directory_value.configure(state='normal')
        directory_value.delete('1.0', END)
        target_path_1 = current_directory + "/No_Fitness_Termination_Example/configFeedForwardLunarLander_NoFitnessTerm.txt"
        directory_value.insert(END, target_path_1)
        directory_value.configure(state='disabled')
        network_type.set("Feed-forward")
        winner_file_name_l.config(fg="red")
        render_window_l.config(fg="black")
        render_window.set("False")
        next_button = tk.Button(tab1, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "NoFitnessTerminationExampleWithin\n" and education_mode == True:
        next_button = tk.Button(tab2, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "Atari_Example_1\n" and education_mode == True:
        for label in labels_list:
            exec(label + '.grid_remove()')
        for form_value in form_values_list:
            exec(form_value + '.grid_remove()')
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)
        except:
            pass
        neat_section_L.grid()
        fitness_criterion_l.grid()
        fitness_criterion.grid()
        fitness_threshold_l.grid()
        fitness_threshold.grid()
        pop_size_l.grid()
        pop_size.grid()
        genome_Section_l.grid()
        network_Parameters_l.grid()
        num_inputs_l.grid()
        num_inputs.grid()
        num_outputs_l.grid()
        num_outputs.grid()
        game_selection_config_l.grid()
        game_selection_config.grid()

        # Set Focus on tab Education
        tabControl.select(tab1)

        fitness_criterion.set("")
        fitness_threshold.set("")
        pop_size.set("")
        num_inputs.set("")
        num_outputs.set("")
        game_selection_config.set("")
        game_selection_config_l.config(fg="red")
        next_button = tk.Button(tab1, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)

        # Set Values in Load Winner for SpaceInvaders
        game_selection.set("SpaceInvaders-v0")
        game_evaluation.set("Single-Processing")
        game_checkpoint.set("0")
        network_type.set("Recurrent")
        directory_value.delete(1.0, tk.END)
        target_path_1 = current_directory + "/Atari_example_Space_invaders1/configfeedforwardSpaceInvadersExample.txt"
        directory_value.configure(state='normal')
        directory_value.delete('1.0', END)
        directory_value.insert(END, target_path_1)
        directory_value.configure(state='disabled')
        winner_file_name_winner.delete('1.0', END)
        target_path_1 = current_directory + '/Atari_example_Space_invaders1/winner_Space_Invaders'
        winner_file_name_winner.insert(END, target_path_1)
        runs_per_network_l.grid_remove()
        runs_per_network.grid_remove()
        winner_file_name_l.config(fg="red")
    elif hidden_level_value == "Atari_Example_within\n" and education_mode == True:
        next_button = tk.Button(tab3, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "Atari_Example_within_1\n" and education_mode == True:
        next_button = tk.Button(tab2, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
    elif hidden_level_value == "Atari_Example_within_2_feed_within\n" and education_mode == True:
        # Set Focus on tab Education
        tabControl.select(tab3)
        # Set Values in Load Winner for SpaceInvaders
        game_selection.set("SpaceInvaders-v0")
        game_evaluation.set("Single-Processing")
        game_checkpoint.set("0")
        network_type.set("Feed-forward")
        directory_value.delete(1.0, tk.END)
        target_path_1 = current_directory + "/Atari_Example_Space_Invaders2/configSpaceInvadersExample2.txt"
        directory_value.configure(state='normal')
        directory_value.delete('1.0', END)
        directory_value.insert(END, target_path_1)
        directory_value.configure(state='disabled')
        winner_file_name_winner.delete('1.0', END)
        target_path_1 = current_directory + '/Atari_Example_Space_Invaders2/Space_invaders-FeedForward_winner'
        winner_file_name_winner.insert(END, target_path_1)
        next_button = tk.Button(tab3, text="Next",
                                command=lambda: next_button_action(hidden_level_value),
                                justify=tk.LEFT, anchor="w")
        next_button.grid(row=40, column=0, sticky=tk.W, padx=5, pady=5)
def next_button_action(hidden_level_value):

    current_directory = os.path.abspath(os.getcwd())

    # Go Close Sticky page, go to education tab and select Load Winner/Checkpoint(s) E1
    if hidden_level_value == "ExampleLevel1\n" and education_mode == True:

        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)
        except:
            pass

        # Set Focus on tab Education
        tabControl.select(tab_education)

        #Change selected List Box to be 'Load Winner/Checkpoints E1'
        Education_listbox.selection_clear(0, END)
        Education_listbox.selection_set(15)
        Education_listbox.event_generate("<<ListboxSelect>>")

        # LoadWinnerExample
        hidden_level_text.delete(1.0, tk.END)
        print(hidden_level_text.get(1.0, tk.END))
        hidden_level_text.insert(tk.END, "LoadWinnerExample")
        print(hidden_level_text.get(1.0, tk.END))

        # Set Values in Load Winner for CartPole example
        game_selection_winner.set("CartPole-v1")
        winner_file_name_winner.delete('1.0', END)
        target_path_1 = current_directory + '/CartPoleExample/winnerCartPoleExample'
        winner_file_name_winner.insert(END, target_path_1)
        network_type_winner.set("Feed-forward")
        target_path_1 = current_directory + "/CartPoleExample/config-feedforwardCartPoleExample.txt"
        directory_value.configure(state='normal')
        directory_value.delete('1.0', END)
        directory_value.insert(END, target_path_1)
        directory_value.configure(state='disabled')
        directory_value_winner.configure(state='normal')
        directory_value_winner.delete('1.0', END)
        directory_value_winner.insert(END, target_path_1)
        choose_config_file_winner.set("Automatic")
        directory_value_winner.configure(state='disabled')

        local_dir_example = current_directory + "/CartPoleExample"
        arr = os.listdir(local_dir_example)
        # Gets all the checkpints in the directory and sepeartes them
        for file in (sorted(arr, key=numericalSort)):
            if file.find("neat-checkpoint") == 0:
                checkpoint_winners = os.path.join(local_dir_example, file)
                checkpoint_directory_value_winner.insert(END, "~ " + checkpoint_winners + "\n")
                print(checkpoint_directory_value_winner.get(1.0, END))

    elif hidden_level_value == "LoadWinnerExample\n" and education_mode == True:
        print("In Example Level 2")
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)
        except:
            pass

        # Set Focus on tab Education
        tabControl.select(tab_education)

        # Change selected List Box to be 'Load Winner/Checkpoints E2'
        Education_listbox.selection_clear(0, END)
        Education_listbox.selection_set(16)
        Education_listbox.event_generate("<<ListboxSelect>>")

        # Set Values for Example 2 - Lunar Lander

        hidden_level_text.delete(1.0, tk.END)
        print(hidden_level_text.get(1.0, tk.END))
        hidden_level_text.insert(tk.END, "LoadWinnerExample2")
        print(hidden_level_text.get(1.0, tk.END))
        game_selection_winner.set("LunarLander-v2")
        winner_file_name_winner.delete('1.0', END)
        target_path_winner = os.path.join(os.path.abspath(os.getcwd()), 'LunarLanderExample/winnerLunarLanderExample')
        winner_file_name_winner.insert(END, target_path_winner)
        network_type_winner.set("Feed-forward")
        target_path_1 = os.path.join(os.path.abspath(os.getcwd()), 'LunarLanderExample/configFeedForwardLunarLander.txt')
        directory_value.configure(state='normal')
        directory_value.delete('1.0', END)
        directory_value.insert(END, target_path_1)
        directory_value.configure(state='disabled')
        directory_value_winner.configure(state='normal')
        directory_value_winner.delete('1.0', END)
        directory_value_winner.insert(END, target_path_1)
        choose_config_file_winner.set("Automatic")
        directory_value_winner.configure(state='disabled')

        local_dir_example = current_directory + "/LunarLanderExample"
        arr = os.listdir(local_dir_example)
        # Gets all the checkpints in the directory and sepeartes them
        for file in (sorted(arr, key=numericalSort)):
            if file.find("neat-checkpoint") == 0:
                checkpoint_winners = os.path.join(local_dir_example, file)
                checkpoint_directory_value_winner.insert(END, "~ " + checkpoint_winners + "\n")
                print(checkpoint_directory_value_winner.get(1.0, END))
    elif hidden_level_value == "LoadWinnerExample2\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)
        except:
            pass

        # Set Focus on tab Education
        tabControl.select(tab_education)

        # Change selected List Box to be 'Run NEAT'
        Education_listbox.selection_clear(0, END)
        Education_listbox.selection_set(17)
        Education_listbox.event_generate("<<ListboxSelect>>")


        hidden_level_text.delete(1.0, tk.END)
        print(hidden_level_text.get(1.0, tk.END))
        hidden_level_text.insert(tk.END, "RunNEATExample")
        print(hidden_level_text.get(1.0, tk.END))
        game_selection.set("CartPole-v1")
        game_evaluation.set("Single-Processing")
        directory_value.delete('1.0', END)
        target_path_directory = os.path.join(os.path.dirname(__file__), 'CartPoleExample/config-feedforwardCartPoleExample.txt')
        directory_value.insert(END, target_path_directory)
        network_type.set("Feed-forward")
        winner_file_name_l.config(fg="red")
        render_window_l.config(fg="red")
    elif hidden_level_value == "RunNeatExampleCartPole\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)

        except:
            pass
        # Set Focus on tab Education
        tabControl.select(tab_education)
        # Change selected List Box to be 'Run NEAT'
        Education_listbox.selection_clear(0, END)
        Education_listbox.selection_set(18)
        Education_listbox.event_generate("<<ListboxSelect>>")
    elif hidden_level_value == "NoFitnessTerminationExample\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)

        except:
            pass
        # Set Focus on tab Education
        tabControl.select(tab2)
        num_generations_l.grid()
        num_generations.grid()
        game_selection.set("LunarLander-v2")
        game_evaluation.set("Single-Processing")
        directory_value.delete('1.0', END)
        network_type.set("Feed-forward")
        winner_file_name_l.config(fg="red")
        render_window_l.config(fg="black")
        render_window.set("False")
        Education_Tab.sticky = StickyNote.StickyNotes(tab2)
        Education_Tab.sticky.mainarea.insert(1.0,
                               "Because we have set no_fitness_termination = True in config file, when you load the config file it scans for this"
                               "parameter and value and gives you the option to choose how many generations would you like to train."
                               "\nTo do:\n"
                               "- Choose after how many generations you would like the algorithm to stop.\n"
                               "(Terminate after num of generations:)")
        hidden_level_text.delete(1.0, tk.END)
        print(hidden_level_text.get(1.0, tk.END))
        hidden_level_text.insert(tk.END, "NoFitnessTerminationExampleWithin")
        print(hidden_level_text.get(1.0, tk.END))
    elif hidden_level_value == "NoFitnessTerminationExampleWithin\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)

        except:
            pass
        # Set Focus on tab Education
        tabControl.select(tab_education)
        # Change selected List Box to be 'Run NEAT'
        Education_listbox.selection_clear(0, END)
        Education_listbox.selection_set(20)
        Education_listbox.event_generate("<<ListboxSelect>>")

    elif hidden_level_value =="Atari_Example_1\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)

        except:
            pass
        Education_Tab.sticky = StickyNote.StickyNotes(tab2)
        Education_Tab.sticky.mainarea.insert(1.0,
                                             "Let's see an example of a trained neural network"
                                             "with Recurrent rather than Feed-Forward and later we will view the same example trained with Feed-Fordward.\n"
                                             "To do:\n (optional)"
                                             "* Select how many times do you want the neural network to try and play the game (number of runs)\n"
                                             "* Select folder Atari_example_Space_invaders1 if you would like to view checkpoints")
        # Set Focus on tab Education
        tabControl.select(tab3)
        hidden_level_text.delete(1.0, tk.END)
        print(hidden_level_text.get(1.0, tk.END))
        hidden_level_text.insert(tk.END, "Atari_Example_within")
        print(hidden_level_text.get(1.0, tk.END))
        game_selection.set("SpaceInvaders-v0")
        num_generations_l.grid_remove()
        num_generations.grid_remove()
        directory_value.delete('1.0', END)
    elif hidden_level_value == "Atari_Example_within\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)

        except:
            pass
        Education_Tab.sticky = StickyNote.StickyNotes(tab2)
        Education_Tab.sticky.mainarea.insert(1.0,
                                             "Now you can train your own neural network. It may take a while as we have a population of 30 genomes and the threshold is quite high."
                                             "The example from winner was trained with the same configuration and parameters."
                                             "So if you would like train the neural network and and would not like to wait a while you can decrease the threshold and population.\n"
                                             "You can also change Recurrent to Feed-forward if you would like.\n"
                                             "To-do:\n"
                                             "- Select winner file name ")

        # Set Focus on tab Education
        tabControl.select(tab2)

        hidden_level_text.delete(1.0, tk.END)
        print(hidden_level_text.get(1.0, tk.END))
        hidden_level_text.insert(tk.END, "Atari_Example_within_1")
        print(hidden_level_text.get(1.0, tk.END))
    elif hidden_level_value == "Atari_Example_within_1\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)
        except:
            pass
            hidden_level_text.delete(1.0, tk.END)
            print(hidden_level_text.get(1.0, tk.END))
            hidden_level_text.insert(tk.END, "Atari_Example_within_2_feed")
            print(hidden_level_text.get(1.0, tk.END))
            # Set Focus on tab Education
            tabControl.select(tab_education)
            # Change selected List Box to be 'Run NEAT'
            Education_listbox.selection_clear(0, END)
            Education_listbox.selection_set(21)
            Education_listbox.event_generate("<<ListboxSelect>>")
    elif hidden_level_value == "Atari_Example_within_2_feed_within\n" and education_mode == True:
        try:
            # Close Sticky Note
            StickyNotes.quit_window_all(Education_Tab.sticky)
        except:
            pass
            # Set Focus on tab Education
            tabControl.select(tab_education)
            # Change selected List Box to be 'Run NEAT'
            Education_listbox.selection_clear(0, END)
            Education_listbox.selection_set(22)
            Education_listbox.event_generate("<<ListboxSelect>>")
def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
def save_progress():
    open("progress_logfile.log", 'w').close()
    logger = setup_logger('progress_logger', 'progress_logfile.log')
    logger.info(f'Introduction_tab: {Education_Tab.Introduction_tab}')
    logger.info(f'Artificial_intelligence_tab: {Education_Tab.Artificial_intelligence_tab}')
    logger.info(f'AI_Categories_tab: {Education_Tab.AI_Categories_tab}')
    logger.info(f'AI_Categories_tab_2: {Education_Tab.AI_Categories_tab_2}')
    logger.info(f'Intelligent_Agents_tab: {Education_Tab.Intelligent_Agents_tab}')
    logger.info(f'Neuron_tab: {Education_Tab.Neuron_tab}')
    logger.info(f'Perceptron_tab: {Education_Tab.Perceptron_tab}')
    logger.info(f'Components_of_NN: {Education_Tab.Components_of_NN}')
    logger.info(f'Learning_Types: {Education_Tab.Learning_Types}')
    logger.info(f'Neat_config_choice: {Education_Tab.Neat_config_choice}')
    logger.info(f'LoadWinner: {Education_Tab.LoadWinner}')
    logger.info(f'LoadWinner2: {Education_Tab.LoadWinner2}')
    logger.info(f'Run_Neat_choice: {Education_Tab.Run_Neat_choice}')
    logger.info(f'How_Lean_NN: {Education_Tab.How_Lean_NN}')
    logger.info(f'ReinforcementL1: {Education_Tab.ReinforcementL1}')
    logger.info(f'ReinforcementL2: {Education_Tab.ReinforcementL2}')
    logger.info(f'ReinforcementL3: {Education_Tab.ReinforcementL3}')
    logger.info(f'Examples: {hidden_level_text}')
    logger.info(f'Feedforward_vs_Recurrent_tab: {Education_Tab.Feedforward_vs_Recurrent_tab}')
    logger.info(f'No_Fitness_termination_tab: {Education_Tab.No_Fitness_termination_tab}')
    logger.info(f'Atari_Example_tab: {Education_Tab.Atari_Example_tab}')
def reset_progress():
    open("progress_logfile.log", 'w').close()
# def update_progress_label():
#     return f"Current Progress: {progress_Bar_Education['value']}%"


root = tk.Tk()
root.resizable(True,True) # Width, Height
my_sizegrip = ttk.Sizegrip(root)
my_sizegrip.grid(row=5,sticky=SE)

style = ttk.Style()
is_on = False

# Easy Input
frame1 = tk.Frame(master=root, width=700, height=600)
frame1.grid(row=0, column=1)
frame_Education = tk.Frame(master=root, width=60, height=600)
frame_Education.grid(row=0, column=0)

# Education
education_L = tk.Label(frame_Education, text="Education", anchor="w", width = 15, font = ("MS Sans Serif", 15))
education_L.grid(row=0, column=0, ipadx=18, sticky=tk.W)

eduction_options = ('Introduction', 'Artificial Intelligence', 'AI categories L1','AI categories L2',
                    'Intelligent Agents', 'Neuron',
                    'Neural Network', 'Components of a neural network', 'Learning Types',
                    "How do the neural network learn?","Reinforcement Learning L1",
                    "Reinforcement Learning L2","Reinforcement Learning L3","Neuroevolution and NEAT",'NEAT Config File', 'Load Winner/Checkpoints E1',
                    'Load Winner/Checkpoints E2','Run NEAT E1', "Feed-Forward vs Recurrent", "No Fitness Termination", "Atari Example Recurrent","Atari Example Feed-Forward", "Conclusion",
                    "NEAT Running Generation", "NEAT Results for generation", "NEAT Found Winner")
langs_var = tk.StringVar(value=eduction_options)
Education_listbox = tk.Listbox(frame_Education, height=20,width =30, listvariable=langs_var, selectmode='single',
                                name="activation_options", exportselection=0)

scrollbar = tk.Scrollbar(frame_Education, orient="vertical")
scrollbar.config(command=Education_listbox.yview)
scrollbar.grid(row=1,column=1)

Education_listbox.config(yscrollcommand=scrollbar.set)

Education_listbox.grid(row=1, column=0, pady=2, sticky=tk.W)
education_options_selected = Education_listbox.bind('<Leave>', items_selected)
Education_listbox.select_set(0)  # This only sets focus on the first item.
Education_listbox.event_generate("<<ListboxSelect>>")

save_progress_btn = tk.Button(frame_Education, text="Save Progress",
                         command=save_progress,
                         justify=tk.LEFT, anchor="w")
save_progress_btn.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

reset_progress_btn= tk.Button(frame_Education, text="Reset Progress",
                              command=reset_progress,
                              justify=tk.LEFT, anchor="w")
reset_progress_btn.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

save_progress_btn.grid_remove()
reset_progress_btn.grid_remove()

tab_View = tk.IntVar()
tabControl = ttk.Notebook(frame1)
tabControl.grid(row=2)

tab_education = ttk.Frame(tabControl, width=700, height=700)


tab1 = ttk.Frame(tabControl, width=700, height=700)
tab2 = ttk.Frame(tabControl, width=700, height=700)
tab3 = ttk.Frame(tabControl, width=1000, height=700)

tabControl.add(tab_education, text='Education')



ttk.Separator(tab1, orient=tk.VERTICAL).grid(column=2, row=0, rowspan=20, sticky='nse', padx=20)

tabControl.add(tab1, text='Neat Config')

# Neat Section
neat_section_L = tk.Label(tab1, text='Neat Section', font='Helvetica 12 bold underline', justify=LEFT, anchor="w")
neat_section_L.grid(row=1, column=0, ipadx=32, pady=1)

# Fitness Criterion
fitness_criterion_l = tk.Label(tab1, text="Fitness Criterion", justify=LEFT, anchor="w")
fitness_criterion_l.grid(row=2, column=0, ipadx=37, pady=2)
CreateHelpMessage.CreateToolTip(fitness_criterion_l,
                                text='fitness_criterion\nThe function used to compute the termination criterion from the set of genome fitnesses. Allowable values are: min, max, and mean')

fitness_criterion = ttk.Combobox(tab1, name="fitness_criterion", width =20)
fitness_criterion['values'] = ('min', 'max', 'mean')
fitness_criterion.grid(row=2, column=1)
CreateHelpMessage.CreateToolTip(fitness_criterion,
                                text='fitness_criterion\nThe function used to compute the termination criterion from the set of genome fitnesses. Allowable values are: min, max, and mean')
fitness_criterion.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(fitness_criterion, fitness_criterion, fitness_criterion_l, style), "%P"))

hidden_level_text = CustomText(tab1, name="hidden_level", width = 1, height = 1)
hidden_level_text.insert(1.0,"False")
hidden_level_text.grid(row=2, column=1)
hidden_level_text.lower(fitness_criterion)
hidden_level_text.bind("<<TextModified>>", onModification)

Education_Tab.Activate_Content(Education_listbox,tab_education,hidden_level_text)

# Fitness Threshhold
fitness_threshold_l = tk.Label(tab1, text="Fitness Threshold", justify=LEFT, anchor="w")
fitness_threshold_l.grid(row=3, column=0, ipadx=35, pady=1)
CreateHelpMessage.CreateToolTip(fitness_threshold_l,
                                text='fitness_threshold\nHow fit we want the agent to become\nWhen the fitness computed by fitness_criterion meets or exceeds this threshold, the evolution process will terminate, with a call to any registered reporting class’ found_solution method.')

fitness_threshold = ttk.Spinbox(tab1, from_=-100000000, to=100000000, increment=1, name="fitness_threshold", width =19)
fitness_threshold.grid(row=3, column=1)
CreateHelpMessage.CreateToolTip(fitness_threshold,
                                text='fitness_threshold\nHow fit we want the agent to become\nWhen the fitness computed by fitness_criterion meets or exceeds this threshold, the evolution process will terminate, with a call to any registered reporting class’ found_solution method.')
fitness_threshold.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(fitness_threshold, fitness_threshold, fitness_threshold_l, style), "%P"))

# No fitness Termination
no_fitness_termination_l = tk.Label(tab1, text="No Fit Termination?", justify=LEFT, anchor="w")
no_fitness_termination_l.grid(row=4, column=0, ipadx=28)
CreateHelpMessage.CreateToolTip(no_fitness_termination_l,
                                text='no_fitness_termination\nIf this evaluates to True, then the fitness_criterion and fitness_threshold are ignored for termination; only valid if termination by a maximum number of generations passed to population.Population.run() is enabled,\n and the found_solution method is called upon generation number termination. If it evaluates to False, then fitness is used to determine termination. This defaults to “False”.')

no_fitness_termination = ttk.Combobox(tab1, name="no_fitness_termination", width =20)
no_fitness_termination['values'] = ('True', 'False')
no_fitness_termination.grid(row=4, column=1)
CreateHelpMessage.CreateToolTip(no_fitness_termination,
                                text='no_fitness_termination\nIf this evaluates to True, then the fitness_criterion and fitness_threshold are ignored for termination; only valid if termination by a maximum number of generations passed to population.Population.run() is enabled,\n and the found_solution method is called upon generation number termination. If it evaluates to False, then fitness is used to determine termination. This defaults to “False”.')
no_fitness_termination.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(no_fitness_termination, no_fitness_termination, no_fitness_termination_l, style), "%P"))

# Pop Size
pop_size_l = tk.Label(tab1, text="Population Size", justify=LEFT, anchor="w")
pop_size_l.grid(row=5, column=0, ipadx=39, pady=1)
CreateHelpMessage.CreateToolTip(pop_size_l, text='pop_size\nThe number of individuals in each generation.\n How many agents per generation that will play the game.')

pop_size = ttk.Spinbox(tab1, from_=0, to=100000000, increment=1, name="pop_size", width =19)
pop_size.grid(row=5, column=1)
CreateHelpMessage.CreateToolTip(pop_size, text='pop_size\nThe number of individuals in each generation.\n How many agents per generation that will play the game.')
pop_size.config(validate="key",
                validatecommand=(ValidateInput.ValidateInput(pop_size, pop_size, pop_size_l, style), "%P"))

# reset_on_extinction
reset_on_extinction_L = tk.Label(tab1, text="Reset on extinction?", justify=LEFT, anchor="w")
reset_on_extinction_L.grid(row=6, column=0, ipadx=27)
CreateHelpMessage.CreateToolTip(reset_on_extinction_L,
                                text='reset_on_extinction\nIf this evaluates to True, when all species simultaneously become extinct due to stagnation, a new random population will be created. If False, a CompleteExtinctionException will be thrown.')

reset_on_extinction = ttk.Combobox(tab1, name="reset_on_extinction", width =20)
reset_on_extinction['values'] = ('True', 'False')
reset_on_extinction.grid(row=6, column=1)
CreateHelpMessage.CreateToolTip(reset_on_extinction,
                                text='reset_on_extinction\nIf this evaluates to True, when all species simultaneously become extinct due to stagnation, a new random population will be created. If False, a CompleteExtinctionException will be thrown.')
reset_on_extinction.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(reset_on_extinction, reset_on_extinction, reset_on_extinction_L, style), "%P"))

# Default Stagnation section
default_stagnation_l = tk.Label(tab1, text='Default Stagnation', font='Helvetica 12 bold underline', justify=LEFT,
                                anchor="w")
default_stagnation_l.grid(row=7, column=0, ipadx=10, pady=2)

# species_fitness_func
species_fitness_func_l = tk.Label(tab1, text="Species Fitness Func", justify=LEFT, anchor="w")
species_fitness_func_l.grid(row=8, column=0, ipadx=27, pady=1)
CreateHelpMessage.CreateToolTip(species_fitness_func_l,
                                text='species_fitness_func\nThe function used to compute species fitness. This defaults to ``mean``. Allowed values are: max, min, mean, and median')

species_fitness_func = ttk.Combobox(tab1, name="species_fitness_func", width =20)
species_fitness_func['values'] = ('min', 'max', 'mean', 'median')
species_fitness_func.grid(row=8, column=1, pady=1)
CreateHelpMessage.CreateToolTip(species_fitness_func,
                                text='species_fitness_func\nThe function used to compute species fitness. This defaults to ``mean``. Allowed values are: max, min, mean, and median')
species_fitness_func.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(species_fitness_func, species_fitness_func, species_fitness_func_l, style), "%P"))

# max_stagnation
max_stagnation_l = tk.Label(tab1, text="Max Stagination", justify=LEFT, anchor="w")
max_stagnation_l.grid(row=9, column=0, ipadx=36, pady=1)
CreateHelpMessage.CreateToolTip(max_stagnation_l,
                                text='max_stagnation\nSpecies that have not shown improvement in more than this number of generations will be considered stagnant and removed. This defaults to 15.')

max_stagnation = ttk.Spinbox(tab1, from_=0, to=100000000, increment=1, name="max_stagnation", width =19)
max_stagnation.grid(row=9, column=1, pady=1)
CreateHelpMessage.CreateToolTip(max_stagnation,
                                text='max_stagnation\nSpecies that have not shown improvement in more than this number of generations will be considered stagnant and removed. This defaults to 15.')
max_stagnation.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(max_stagnation, max_stagnation, max_stagnation_l, style), "%P"))

# species_elitism
species_elitism_l = tk.Label(tab1, text="Num Protected Species", justify=LEFT, anchor="w")
species_elitism_l.grid(row=10, column=0, ipadx=18, pady=1)
CreateHelpMessage.CreateToolTip(species_elitism_l,
                                text='species_elitism\nThe number of species that will be protected from stagnation; mainly intended to prevent total extinctions caused by all species becoming stagnant before new species arise. For example, a species_elitism setting of 3 will prevent the 3 species with the highest species fitness from being removed for stagnation regardless of the amount of time they have not shown improvement. This defaults to 0.')

species_elitism = ttk.Spinbox(tab1, from_=0, to=100000000, increment=1, name="species_elitism", width =19)
species_elitism.grid(row=10, column=1, pady=2)
CreateHelpMessage.CreateToolTip(species_elitism,
                                text='species_elitism\nThe number of species that will be protected from stagnation; mainly intended to prevent total extinctions caused by all species becoming stagnant before new species arise. For example, a species_elitism setting of 3 will prevent the 3 species with the highest species fitness from being removed for stagnation regardless of the amount of time they have not shown improvement. This defaults to 0.')
species_elitism.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(species_elitism, species_elitism, species_elitism_l, style), "%P"))

# Default Reproduction
default_reproduction_l = tk.Label(tab1, text='Default Reproduction', font='Helvetica 12 bold underline')
default_reproduction_l.grid(row=11, column=0, pady=5, ipadx=2)

# elitism
elitism_l = tk.Label(tab1, text="Elitism", justify=LEFT, anchor="w")
elitism_l.grid(row=12, column=0, ipadx=63, pady=2)
CreateHelpMessage.CreateToolTip(elitism_l,
                                text='elitism\nThe number of most-fit individuals in each species that will be preserved as-is from one generation to the next. This defaults to 0.')

elitism = ttk.Spinbox(tab1, from_=0, to=100000000, name='elitism', width =19)
elitism.grid(row=12, column=1)
CreateHelpMessage.CreateToolTip(elitism,
                                text='elitism\nThe number of most-fit individuals in each species that will be preserved as-is from one generation to the next. This defaults to 0.')
elitism.config(validate="key", validatecommand=(ValidateInput.ValidateInput(elitism, elitism, elitism_l, style), "%P"))

# survival_threshold
survival_threshold_l = tk.Label(tab1, text="Survival Threshold", justify=LEFT, anchor="w")
survival_threshold_l.grid(row=13, column=0, ipadx=32, pady=2)
CreateHelpMessage.CreateToolTip(survival_threshold_l,
                                text='survival_threshold\nThe fraction for each species allowed to reproduce each generation. This defaults to 0.2.')

survival_threshold = ttk.Spinbox(tab1, from_=0.00, to=100000000.00, increment=0.01, name="survival_threshold", width =19)
survival_threshold.grid(row=13, column=1)  # ipady = 2)
CreateHelpMessage.CreateToolTip(survival_threshold,
                                text='survival_threshold\nThe fraction for each species allowed to reproduce each generation. This defaults to 0.2.')
survival_threshold.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(survival_threshold, survival_threshold, survival_threshold_l, style), "%P"))

# min_species_size
min_species_size_l = tk.Label(tab1, text="Min N of genomes per species", justify=LEFT, anchor="w")
min_species_size_l.grid(row=14, column=0, pady=2)
CreateHelpMessage.CreateToolTip(min_species_size_l,
                                text='min_species_size\nThe minimum number of genomes per species after reproduction. This defaults to 2.')

min_species_size = ttk.Spinbox(tab1, from_=0, to=100000000, name="min_species_size", width =19)
min_species_size.grid(row=14, column=1)
CreateHelpMessage.CreateToolTip(min_species_size,
                                text='min_species_size\nThe minimum number of genomes per species after reproduction. This defaults to 2.')
min_species_size.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(min_species_size, min_species_size, min_species_size_l, style), "%P"))


# Default Genome
tabControl.add(tab2, text='Default Genome')

# Genome
genome_Section_l = tk.Label(tab1, text='Genome Section', font='Helvetica 12 bold underline', anchor="w")
genome_Section_l.grid(row=15, column=0, pady=5, ipadx=15)

# Network Parameters
network_Parameters_l = tk.Label(tab1, text='Network Parameters', justify=LEFT, font='Helvetica 11 bold', anchor="w")
network_Parameters_l.grid(row=16, column=0, pady=2, sticky=tk.W)

# num_inputs
num_inputs_l = tk.Label(tab1, text="Number of input nodes:", anchor="w")
num_inputs_l.grid(row=17, column=0, ipadx=16)
CreateHelpMessage.CreateToolTip(num_inputs_l,
                                text='num_inputs\nNumber of inputs into our model\nThe number of input nodes, through which the network receives inputs.')

num_inputs = ttk.Spinbox(tab1, from_=1, to=1000000000, increment=1, name="num_inputs", width =19)
num_inputs.grid(row=17, column=1)
CreateHelpMessage.CreateToolTip(num_inputs,
                                text='num_inputs\nNumber of inputs into our model\nThe number of input nodes, through which the network receives inputs.')
num_inputs.config(validate="key",
                  validatecommand=(ValidateInput.ValidateInput(num_inputs, num_inputs, num_inputs_l, style), "%P"))

# num_outputs
num_outputs_l = tk.Label(tab1, text="Number of output nodes:", anchor="w")
num_outputs_l.grid(row=18, column=0, ipadx=13, pady=2)
CreateHelpMessage.CreateToolTip(num_outputs_l,
                                text='num_outputs\nHow many actions can the agent perform (num of buttons on controller for example\nThe number of output nodes, to which the network delivers outputs.')

num_outputs = ttk.Spinbox(tab1, from_=1, to=1000000000, increment=1, name="num_outputs", width =19)
num_outputs.grid(row=18, column=1)
CreateHelpMessage.CreateToolTip(num_outputs,
                                text='num_outputs\nHow many actions can the agent perform (num of buttons on controller for example\nThe number of output nodes, to which the network delivers outputs.')
num_outputs.config(validate="key",
                   validatecommand=(ValidateInput.ValidateInput(num_outputs, num_outputs, num_outputs_l, style), "%P"))

# num_hidden
num_hidden_l = tk.Label(tab1, text="Number of hidden nodes:", anchor="w")
num_hidden_l.grid(row=19, column=0, ipadx=13, pady=2)
CreateHelpMessage.CreateToolTip(num_hidden_l,
                                text='num_hidden\nThe number of hidden nodes to add to each genome in the initial population.')

num_hidden = ttk.Spinbox(tab1, from_=1, to=1000000000, increment=1, name="num_hidden", width =19)
num_hidden.grid(row=19, column=1)
CreateHelpMessage.CreateToolTip(num_hidden,
                                text='num_hidden\nThe number of hidden nodes to add to each genome in the initial population.')
num_hidden.config(validate="key",
                  validatecommand=(ValidateInput.ValidateInput(num_hidden, num_hidden, num_hidden_l, style), "%P"))

# initial_connection
initial_connection_L = tk.Label(tab1, text="Initial connection:", anchor="w")
initial_connection_L.grid(row=20, column=0, ipadx=34)
CreateHelpMessage.CreateToolTip(initial_connection_L,
                                text='initial_connection\nSpecifies the initial connectivity of newly-created genomes. (Note the effects on settings other than unconnected of the enabled_default parameter.) There are seven allowed values:\n* unconnected - No connections are initially present. This is the default.\n* fs_neat_nohidden - One randomly-chosen input node has one connection to each output node. (This is one version of the FS-NEAT scheme; “FS” stands for “Feature Selection”.)\n* fs_neat_hidden - One randomly-chosen input node has one connection to each hidden and output node. (This is another version of the FS-NEAT scheme. If there are no hidden nodes, it is the same as fs_neat_nohidden.)\n* full_nodirect - Each input node is connected to all hidden nodes, if there are any, and each hidden node is connected to all output nodes; otherwise, each input node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\n* full_direct - Each input node is connected to all hidden and output nodes, and each hidden node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\n* partial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\n* partial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')
initial_connection = ttk.Combobox(tab1, name="initial_connection", width =20)
initial_connection['values'] = ('unconnected', 'fs_neat_nohidden', 'fs_neat_hidden', 'full_nodirect', 'full_direct',
                                'partial_nodirect', 'partial_direct')
initial_connection.grid(row=20, column=1)
CreateHelpMessage.CreateToolTip(initial_connection,
                                text='initial_connection\nSpecifies the initial connectivity of newly-created genomes. (Note the effects on settings other than unconnected of the enabled_default parameter.) There are seven allowed values:\n* unconnected - No connections are initially present. This is the default.\n* fs_neat_nohidden - One randomly-chosen input node has one connection to each output node. (This is one version of the FS-NEAT scheme; “FS” stands for “Feature Selection”.)\n* fs_neat_hidden - One randomly-chosen input node has one connection to each hidden and output node. (This is another version of the FS-NEAT scheme. If there are no hidden nodes, it is the same as fs_neat_nohidden.)\n* full_nodirect - Each input node is connected to all hidden nodes, if there are any, and each hidden node is connected to all output nodes; otherwise, each input node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\n* full_direct - Each input node is connected to all hidden and output nodes, and each hidden node is connected to all output nodes. Genomes with feed_forward set to False will also have recurrent (loopback, in this case) connections from each hidden or output node to itself.\n* partial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\n* partial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')
initial_connection.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(initial_connection, initial_connection, initial_connection_L, style), "%P"))

# initial_conection
initial_conection_value_l = tk.Label(tab1, text="Initial Connection probability:", anchor="w")
initial_conection_value_l.grid(row=21, column=0, ipadx=3)
CreateHelpMessage.CreateToolTip(initial_conection_value_l,
                                text='initial_conection #\npartial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\npartial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')

initial_connection_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="initial_connection_value", width =19)
initial_connection_value.grid(row=21, column=1)
CreateHelpMessage.CreateToolTip(initial_connection_value,
                                text='initial_conection #\npartial_nodirect # - As for full_nodirect, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).\npartial_direct # - as for full_direct, but each connection has a probability of being present determined by the number (valid values are in [0.0, 1.0]).')
initial_connection_value.config(state='disabled')
CreateHelpMessage.Validate(initial_connection, initial_connection_value)
initial_connection_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(initial_connection_value, initial_connection_value, initial_conection_value_l, style),
"%P"))

# feed_forward
feed_forward_L = tk.Label(tab1, text="Feed Forward?", anchor="w")
feed_forward_L.grid(row=22, column=0, ipadx=43)
CreateHelpMessage.CreateToolTip(feed_forward_L,
                                text='feed_forward\nIf this evaluates to True, generated networks will not be\nallowed to have recurrent connections (they will be feedforward).Otherwise they may be (but are not forced to be) recurrent.')

feed_forward = ttk.Combobox(tab1, name='feed_forward', width =20)
feed_forward['values'] = ('True', 'False')
feed_forward.grid(row=22, column=1)
CreateHelpMessage.CreateToolTip(feed_forward,
                                text='feed_forward\nIf this evaluates to True, generated networks will not be\nallowed to have recurrent connections (they will be feedforward).Otherwise they may be (but are not forced to be) recurrent.')
feed_forward.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(feed_forward, feed_forward, feed_forward_L, style), "%P"))

# Select game
game_selection_config_l = tk.Label(tab1, text="Gym Game: ", justify=LEFT, anchor="w")
game_selection_config_l.grid(row=0, column=0,ipadx=37, pady=2, sticky=tk.W)

game_selection_config = ttk.Combobox(tab1, name="game_selection_config", width =20)
game_selection_config['values'] = ('SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0",
                            "KungFuMaster-v0", "LunarLander-v2", "CartPole-v1",
                            "Pong-v0", "Alien-v0", "Asterix-v0", "Asteroids-v0",
                            "Amidar-v0", "Assault-v0", "Atlantis-v0", "BattleZone-v0",
                            "Carnival-v0", "Centipede-v0", "DemonAttack-v0",
                            "JourneyEscape-v0", "Phoenix-v0",
                            "Pooyan-v0", "StarGunner-v0",
                            "TimePilot-v0", "UpNDown-v0", "Zaxxon-v0"
                            )
game_selection_config.grid(row=0, column=1, sticky=tk.W)
game_selection_config.config(validate="key", validatecommand=(
    Validate_Neat_Setup.Validate_Gym_Game(game_selection_config, game_selection_config_l, style, num_inputs, num_outputs), "%P"))


# Node Activation and Aggregation options

# activation_default
random_from_form_l = tk.Label(tab1, text="Enable random selector:", font='Helvetica 9 italic')
random_from_form_l.grid(row=0, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(random_from_form_l,
                                text='Enabling this will allow the user to see assign random choices if none selected directly on form so can see later which one is used')

random_from_form = ttk.Combobox(tab1, name='random_from_form', width =20)
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
                                text='activation_default\nThe default activation function attribute assigned to new nodes. If none is given, or “random” is specified, one of the activation_options will be chosen at random.')

activation_default = ttk.Combobox(tab1, name="activation_default", width =20)
activation_default['values'] = ('abs', 'clamped', 'cube', 'exp', 'gauss',
                                'hat', 'identity', 'inv', 'log', 'relu', 'elu',
                                'lelu', 'selu', 'sigmoid', 'sin', 'softplus', 'square', 'tanh')
activation_default.grid(row=2, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_default,
                                text='activation_default\nThe default activation function attribute assigned to new nodes. If none is given, or “random” is specified, one of the activation_options will be chosen at random.')
activation_default.config(validate="key", validatecommand=(
ValidateInput.ValidateInputWithRandom(activation_default, activation_default, activation_default_L, style,
                                      random_from_form), "%P"))

# Activation Mutate rate
activation_mutate_rate_L = tk.Label(tab1, text="Activation Mutate rate:", anchor="w")
activation_mutate_rate_L.grid(row=3, column=3, ipadx=1, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_mutate_rate_L,
                                text='activation_mutate_rate\nThe probability that mutation will replace the node’s activation function with a randomly-determined member of the activation_options. Valid values are in [0.0, 1.0].')

activation_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="activation_mutate_rate", width =19)
activation_mutate_rate.grid(row=3, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_mutate_rate,
                                text='activation_mutate_rate\nThe probability that mutation will replace the node’s activation function with a randomly-determined member of the activation_options. Valid values are in [0.0, 1.0].')
activation_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(activation_mutate_rate, activation_mutate_rate, activation_mutate_rate_L, style), "%P"))

# Activation Option
activation_options_L = tk.Label(tab1, text="Activation Func:", anchor="w")
activation_options_L.grid(row=4, column=3, ipadx=18, sticky=tk.W)
CreateHelpMessage.CreateToolTip(activation_options_L,
                                text='activation_options\nA space-separated list of the activation functions that may be used by nodes. This defaults to sigmoid. The built-in available functions can be found in Overview of builtin activation functions; more can be added as described in Customizing Behavior.')

activation_options_values_sec = ('abs', 'clamped', 'cube', 'exp', 'gauss',
                                 'hat', 'identity', 'inv', 'log', 'relu', 'elu',
                                 'lelu', 'selu', 'sigmoid', 'sin', 'softplus', 'square', 'tanh')
langs_var = tk.StringVar(value=activation_options_values_sec)
activation_listbox = tk.Listbox(tab1, height=3, listvariable=langs_var, selectmode='extended',
                                name="activation_options", exportselection=0)
activation_listbox.grid(row=4, column=4, pady=2, sticky=tk.W)
#activation_options_selected = activation_listbox.bind('<<ListboxSelect>>', items_selected)
activation_options_selected = activation_listbox.bind('<Leave>', items_selected)

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
                                text='aggregation_mutate_rate\nThe probability that mutation will replace the node’s aggregation function with a randomly-determined member of the aggregation_options. Valid values are in [0.0, 1.0].')

aggregation_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="aggregation_mutate_rate", width =19)
aggregation_mutate_rate.grid(row=5, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_mutate_rate,
                                text='aggregation_mutate_rate\nThe probability that mutation will replace the node’s aggregation function with a randomly-determined member of the aggregation_options. Valid values are in [0.0, 1.0].')
aggregation_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(aggregation_mutate_rate, aggregation_mutate_rate, aggregation_mutate_rate_L, style), "%P"))

# aggregation_default
aggregation_default_L = tk.Label(tab1, text="Aggregation default:", anchor="w")
aggregation_default_L.grid(row=6, column=3, ipadx=8, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_default_L,
                                text='aggregation_default\nThe default aggregation function attribute assigned to new nodes. If none is given, or “random” is specified, one of the aggregation_options will be chosen at random.')

aggregation_default = ttk.Combobox(tab1, name="aggregation_default", width =20)
aggregation_default['values'] = ('sum', 'product', 'min', 'max', 'mean', 'median', 'maxabs')
aggregation_default.grid(row=6, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(aggregation_default,
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
#aggregation_options_selected = listbox_aggregation_options.bind('<<ListboxSelect>>', items_selected)
aggregation_options_selected = listbox_aggregation_options.bind('<Leave>', items_selected)
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

bias_init_mean = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=0.1, name="bias_init_mean", width =19)
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

bias_init_stdev = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_init_stdev", width =19)
bias_init_stdev.grid(row=10, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_stdev,
                                text='bias_init_stdev\nThe standard deviation of the normal/gaussian distribution, if it is used to select bias values for new nodes.')
bias_init_stdev.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_init_stdev, bias_init_stdev, bias_init_stdev_l, style), "%P"))

# bias_init_type
bias_init_type_l = tk.Label(tab1, text="Bias init type:")
bias_init_type_l.grid(row=11, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_type_l,
                                text='bias_init_type\nIf set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(bias_min_value,(bias_init_mean−(bias_init_stdev∗2))) to min(bias_max_value,(bias_init_mean+(bias_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')

bias_init_type = ttk.Combobox(tab1, name="bias_init_type", width =20)
bias_init_type['values'] = ('gaussian', 'normal', 'uniform')
bias_init_type.grid(row=11, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_init_type,
                                text='bias_init_type\nIf set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(bias_min_value,(bias_init_mean−(bias_init_stdev∗2))) to min(bias_max_value,(bias_init_mean+(bias_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')
bias_init_type.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_init_type, bias_init_type, bias_init_type_l, style), "%P"))

# bias_max_value
bias_max_value_l = tk.Label(tab1, text="Bias Maximum allowed bias value:")
bias_max_value_l.grid(row=12, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_max_value_l,
                                text='bias_max_value\nThe maximum allowed bias value. Biases above this value will be clamped to this value.')

bias_max_value = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_max_value", width =19)
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

bias_min_value = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_min_value", width =19)
bias_min_value.grid(row=13, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_min_value,
                                text='bias_min_value\nThe minimum  allowed bias value. Biases above this value will be clamped to this value.')
bias_min_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_min_value, bias_min_value, bias_min_value_l, style), "%P"))

# bias_mutate_power
bias_mutate_power_l = tk.Label(tab1, text="Bias mutation power:")
bias_mutate_power_l.grid(row=14, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_mutate_power_l,
                                text='bias_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a bias value mutation is drawn.')

bias_mutate_power = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_mutate_power", width =19)
bias_mutate_power.grid(row=14, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_mutate_power,
                                text='bias_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a bias value mutation is drawn.')
bias_mutate_power.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(bias_mutate_power, bias_mutate_power, bias_mutate_power_l, style), "%P"))

# bias_mutate_rate
bias_mutate_rate_l = tk.Label(tab1, text="Bias mutation rate:")
bias_mutate_rate_l.grid(row=15, column=3, sticky=tk.W)
CreateHelpMessage.CreateToolTip(bias_mutate_rate_l,
                                text='bias_mutate_rate\nThe probability that mutation will change the bias of a node by adding a random value.')

bias_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_mutate_rate", width =19)
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

bias_replace_rate = ttk.Spinbox(tab1, from_=0.0, to=1000.0, increment=0.1, name="bias_replace_rate", width =19)
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

compatibility_threshold = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name="compatibility_threshold", width =19)
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
                                                 name="compatibility_disjoint_coefficient", width =19)
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
                                text='compatibility_weight_coefficient\nThe coefficient for each weight, bias, or response multiplier difference’s contribution to the genomic distance (for homologous nodes or connections). This is also used as the value to add for differences in activation functions, aggregation functions, or enabled/disabled status.')

compatibility_weight_coefficient = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1,
                                               name="compatibility_weight_coefficient", width =19)
compatibility_weight_coefficient.grid(row=20, column=4, sticky=tk.W)
CreateHelpMessage.CreateToolTip(compatibility_weight_coefficient,
                                text='compatibility_weight_coefficient\nThe coefficient for each weight, bias, or response multiplier difference’s contribution to the genomic distance (for homologous nodes or connections). This is also used as the value to add for differences in activation functions, aggregation functions, or enabled/disabled status.')
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

conn_add_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="conn_add_prob", width =19)
conn_add_prob.grid(row=1, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(conn_add_prob,
                                text='conn_add_prob\nThe probability that mutation will add a connection between existing nodes. Valid values are in [0.0, 1.0].')
conn_add_prob.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(conn_add_prob, conn_add_prob, conn_add_prob_l, style), "%P"))

# conn_delete_prob
conn_delete_prob_l = tk.Label(tab1, text="Connection delete probability:")
conn_delete_prob_l.grid(row=2, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(conn_delete_prob_l,
                                text='conn_delete_prob\nThe probability that mutation will delete an existing connection. Valid values are in [0.0, 1.0].')

conn_delete_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="conn_delete_prob", width =19)
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

enabled_default = ttk.Combobox(tab1, name="enabled_default", width =20)
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
                                text='enabled_mutate_rate\nThe probability that mutation will replace (50/50 chance of True or False) the enabled status of a connection. Valid values are in [0.0, 1.0].')

enabled_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name='enabled_mutate_rate', width =19)
enabled_mutate_rate.grid(row=4, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_mutate_rate,
                                text='enabled_mutate_rate\nThe probability that mutation will replace (50/50 chance of True or False) the enabled status of a connection. Valid values are in [0.0, 1.0].')
enabled_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(enabled_mutate_rate, enabled_mutate_rate, enabled_mutate_rate_l, style), "%P"))

# enabled_rate_to_false_add
enabled_rate_to_false_add_l = tk.Label(tab1, text="enabled_rate_to_false_add:")
enabled_rate_to_false_add_l.grid(row=5, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(enabled_rate_to_false_add_l,
                                text='enabled_rate_to_false_add\nAdds to the enabled_mutate_rate if the connection is currently enabled.')

enabled_rate_to_false_add = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name="enabled_rate_to_false_add", width =19)
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

enabled_rate_to_true_add = ttk.Spinbox(tab1, from_=0.0, to=100.0, increment=1.0, name="enabled_rate_to_true_add", width =19)
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

node_add_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="node_add_prob", width =19)
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

node_delete_prob = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="node_delete_prob", width =19)
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
                                text='response_init_mean\nThe mean of the normal/gaussian distribution, if it is used to select response multiplier attribute values for new nodes.')

response_init_mean = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_init_mean", width =19)
response_init_mean.grid(row=10, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_mean,
                                text='response_init_mean\nThe mean of the normal/gaussian distribution, if it is used to select response multiplier attribute values for new nodes.')
response_init_mean.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_init_mean, response_init_mean, response_init_mean_l, style), "%P"))

# response_init_stdev
response_init_stdev_l = tk.Label(tab1, text="Standard response deviation:")
response_init_stdev_l.grid(row=11, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_stdev_l,
                                text='response_init_stdev\nThe standard deviation of the normal/gaussian distribution, if it is used to select response multipliers for new nodes.')

response_init_stdev = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_init_stdev", width =19)
response_init_stdev.grid(row=11, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_stdev,
                                text='response_init_stdev\nThe standard deviation of the normal/gaussian distribution, if it is used to select response multipliers for new nodes.')
response_init_stdev.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_init_stdev, response_init_stdev, response_init_stdev_l, style), "%P"))

# response_init_type
response_init_type_L = tk.Label(tab1, text="Response type:")
response_init_type_L.grid(row=12, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_type_L,
                                text='response_init_type\nIf set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(response_min_value,(response_init_mean−(response_init_stdev∗2))) to min(response_max_value,(response_init_mean+(response_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')

response_init_type = ttk.Combobox(tab1, name="response_init_type", width =20)
response_init_type['values'] = ('normal', 'uniform', 'gaussian')
response_init_type.grid(row=12, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_init_type,
                                text='response_init_type\nIf set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(response_min_value,(response_init_mean−(response_init_stdev∗2))) to min(response_max_value,(response_init_mean+(response_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')
response_init_type.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_init_type, response_init_type, response_init_type_L, style), "%P"))

# response_max_value
response_max_value_l = tk.Label(tab1, text="Max response value:")
response_max_value_l.grid(row=13, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_max_value_l,
                                text='response_max_value\nThe maximum allowed response multiplier. Response multipliers above this value will be clamped to this value.')

response_max_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_max_value", width =19)
response_max_value.grid(row=13, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_max_value,
                                text='response_max_value\nThe maximum allowed response multiplier. Response multipliers above this value will be clamped to this value.')
response_max_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_max_value, response_max_value, response_max_value_l, style), "%P"))

# response_min_value
response_min_value_l = tk.Label(tab1, text="Min response value:")
response_min_value_l.grid(row=14, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_min_value_l,
                                text='response_min_value\nThe minimum allowed response multiplier. Response multipliers below this value will be clamped to this value.')

response_min_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_min_value", width =19)
response_min_value.grid(row=14, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_min_value,
                                text='response_min_value\nThe minimum allowed response multiplier. Response multipliers below this value will be clamped to this value.')
response_min_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_min_value, response_min_value, response_min_value_l, style), "%P"))

# response_mutate_power
response_mutate_power_l = tk.Label(tab1, text="Mutate response power:")
response_mutate_power_l.grid(row=15, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_power_l,
                                text='response_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a response multiplier mutation is drawn.')

response_mutate_power = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_mutate_power", width =19)
response_mutate_power.grid(row=15, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_power,
                                text='response_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a response multiplier mutation is drawn.')
response_mutate_power.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_mutate_power, response_mutate_power, response_mutate_power_l, style), "%P"))

# response_mutate_rate
response_mutate_rate_l = tk.Label(tab1, text="Mutate response rate:")
response_mutate_rate_l.grid(row=16, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_rate_l,
                                text='response_mutate_rate\nThe probability that mutation will change the response multiplier of a node by adding a random value.')

response_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_mutate_rate", width =19)
response_mutate_rate.grid(row=16, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_mutate_rate,
                                text='response_mutate_rate\nThe probability that mutation will change the response multiplier of a node by adding a random value.')
response_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_mutate_rate, response_mutate_rate, response_mutate_rate_l, style), "%P"))

# response_replace_rate
response_replace_rate_l = tk.Label(tab1, text="Response response rate:")
response_replace_rate_l.grid(row=17, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_replace_rate_l,
                                text='response_replace_rate\nThe probability that mutation will change the response multiplier of a node by adding a random value.')

response_replace_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="response_replace_rate", width =19)
response_replace_rate.grid(row=17, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(response_replace_rate,
                                text='response_replace_rate\nThe probability that mutation will change the response multiplier of a node by adding a random value.')
response_replace_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(response_replace_rate, response_replace_rate, response_replace_rate_l, style), "%P"))

# single_structural_mutation
single_structural_mutation_L = tk.Label(tab1, text="Singe structural mutation?")
single_structural_mutation_L.grid(row=18, column=5, sticky=tk.W)
CreateHelpMessage.CreateToolTip(single_structural_mutation_L,
                                text='single_structural_mutation\nIf this evaluates to True, only one structural mutation (the addition or removal of a node or connection) will be allowed per genome per generation. (If the probabilities for conn_add_prob, conn_delete_prob, node_add_prob, and node_delete_prob add up to over 1, the chances of each are proportional to the appropriate configuration value.) This defaults to “False”.')

single_structural_mutation = ttk.Combobox(tab1, name="single_structural_mutation", width =20)
single_structural_mutation['values'] = ('True', 'False')
single_structural_mutation.grid(row=18, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(single_structural_mutation,
                                text='single_structural_mutation\nIf this evaluates to True, only one structural mutation (the addition or removal of a node or connection) will be allowed per genome per generation. (If the probabilities for conn_add_prob, conn_delete_prob, node_add_prob, and node_delete_prob add up to over 1, the chances of each are proportional to the appropriate configuration value.) This defaults to “False”.')
single_structural_mutation.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(single_structural_mutation, single_structural_mutation, single_structural_mutation_L,
                            style), "%P"))

# structural_mutation_surer
structural_mutation_surer_L = tk.Label(tab1, text="Structural mutation surer?")
structural_mutation_surer_L.grid(row=19, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(structural_mutation_surer_L,
                                text='structural_mutation_surer\nIf this evaluates to True, then an attempt to add a node to a genome lacking connections will result in adding a connection instead; furthermore, if an attempt to add a connection tries to add a connection that already exists, that connection will be enabled. If this is set to default, then it acts as if it had the same value as single_structural_mutation (above). This defaults to “default”.')

structural_mutation_surer = ttk.Combobox(tab1, name="structural_mutation_surer", width =20)
structural_mutation_surer['values'] = ('True', 'False', 'default')
structural_mutation_surer.grid(row=19, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(structural_mutation_surer,
                                text='structural_mutation_surer\nIf this evaluates to True, then an attempt to add a node to a genome lacking connections will result in adding a connection instead; furthermore, if an attempt to add a connection tries to add a connection that already exists, that connection will be enabled. If this is set to default, then it acts as if it had the same value as single_structural_mutation (above). This defaults to “default”.')
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
                                text='weight_init_mean\nThe mean of the normal/gaussian distribution used to select weight attribute values for new connections.')

weight_init_mean = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_init_mean", width =19)
weight_init_mean.grid(row=21, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_mean,
                                text='weight_init_mean\nThe mean of the normal/gaussian distribution used to select weight attribute values for new connections.')
weight_init_mean.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_init_mean, weight_init_mean, weight_init_mean_l, style), "%P"))

# weight_init_stdev
weight_init_stdev_l = tk.Label(tab1, text="Standard weight:")
weight_init_stdev_l.grid(row=22, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_stdev_l,
                                text='weight_init_stdev\nThe standard deviation of the normal/gaussian distribution used to select weight values for new connections.')

weight_init_stdev = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_init_stdev", width =19)
weight_init_stdev.grid(row=22, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_stdev,
                                text='weight_init_stdev\nThe standard deviation of the normal/gaussian distribution used to select weight values for new connections.')
weight_init_stdev.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_init_stdev, weight_init_stdev, weight_init_stdev_l, style), "%P"))

# weight_init_type
weight_init_type_L = tk.Label(tab1, text="Weight Type")
weight_init_type_L.grid(row=23, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_type_L,
                                text='weight_init_type\nIf set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(weight_min_value,(weight_init_mean−(weight_init_stdev∗2))) to min(weight_max_value,(weight_init_mean+(weight_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')

weight_init_type = ttk.Combobox(tab1, name="weight_init_type", width =20)
weight_init_type['values'] = ('gaussian', 'normal', 'uniform')
weight_init_type.grid(row=23, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_init_type,
                                text='weight_init_type\nIf set to gaussian or normal, then the initialization is to a normal/gaussian distribution. If set to uniform, a uniform distribution from max(weight_min_value,(weight_init_mean−(weight_init_stdev∗2))) to min(weight_max_value,(weight_init_mean+(weight_init_stdev∗2))). (Note that the standard deviation of a uniform distribution is not range/0.25, as implied by this, but the range divided by a bit over 0.288 (the square root of 12); however, this approximation makes setting the range much easier.) This defaults to “gaussian”.')
weight_init_type.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_init_type, weight_init_type, weight_init_type_L, style), "%P"))

# weight_max_value
weight_max_value_l = tk.Label(tab1, text="Max weight:")
weight_max_value_l.grid(row=24, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_max_value_l,
                                text='weight_max_value\nThe maximum allowed weight value. Weights above this value will be clamped to this value.')

weight_max_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_max_value", width =19)
weight_max_value.grid(row=24, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(weight_max_value,
                                text='weight_max_value\nThe maximum allowed weight value. Weights above this value will be clamped to this value.')
weight_max_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_max_value, weight_max_value, weight_max_value_l, style), "%P"))

# weight_min_value
weight_min_value_l = tk.Label(tab1, text="Min weight:")
weight_min_value_l.grid(row=25, column=5, sticky=tk.W, ipady=2)
CreateHelpMessage.CreateToolTip(weight_min_value_l,
                                text='weight_min_value\nThe minimum allowed weight value. Weights below this value will be clamped to this value.')

weight_min_value = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_min_value", width =19)
weight_min_value.grid(row=25, column=6, sticky=tk.W)
CreateHelpMessage.CreateToolTip(weight_min_value,
                                text='weight_min_value\nThe minimum allowed weight value. Weights below this value will be clamped to this value.')
weight_min_value.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_min_value, weight_min_value, weight_min_value_l, style), "%P"))

# weight_mutate_power
weight_mutate_power_l = tk.Label(tab1, text="Weight Mutate power:")
weight_mutate_power_l.grid(row=26, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_power_l,
                                text='weight_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a weight value mutation is drawn.')

weight_mutate_power = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_mutate_power", width =19)
weight_mutate_power.grid(row=26, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_power,
                                text='weight_mutate_power\nThe standard deviation of the zero-centered normal/gaussian distribution from which a weight value mutation is drawn.')
weight_mutate_power.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_mutate_power, weight_mutate_power, weight_mutate_power_l, style), "%P"))

# weight_mutate_rate
weight_mutate_rate_l = tk.Label(tab1, text="Weight Mutate rate:")
weight_mutate_rate_l.grid(row=27, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_rate_l,
                                text='weight_mutate_rate\nThe probability that mutation will change the weight of a connection by adding a random value.')

weight_mutate_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_mutate_rate", width =19)
weight_mutate_rate.grid(row=27, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_mutate_rate,
                                text='weight_mutate_rate\nThe probability that mutation will change the weight of a connection by adding a random value.')
weight_mutate_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_mutate_rate, weight_mutate_rate, weight_mutate_rate_l, style), "%P"))

# weight_replace_rate
weight_replace_rate_l = tk.Label(tab1, text="Weight replace rate:")
weight_replace_rate_l.grid(row=28, column=5, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_replace_rate_l,
                                text='weight_replace_rate\nThe probability that mutation will replace the weight of a connection with a newly chosen random value (as if it were a new connection).')

weight_replace_rate = ttk.Spinbox(tab1, from_=0.0, to=1.0, increment=0.1, name="weight_replace_rate", width =19)
weight_replace_rate.grid(row=28, column=6, sticky=tk.W, pady=2)
CreateHelpMessage.CreateToolTip(weight_replace_rate,
                                text='weight_replace_rate\nThe probability that mutation will replace the weight of a connection with a newly chosen random value (as if it were a new connection).')
weight_replace_rate.config(validate="key", validatecommand=(
ValidateInput.ValidateInput(weight_replace_rate, weight_replace_rate, weight_replace_rate_l, style), "%P"))

tabControl.grid(row=0, column=0)

# Editor
frame2 = tk.Frame(master=root, width=500, height=600)
frame2.grid(row=0, column=2,padx=10)

frame2.rowconfigure(0, minsize=900)  # row where buttons are
frame2.columnconfigure(1, minsize=600)  # column where buttons are

#frame2.rowconfigure(0, minsize=900, weight=1)  # row where buttons are
#frame2.columnconfigure(1, minsize=900, weight=1)  # column where buttons are


txt_edit = tk.Text(frame2, width =10, height=50)

fr_buttons = tk.Frame(frame2, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
default_values_config_btn = tk.Button(fr_buttons, text="Default Config", command=default_values_config)
get_empty_config_btn = tk.Button(fr_buttons, text="Config Layout", command=get_empty_config)
update_btn = tk.Button(fr_buttons, text="Update Config", command=update_editor)

# Keep track of the button state on/off
# global is_on


# Define Our Images
on = tk.PhotoImage(file="on.png")
off = tk.PhotoImage(file="off.png")

# Create A Button
on_button = tk.Button(fr_buttons, image=off, bd=0,
                      command=switch)

# Define Our Images
education_mode_pic = tk.PhotoImage(file="education_mode_icon.png")
normal_mode_pic = tk.PhotoImage(file="normal_mode_pic.png")

# Create A Button
education_mode_normal_mode = tk.Button(fr_buttons, image=education_mode_pic, bd=0,
                      command=switch_modes)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
default_values_config_btn.grid(row=2, column=0, sticky="ew", padx=5)
get_empty_config_btn.grid(row=3, column=0, sticky="ew", padx=5)
update_btn.grid(row=4, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
on_button.grid(row=5, column=0, sticky="ne")
education_mode_normal_mode.grid(row=6,column =0)


# Tab 2 --- Set up
tabControl.add(tab2, text = "NEAT Setup")

# Setup label
setup_neat_l = tk.Label(tab2, text='Setup', font='Helvetica 12 bold underline', justify=LEFT, anchor="w")
setup_neat_l.grid(row=0, column=0, ipadx=32, pady=1, sticky=tk.W)


# Runs Per Network
runs_per_network_l = tk.Label(tab2, text="Runs Per Network:", justify=LEFT, anchor="w")
runs_per_network_l.grid(row=0, column=2, ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(runs_per_network_l,
                                text='The game you selected runs on a number of episodes')

runs_per_network = ttk.Spinbox(tab2, from_=0, to=100000000, increment=1, name = "runs_per_network", width =19)
runs_per_network.grid(row=1, column=2, sticky=tk.W)
runs_per_network.config(validate="key", validatecommand=(
    Validate_Neat_Setup.Validate_Game_Selection(runs_per_network, runs_per_network_l, style, runs_per_network_l, runs_per_network), "%P"))

CreateHelpMessage.CreateToolTip(runs_per_network,
                                text='The game you selected runs on a number of episodes')

runs_per_network_l.grid_remove()
runs_per_network.grid_remove()

# Select game
game_selection_l = tk.Label(tab2, text="Gym Game:", justify=LEFT, anchor="w")
game_selection_l.grid(row=1, column=0,ipadx=37, pady=2, sticky=tk.W)

game_selection = ttk.Combobox(tab2, name="game_selection", width =20)
game_selection['values'] = ('SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0",
                            "KungFuMaster-v0", "LunarLander-v2", "CartPole-v1",
                            "Pong-v0", "Alien-v0", "Asterix-v0", "Asteroids-v0",
                            "Amidar-v0", "Assault-v0", "Atlantis-v0", "BattleZone-v0",
                            "Carnival-v0", "Centipede-v0", "DemonAttack-v0",
                            "JourneyEscape-v0", "Phoenix-v0",
                            "Pooyan-v0", "StarGunner-v0",
                            "TimePilot-v0", "UpNDown-v0", "Zaxxon-v0"
                            )
CreateHelpMessage.CreateToolTip(game_selection_l,
                                text='A game from the gym environment.\nAtari games:\n "SpaceInvaders-v0", "Berzerk-v0", "Boxing-v0", "Freeway-v0", "Frostbite-v0", "Kangaroo-v0", "KungFuMaster-v0","Pong-v0", "Alien-v0", "Asterix-v0", "Asteroids-v0", "Amidar-v0", "Assault-v0", "Atlantis-v0", "BattleZone-v0", "Carnival-v0", "Centipede-v0", "DemonAttack-v0", "JourneyEscape-v0", "Phoenix-v0", "Pooyan-v0", "StarGunner-v0","TimePilot-v0", "UpNDown-v0", "Zaxxon-v0"\nBox2D games:\n  "LunarLander-v2", "CartPole-v1"')

game_selection.grid(row=1, column=1, sticky=tk.W)
game_selection.config(validate="key", validatecommand=(
    Validate_Neat_Setup.Validate_Game_Selection(game_selection, game_selection_l, style, runs_per_network_l, runs_per_network), "%P"))
CreateHelpMessage.CreateToolTip(game_selection,
                                text='A game from the gym environment.\nAtari games:\n "SpaceInvaders-v0", "Berzerk-v0", "Boxing-v0", "Freeway-v0", "Frostbite-v0", "Kangaroo-v0", "KungFuMaster-v0","Pong-v0", "Alien-v0", "Asterix-v0", "Asteroids-v0", "Amidar-v0", "Assault-v0", "Atlantis-v0", "BattleZone-v0", "Carnival-v0", "Centipede-v0", "DemonAttack-v0", "JourneyEscape-v0", "Phoenix-v0", "Pooyan-v0", "StarGunner-v0","TimePilot-v0", "UpNDown-v0", "Zaxxon-v0"\nBox2D games:\n  "LunarLander-v2", "CartPole-v1"')


# Select evalutation
game_evaluation_l = tk.Label(tab2, text="Evaluate Genomes:", justify=LEFT, anchor="w")
game_evaluation_l.grid(row=2, column=0,ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(game_evaluation_l,
                                text='When single-processing is selected it means it will run only on one core or one thread of your computer, so one game (genome) at a time.')


game_evaluation = ttk.Combobox(tab2, name="game_evaluation", width =20)
game_evaluation['values'] = ("Single-Processing")
game_evaluation.grid(row=2, column=1, sticky=tk.W)
game_evaluation.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(game_evaluation, game_evaluation_l, style), "%P"))
CreateHelpMessage.CreateToolTip(game_evaluation,
                                text='When single-processing is selected it means it will run only on one core or one thread of your computer, so one game (genome) at a time.')

# Winner file name
winner_file_name_l = tk.Label(tab2, text="Winner file name:", justify=LEFT, anchor="w")
winner_file_name_l.grid(row=3, column=0, ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(winner_file_name_l,
                                text='The name of the file that will save the winner genome that reaches fitness_threshold.')

winner_file_name = tk.Text(tab2, name="winner_file_name", height = 0.5, width =17)
winner_file_name.grid(row=3, column=1, sticky=tk.W)
winner_file_name.bind('<KeyRelease>',Validate_Text_Widget_Neat)
CreateHelpMessage.CreateToolTip(winner_file_name,
                                text='The name of the file that will save the winner genome that reaches fitness_threshold.')
# Checkpoints
game_checkpoint_l = tk.Label(tab2, text="Save Checkpoint:", justify=LEFT, anchor="w")
game_checkpoint_l.grid(row=4, column=0,ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(game_checkpoint_l,
                                text='Choosing N(5 for example) number of checkpoints it means that the process of your game will be saved after N(5 for example) number of generations.')

game_checkpoint = ttk.Spinbox(tab2, from_=0, to=100000000, increment=1, name = "game_checkpoint", width =19)
game_checkpoint.grid(row=4, column=1, sticky=tk.W)
game_checkpoint.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(game_checkpoint, game_checkpoint_l, style), "%P"))
CreateHelpMessage.CreateToolTip(game_checkpoint_l,
                                text='Choosing N(5 for example) number of checkpoints it means that the process of your game will be saved after N(5 for example) number of generations.')

# Console
console_l = tk.Label(tab2, text="Enter command:", justify=LEFT, anchor="w")
console_l.grid(row=11, column=0,ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(console_l,
                                text='Here you will see the input and output for the game you have selected if the tickbox is ticked.\nOtherwise you can type commands such as:\n'
                                     'print(env.action_space) or print(env.observation_space) after you have selected the game and you can manually see output (action_space) and input(observation_space)')

build_in_console = tk.Text(tab2, name="build_in_console", height = 5, width =45)
build_in_console.grid(row=12, column=0, sticky=tk.W,columnspan=2)
build_in_console.bind("<Return>",Build_in_Console.Get_Console_input(build_in_console, game_selection))
CreateHelpMessage.CreateToolTip(build_in_console,
                                text='Here you will see the input and output for the game you have selected if the tickbox is ticked.\nOtherwise you can type commands such as:\n'
                                     'print(env.action_space) or print(env.observation_space) after you have selected the game and you can manually see output (action_space) and input(observation_space)')

# Reccurent / FeedForward network
network_type_l = tk.Label(tab2, text="Network Type:", justify=LEFT, anchor="w")
network_type_l.grid(row=5, column=0,ipadx=37, pady=2, sticky=tk.W)

network_type = ttk.Combobox(tab2, name="network_type", width =20)
network_type['values'] = ("Feed-forward", "Recurrent")
network_type.grid(row=5, column=1, sticky=tk.W)
network_type.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(network_type, network_type_l, style), "%P"))

# Directory path
directory_value_l = tk.Label(tab2, text="Directory:", justify=LEFT, anchor="w")
directory_value_l.grid(row=8, column=0, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(directory_value_l,
                                text='The directory of your Configuration file or checkpoint')
directory_value = tk.Text(tab2, name="directory_value", height = 2, width =50)
directory_value.grid(row=9, column=0, sticky=tk.W, columnspan=3)
directory_value.bind('<Key>',lambda e: 'break')
CreateHelpMessage.CreateToolTip(directory_value,
                                text='The directory of your Configuration file or checkpoint')

# Render Window
render_window_l = tk.Label(tab2, text="Render game?", justify=LEFT, anchor="w")
render_window_l.grid(row=6, column=0,ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(render_window_l,
                                text='True - you will see the game on your screen while your computer is trying to learn how to play\n'
                                     'False - you will not see the game on your screen while your computer is trying to learn to play')
render_window = ttk.Combobox(tab2, name="render_window", width =20)
render_window['values'] = ("True", "False")
render_window.grid(row=6, column=1, sticky=tk.W)
render_window.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(render_window, render_window_l, style), "%P"))
CreateHelpMessage.CreateToolTip(render_window,
                                text='True - you will see the game on your screen while your computer is trying to learn how to play\n'
                                     'False - you will not see the game on your screen while your computer is trying to learn to play')

# Runs Per Network
num_generations_l = tk.Label(tab2, text="Terminate after num of generations:", justify=LEFT, anchor="w")
num_generations_l.grid(row=2, column=2, ipadx=37, pady=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(num_generations_l,
                                text='no_fitness_termination = True in Config file which means fitness_criterion and fitness_threshold are ignnored and algorithm will run N generations')

num_generations = ttk.Spinbox(tab2, from_=0, to=100000000, increment=1, name = "num_generations", width =19)
num_generations.grid(row=3, column=2, sticky=tk.W)
CreateHelpMessage.CreateToolTip(num_generations,
                                text='no_fitness_termination = True in Config file which means fitness_criterion and fitness_threshold are ignnored and algorithm will run N generations')
num_generations.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(num_generations, num_generations_l, style), "%P"))

num_generations_l.grid_remove()
num_generations.grid_remove()

# Choose Config File
choose_config_file_l = tk.Label(tab2, text="Config File:", justify=LEFT, anchor="w")
choose_config_file_l.grid(row=7, column=0,ipadx=37, pady=2, sticky=tk.W)

choose_config_file = ttk.Combobox(tab2, name="choose_config_file", width =20)
choose_config_file['values'] = ("From Text Editor", "Choose file from directory", "Restore from Checkpoint")
choose_config_file.grid(row=7, column=1, sticky=tk.W)
choose_config_file.config(validate="key", validatecommand=Get_Directory_For_Neat.run_NEAT_get_input(choose_config_file, directory_value, txt_edit, num_generations, num_generations_l))
CreateHelpMessage.CreateToolTip(choose_config_file,
                                text='The directory of your Configuration file or checkpoint')
# Output console
Output_Console = tk.Text(tab2, name="output_console", height = 30, width = 80)
Output_Console.grid(row=13, column=0, sticky=tk.W, rowspan =4, columnspan=4, pady = 5)
Output_Console.bind('<Key>',lambda e: 'break')
Output_Console.insert(tk.END, "## See the evolution of genomes while running NEAT ##")


var1 = tk.IntVar()
var2 = tk.IntVar()
config_file_check = tk.Checkbutton(tab2, text='Check config file for input/output',variable=var1, onvalue=1, offvalue=0, command=print_selection)
config_file_check.grid(row =10, column =1,sticky=tk.W, padx=5, pady=5)

# Run button for Neat using a thread
btn_run_neat = tk.Button(tab2, text="Run NEAT", command= lambda : submit_to_thread_pool_run_neat(Output_Console,game_selection, game_evaluation, winner_file_name, game_checkpoint, network_type, directory_value, render_window, runs_per_network, num_generations, choose_config_file), justify=LEFT, anchor="w")
btn_run_neat.grid(row=10, column=0, sticky=tk.W, padx=5, pady=5)

# Run button for Neat using a thread
#btn_stop_neat = tk.Button(tab2, text="Stop NEAT", command= stop_thread, justify=LEFT, anchor="w")
#btn_stop_neat.grid(row=10, column=1, sticky=tk.W, padx=5, pady=5)


tabControl.add(tab3, text='Load Winner')
tabControl.bind('<<NotebookTabChanged>>', on_tab_change)
# Setup label
setup_neat_l_Winner = tk.Label(tab3, text='Run Winner', font='Helvetica 12 bold underline', justify=LEFT, anchor="w")
setup_neat_l_Winner.grid(row=0, column=0, ipadx=32, pady=1, sticky=tk.W)

# Select game
game_selection_l_Winner = tk.Label(tab3, text="Gym Game:", justify=LEFT, anchor="w")
game_selection_l_Winner.grid(row=1, column=0,ipadx=37, pady=2, sticky=tk.W)

game_selection_winner = ttk.Combobox(tab3, name="game_selection_winner", width =20)
game_selection_winner['values'] = ('SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo",
                                   "LunarLander-v2", "CartPole-v1", "Pong-v0", "Alien-v0", "Asterix-v0", "Asteroids-v0", "Amidar-v0", "Assault-v0",
                                   "Atlantis-v0", "BattleZone-v0", "Carnival-v0", "Centipede-v0", "DemonAttack-v0", "JourneyEscape-v0",
                                   "Phoenix-v0", "Pooyan-v0",
                                   "StarGunner-v0", "TimePilot-v0", "UpNDown-v0")
game_selection_winner.grid(row=1, column=1, sticky=tk.W)
game_selection_winner.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(game_selection_winner, game_selection_l_Winner, style), "%P"))

# Winner file name
winner_file_name_l_winner = tk.Label(tab3, text="Winner file name:", justify=LEFT, anchor="w")
winner_file_name_l_winner.grid(row=3, column=0, ipadx=37, pady=2, sticky=tk.W)

winner_file_name_winner = tk.Text(tab3, name="winner_file_name_winner", height = 0.5, width =17)
winner_file_name_winner.grid(row=3, column=1, sticky=tk.W)
winner_file_name_winner.bind('<KeyRelease>',Validate_Text_Widget_Neat)

btnFind_winner = tk.Button(tab3, text="Select File",command=getFolderPath_and_File, name = "btnFind_winner")
btnFind_winner.grid(row=3,column=2)

# Checkpoints
game_checkpoint_l_winner = tk.Label(tab3, text="Num of ep. per genome:", justify=LEFT, anchor="w")
game_checkpoint_l_winner.grid(row=4, column=0,ipadx=37, pady=2, sticky=tk.W)

game_checkpoint_winner = ttk.Spinbox(tab3, from_=0, to=100000000, increment=1, name = "ep_per_genome", width =19)
game_checkpoint_winner.grid(row=4, column=1, sticky=tk.W)
game_checkpoint_winner.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(game_checkpoint_winner, game_checkpoint_l_winner, style), "%P"))

# Number of genomes
number_of_genomes_l = tk.Label(tab3, text="Num of genomes in checkpoint:", justify=LEFT, anchor="w")
number_of_genomes_l.grid(row=5, column=2,ipadx=37, pady=2, sticky=tk.W)

number_of_genomes = ttk.Spinbox(tab3, from_=0, to=100000000, increment=1, name = "number_of_genomes", width =19)
number_of_genomes.grid(row=5, column=3, sticky=tk.W)
number_of_genomes.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(number_of_genomes, number_of_genomes_l, style), "%P"))

number_of_genomes_l.grid_remove()
number_of_genomes.grid_remove()

# Directory path
checkpoint_directory_value_l_winner = tk.Label(tab3, text="Checkpoint(s) directory:", justify=LEFT, anchor="w")
checkpoint_directory_value_l_winner.grid(row=5, column=0, pady=2, sticky=tk.W)

btnFind = tk.Button(tab3, text="Browse Folder",command=getFolderPath, name = "btnFind")
btnFind.grid(row=5,column=1)

checkpoint_directory_value_winner = tk.Text(tab3, name="checkpoint_directory_value_winner", height = 4, width =80)
checkpoint_directory_value_winner.grid(row=6, column=0, sticky=tk.W, columnspan=4)
#checkpoint_directory_value_winner.bind('<Key>',lambda e: 'break')

# Reccurent / FeedForward network
network_type_l_winner = tk.Label(tab3, text="Network Type:", justify=LEFT, anchor="w")
network_type_l_winner.grid(row=7, column=0,ipadx=37, pady=2, sticky=tk.W)

network_type_winner = ttk.Combobox(tab3, name="network_type_winner", width =20)
network_type_winner['values'] = ("Feed-forward", "Recurrent")
network_type_winner.grid(row=7, column=1, sticky=tk.W)
network_type_winner.config(validate="key", validatecommand=(
    Validate_Neat_Setup.ValidateInputNEAT(network_type_winner, network_type_l_winner, style), "%P"))

# Directory path
directory_value_l_winner = tk.Label(tab3, text="Directory:", justify=LEFT, anchor="w")
directory_value_l_winner.grid(row=9, column=0, pady=2, sticky=tk.W)

directory_value_winner = tk.Text(tab3, name="directory_value_winner", height = 2, width =50)
directory_value_winner.grid(row=10, column=0, sticky=tk.W, columnspan=3)
directory_value_winner.bind('<Key>',lambda e: 'break')

# Choose Config File
choose_config_file_l_winner = tk.Label(tab3, text="Config File:", justify=LEFT, anchor="w")
choose_config_file_l_winner.grid(row=8, column=0,ipadx=37, pady=2, sticky=tk.W)

choose_config_file_winner = ttk.Combobox(tab3, name="choose_config_file_winner", width =20)
choose_config_file_winner['values'] = ("From Text Editor", "Choose file from directory")
choose_config_file_winner.grid(row=8, column=1, sticky=tk.W)
choose_config_file_winner.config(validate="key", validatecommand=Get_Directory_For_Neat.Get_Input(choose_config_file_winner, directory_value_winner, txt_edit, num_generations, num_generations_l))

#btn_run_neat_winner = tk.Button(tab3, text="Load Genomes and winner", command= lambda : threading.Thread(target =  load_winner ,args = [game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner]).start(), justify=LEFT, anchor="w")


# Output console
Output_Console_winner = tk.Text(tab3, name="output_console_winner", height = 30, width =80)
Output_Console_winner.grid(row=12, column=0, sticky=tk.W, rowspan =4, columnspan=4, pady = 5)
Output_Console_winner.bind('<Key>',lambda e: 'break')
Output_Console_winner.insert(tk.END, "## Load checkpoints / winner ##")

# Run button for Neat using a thread
btn_run_neat_winner = tk.Button(tab3, text="Load Genomes and winner", command= lambda : submit_to_thread_pool_load_winner(Output_Console_winner,game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner, number_of_genomes), justify=LEFT, anchor="w")
btn_run_neat_winner.grid(row=11, column=0, sticky=tk.W, padx=5, pady=5)



# Color LightMode program
for label in labels_list:  # Loop though Labels
    exec(label + '.config(fg = "gray1", bg = "grey75")')
for label_o in other_tabs_labels:  # Loop though Labels
    exec(label_o + '.config(fg = "gray1", bg = "grey75")')
for button in buttons_list:
    exec(button + ".configure(bg = '#32285b', fg= 'gray99')")

config_file_check.configure(activebackground = "grey75")
txt_edit.config(bg="light grey", fg="gray1")
winner_file_name.config(bg="#e5e5e5", fg="gray1")
directory_value.config(bg="#e5e5e5", fg="gray1")
build_in_console.config(bg="#e5e5e5", fg="gray1")
Output_Console.config(bg="#e5e5e5", fg="gray1")
winner_file_name_winner.config(bg="#e5e5e5", fg="gray1")
checkpoint_directory_value_winner.config(bg="#e5e5e5", fg="gray1")
directory_value_winner.config(bg="#e5e5e5", fg="gray1")
Output_Console_winner.config(bg="#e5e5e5", fg="gray1")
fr_buttons.configure(bg="#d9001f")
on_button.configure(bg="#d9001f", activebackground='#d9001f')
education_mode_normal_mode.configure(bg="#d9001f", activebackground='#d9001f')
root.config(bg='#d9001f')
# Tab Style
style.theme_use('default')
style.configure('TNotebook.Tab', background="#5d797e")
style.configure("TNotebook", background="#333333", borderwidth=0)
# style.configure("TNotebook.Tab", background="green", foreground=COLOR_3,, borderwidth=2)
# Style of form (background), no foreground
style.configure("TFrame", background="grey75", borderwidth=5)
style.configure("TCombobox", fieldbackground="#e5e5e5", background="#d9001f", foreground="gray1")
style.configure("TSpinbox", fieldbackground="#e5e5e5", background="#d9001f", foreground="gray1")
style.configure("TCheckbutton", fieldbackground="#dcdcdc", bg="#dcdcdc",
                foreground="gray1")
# this changes the background colour of the 2nd item
for options in range(len(aggregation_options)):
    listbox_aggregation_options.itemconfig(options, {'bg': '#dcdcdc'})
for activation_option in range(len(activation_options_values_sec)):
    activation_listbox.itemconfig(activation_option, {'bg': "#dcdcdc"})


response_from_message_box = ctypes.windll.user32.MessageBoxW(0, "Would you like to launch education mode?", "Options", 4)
education_mode = False
root.protocol("WM_DELETE_WINDOW", on_closing)

ProcessImages.process_file()

#print(gym.envs.registration.ROOT_DIR)

if response_from_message_box == 6: #yes
    education_mode = True
    root.resizable(True, False)  # Width, Height
    education_mode_normal_mode.config(image=normal_mode_pic)
    Education_listbox.selection_clear(0, END)
    Education_listbox.select_set(0)  # This only sets focus on the first item.
    Education_listbox.event_generate("<<ListboxSelect>>")
    # progressbar
    progress_Bar_Education = ttk.Progressbar(
        frame_Education,
        orient='horizontal',
        mode='determinate',
        length=280
    )
    save_progress_btn.grid()
    reset_progress_btn.grid()
    root.mainloop()

    #pyglet.app.run()
else:
    education_mode_normal_mode.config(image=education_mode_pic)
    frame_Education.grid_remove()
    education_L.grid_remove()
    Education_listbox.grid_remove()
    tabControl.tab(tab_education, state = "disabled")
    root.mainloop()
    #pyglet.app.run()


