from datetime import datetime
import os
import csv
import tkinter as tk
from tkinter import ttk

class ValidatedMixin:
    """Adds a validation functionality to an input widget"""

    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)
        # The constructor also has an extra argument called
        # error_var. This will allow us to pass in a variable
        # to use for the error message; if we don't, the class
        # creates its own.

        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)

        self.config(
            validate='all',
            validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d')
        )
        # set up validation
        # We're running validation on all conditions, so we can capture
        # both focus and keystroke events.

    def _toggle_error(self, on=False):
        self.config(foreground=('red' if on else 'black'))
        # define our error condition handler

        # This will just change the text color
        # to red if there's an error, or black otherwise.

        # We don't set the error in this function, since
        # we'll want to set the actual error text in the validate method
    def _validate(self, proposed, current, char, event, index,
                  action):
        self._toggle_error(False)
        self.error.set('')
        valid = True
        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':
            valid = self._key_validate(proposed=proposed,
                                       current=current, char=char, event=event,
                                       index=index, action=action)
        return valid
        # Our _validate() method just handles a few setup chores like
        # toggling off the error and clearing the error message.

        # Then, it runs an event-specific validate method,
        # depending on the event type passed in.

        # We only care about the key and focusout events
        # right now, so any other event just returns True.
    def _focusout_validate(self, **kwargs):
        return True

    def _key_validate(self, **kwargs):
        return True

    def _invalid(self, proposed, current, char, event, index,
                 action):
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event == 'key':
            self._key_invalid(proposed=proposed,
                              current=current, char=char, event=event,
                              index=index, action=action)


    def _focusout_invalid(self, **kwargs):
        self._toggle_error(True)

    def _key_invalid(self, **kwargs):
        pass

    #  handle an invalid event

    def trigger_focusout_validation(self):
        valid = self._validate('', '', '', 'focusout', '', '')
        if not valid:
            self._focusout_invalid(event='focusout')
        return valid
        # effectively checks a completely entered value.
class RequiredEntry(ValidatedMixin, ttk.Entry):

    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid

