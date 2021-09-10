from tkinter import END
from io import StringIO
import sys
import gym

#This build in console cannot get the variables from TextEditor
class Build_in_Console(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def console_output(self,widget, game_selection):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        # If game is empty - do not continue with function
        # just exit function
        if game_selection.get() == "":
            print("Game is not selected")
            message = mystdout.getvalue()
            widget.insert(END, "\n" + message)
            return
        env = gym.make(game_selection.get())

        if widget.get(1.0, "end-1c") == "exit":
            pass
        try:
            y = eval(widget.get(1.0, "end-1c"))
            sys.stdout = old_stdout
            message = mystdout.getvalue()
            widget.insert(END,"\n" + message)
        except:
            try:
                #sys.stdout = sys.__stdout__
                exec(widget.get(1.0, "end-1c"))
            except Exception as e:
                print("error:", e)
                message = mystdout.getvalue()
                widget.insert(END,"\n" + message)
def Get_Console_input(widget, game_selection):
    input_from_widget = Build_in_Console(widget)

    def leave(event):
        input_from_widget.console_output(widget, game_selection)

    widget.bind('<Return>', leave)