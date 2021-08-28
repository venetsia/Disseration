#The program must:
#...
#* have inputs that:
#  - ignore meaningless keystrokes
#  - require a value for all fields, except Notes
# - get marked with an error if the value is invalid on focusout
#* prevent saving the record when errors are present

import tkinter as tk
from decimal import Decimal
from tkinter.filedialog import askopenfilename, asksaveasfilename, LEFT, VERTICAL
from tkinter import ttk, INSERT
from tkinter.font import BOLD
from tkinter.messagebox import showinfo

from Validation import ValidatedMixin


class ValidatedSpinbox(ValidatedMixin, tk.Spinbox):

    def __init__(self, *args, min_var=None, max_var=None,
                 focus_update_var=None, from_='-Infinity',
                 to='Infinity', **kwargs):
        super().__init__(*args, from_=from_, to=to, **kwargs)
        self.resolution = Decimal(str(kwargs.get('increment',
        '1.0')))
        self.precision = (
            self.resolution
            .normalize()
            .as_tuple()
            .exponent
        )