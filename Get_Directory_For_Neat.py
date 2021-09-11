import os
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import ttk, INSERT

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
    path_directory.insert(INSERT, filepath)
    path_directory.configure(state='disabled')

def open_file(txt_edit, path_directory):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    print(filepath)
    # Reverse slashes
    filepath = filepath.replace('/', '\\')
    print(filepath)
    path_directory.configure(state='normal')
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


def Get_Input(widget,path_directory, txt_edit):
    toolTip = Get_Dir_for_Neat(widget)

    def directory_selection(event):
        toolTip.select_directory(widget,path_directory, txt_edit)

    widget.bind('<FocusOut>', directory_selection)