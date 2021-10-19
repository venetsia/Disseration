import os
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename, END
from tkinter import ttk, INSERT
import os.path
from os import path

def save_file(txt_edit, path_directory):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
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

    #Where file has been saved
    print(filepath)

    # Reverse slashes
    filepath = filepath.replace('/','\\')
    print(filepath)
    path_directory.configure(state='normal')
    path_directory.delete('1.0', END)
    path_directory.insert(INSERT, filepath)
    path_directory.configure(state='disabled')

def open_file(txt_edit, path_directory):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    print(filepath)
    # Reverse slashes
    #filepath = filepath.replace('/', '\\')
    #replace_slash = "\\"
    #res = filepath.rindex(replace_slash)
    #filepath = filepath[:res] + "/" + filepath[res + 1:]
    #filepath = os.path.normpath(filepath)
    print(path.exists(filepath))
    print(filepath)
    path_directory.configure(state='normal')
    path_directory.delete('1.0', END)
    path_directory.insert(INSERT, filepath)
    path_directory.configure(state='disabled')

def open_file_run_neat(txt_edit, path_directory, num_generations, num_generations_l):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    # If File path does not exist - return
    if not filepath:
        return

    with open(filepath, "r") as input_file:
        text = input_file.read()  # Read file
        for line in text.split("\n"):
            if "no_fitness_termination" in line:
                no_fitness_termination_value = line.split("=", 1)[1]
                if no_fitness_termination_value.strip() == "True":
                    num_generations.grid()
                    num_generations_l.grid()
                else:
                    num_generations.grid_remove()
                    num_generations_l.grid_remove()

    print(filepath)
    # Reverse slashes
    #filepath = filepath.replace('/', '\\')
    #replace_slash = "\\"
    #res = filepath.rindex(replace_slash)
    #filepath = filepath[:res] + "/" + filepath[res + 1:]
    #filepath = os.path.normpath(filepath)
    print(path.exists(filepath))
    print(filepath)
    path_directory.configure(state='normal')
    path_directory.delete('1.0', END)
    path_directory.insert(INSERT, filepath)
    path_directory.configure(state='disabled')

def open_file_checkpoint_run_neat(txt_edit, path_directory):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )

    # If File path does not exist - return
    if not filepath:
        return

    path_directory.configure(state='normal')
    path_directory.delete('1.0', END)
    path_directory.insert(INSERT, filepath)
    path_directory.configure(state='disabled')

class Get_Dir_for_Neat(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def select_directory(self, widget, path_directory, txt_edit):
        if widget.get()== "From Text Editor":
            save_file(txt_edit, path_directory)
        elif widget.get() == "Choose file from directory":
            open_file(txt_edit, path_directory)
    def select_directory_run_Neat(self, widget, path_directory, txt_edit, num_generations, num_generations_l):
        if widget.get()== "From Text Editor":
            save_file(txt_edit, path_directory)
        elif widget.get() == "Choose file from directory":
            open_file_run_neat(txt_edit, path_directory, num_generations, num_generations_l)
        elif widget.get() == "Restore from Checkpoint":
            open_file_checkpoint_run_neat(txt_edit, path_directory)

def Get_Input(widget,path_directory, txt_edit, num_generations, num_generations_l):
    toolTip = Get_Dir_for_Neat(widget)

    def directory_selection(event):
        widget_name = widget._name
        if "winner" not in widget_name:
            toolTip.select_directory_run_Neat(widget,path_directory, txt_edit, num_generations, num_generations_l)
        else:
            toolTip.select_directory(widget, path_directory, txt_edit)

    widget.bind('<FocusOut>', directory_selection)

def run_NEAT_get_input(widget,path_directory, txt_edit,num_generations, num_generations_l):
    toolTip_run_neat = Get_Dir_for_Neat(widget)

    def directory_selection_Run_neat(event):
        toolTip_run_neat.select_directory_run_Neat(widget,path_directory, txt_edit, num_generations, num_generations_l)

    widget.bind('<FocusOut>', directory_selection_Run_neat)