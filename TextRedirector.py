# Class used for redirecting printed statements into widget

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.insert("end", str, (self.tag,))
    # The flush() method in Python file handling clears the internal buffer of the file
    def flush(self):
        pass