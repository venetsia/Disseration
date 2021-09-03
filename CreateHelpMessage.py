from tkinter import *

class CreateHelpMessage(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
    def enableWidged(self,widget,widget1):
        if (widget.get() == "partial_nodirect" or widget.get() == "partial_direct"):
            widget1.config(state="enabled")
        else:
            widget1.set("")
            widget1.config(state="disabled")

def CreateToolTip(widget, text):
    toolTip = CreateHelpMessage(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def Validate(widget,widget1):
    toolTip = CreateHelpMessage(widget)

    def enable(event):
        toolTip.enableWidged(widget,widget1)
    widget.bind('<Enter>', enable)


