from datetime import datetime
import os
import csv
import tkinter as tk
from tkinter import ttk



class LabelInput(tk.Frame):
    """A widget containing a label and input together."""

    def __init__(self, parent, label='', input_class=ttk.Entry,
                 input_var=None, input_args=None, label_args=None,
                 **kwargs):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["text"] = label
            input_args["variable"] = input_var
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
            input_args["textvariable"] = input_var

        self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        super().grid(sticky=sticky, **kwargs)

    def get(self):
        if self.variable:
            print(self.variable.get())
            return self.variable.get()
        elif type(self.input) == tk.Text:
            return self.input.get('1.0', tk.END)
        else:
            return self.input.get()

    def set(self, value, *args, **kwargs):
        if type(self.variable) == tk.BooleanVar:
            self.variable.set(bool(value))
        elif self.variable:
            self.variable.set(value, *args, **kwargs)
        elif type(self.input).__name__.endswith('button'):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else:
            self.input.delete(0, tk.END)
            self.input.insert(0, value)

class TextEditor(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets
        self.inputs = {}

        self.textArea = tk.Text(self)
        # recordinfo section

class DataRecordForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets
        self.inputs = {}

        # recordinfo section
        neat_Section = tk.LabelFrame(self, text="NEAT Section")

        # fitness_criterion
        self.inputs['fitness_criterion'] = LabelInput(
            neat_Section, "Fitness Criterion",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["min", "max", "mean"]}
        )
        self.inputs['fitness_criterion'].grid(row=0, column=0)

        # fitness_threshold
        self.inputs['fitness_threshold'] = LabelInput(
            neat_Section, "Fitness Threshold",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 100000000, "increment": 1}
        )
        self.inputs['fitness_threshold'].grid(row=0, column=1)

        # pop_size
        self.inputs['pop_size'] = LabelInput(
            neat_Section, "Population Size",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000000, "increment": 1}
        )
        self.inputs['pop_size'].grid(row=0, column=2)

        # no_fitness_termination
        self.inputs['no_fitness_termination'] = LabelInput(
            neat_Section, "Fitness Termination?",
            input_class=ttk.Checkbutton,
            input_var=tk.BooleanVar())
        self.inputs['no_fitness_termination'].grid(
            row=1, column=0, columnspan=3)
        self.inputs['no_fitness_termination'].grid(row=1, column=0)

        # reset_on_extinction
        self.inputs['reset_on_extinction'] = LabelInput(
            neat_Section, "Reset on extinction?",
            input_class=ttk.Checkbutton,
            input_var=tk.BooleanVar())
        self.inputs['reset_on_extinction'].grid(row=1, column=1)

        neat_Section.grid(row=0, column=0, sticky=(tk.W + tk.E))

        # default_Stagnation_section
        default_Stagnation_section = tk.LabelFrame(self, text="Stagnation section")

        # species_fitness_func
        self.inputs['species_fitness_func'] = LabelInput(
            default_Stagnation_section, "Species Fitness Function)",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["max", "min", "mean", "median"]}
        )
        self.inputs['species_fitness_func'].grid(row=0, column=0)

        # max_stagnation
        self.inputs['max_stagnation'] = LabelInput(
            default_Stagnation_section, "Maximum Stagnation",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000, "increment": 1}
        )
        self.inputs['max_stagnation'].grid(row=0, column=1)

        # species_elitism
        self.inputs['species_elitism'] = LabelInput(
            default_Stagnation_section, "Protected Species from stagnation",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000, "increment": 1}
        )
        self.inputs['species_elitism'].grid(row=0, column=2)

        default_Stagnation_section.grid(row=1, column=0, sticky=(tk.W + tk.E))

        # Plant Data section
        default_Reproduction = tk.LabelFrame(self, text="Reproduction")

        # elitism
        self.inputs['elitism'] = LabelInput(
            default_Reproduction, "Protected Num of most-fit individuals in each species (elitism)",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000, "increment": 1}
        )
        self.inputs['elitism'].grid(row=0, column=0)

        # survival_threshold
        self.inputs['survival_threshold'] = LabelInput(
            default_Reproduction, "Fraction of species allowed to reproduce",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1000, "increment": .1}
        )
        self.inputs['survival_threshold'].grid(row=0, column=1)

        # min_species_size
        self.inputs['min_species_size'] = LabelInput(
            default_Reproduction, "Min number of genomes after reproduction (per species)",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000, "increment": 1}
        )
        self.inputs['min_species_size'].grid(row=0, column=2)

        default_Reproduction.grid(row=2, column=0, sticky=(tk.W + tk.E))

        default_Genome = tk.LabelFrame(self, text="Genome section")

        # activation_default
        self.inputs['activation_default'] = LabelInput(
            default_Genome, "Activation Function Default)",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={
                "values": ["none", "abs", "clamped", "cube", "exp", "gauss", "hat", "identity", "inv", "log", "relu",
                           "elu", "lelu", "selu", "sigmoid", "sin", "softplus", "square", "tanh"]}
        )
        self.inputs['activation_default'].grid(row=0, column=0)

        # activation_mutate_rate
        self.inputs['activation_mutate_rate'] = LabelInput(
            default_Genome, "Activation Mutate Rate)",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1, "increment": 0.1}
        )
        self.inputs['activation_mutate_rate'].grid(row=0, column=1)

        # aggregation_options
        self.inputs['aggregation_options'] = LabelInput(
            default_Genome, "Aggregation Options)",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={
                "values": ["sum", "min", "max", "mean", "median", "product"]}
        )
        self.inputs['aggregation_options'].grid(row=0, column=2)

        # bias_init_mean
        self.inputs['bias_init_mean'] = LabelInput(
            default_Genome, "Bias Initial Mean",
            input_class=ttk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000, "increment": 0.1}
        )
        self.inputs['bias_init_mean'].grid(row=0, column=3)

        # bias_init_stdev
        self.inputs['bias_init_stdev'] = LabelInput(
            default_Genome, "Bias Initial standard",
            input_class=ttk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000, "increment": 0.1}
        )
        self.inputs['bias_init_stdev'].grid(row=0, column=4)

        # bias_init_type
        self.inputs['bias_init_type'] = LabelInput(
            default_Genome, "Bias Initial type)",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={
                "values": ["gaussian", "normal", "uniform"]}
        )
        self.inputs['bias_init_type'].grid(row=0, column=5)

        # bias_min_value
        self.inputs['bias_min_value'] = LabelInput(
            default_Genome, "Bias Min Value",
            input_class=ttk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 1}
        )
        self.inputs['bias_min_value'].grid(row=1, column=0)

        # bias_max_value
        self.inputs['bias_max_value'] = LabelInput(
            default_Genome, "Bias Max value",
            input_class=ttk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 1}
        )
        self.inputs['bias_max_value'].grid(row=1, column=1)

        # bias_mutate_power
        self.inputs['bias_mutate_power'] = LabelInput(
            default_Genome, "Bias Mutate Power",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 0.1}
        )
        self.inputs['bias_mutate_power'].grid(row=1, column=2)

        # bias_mutate_rate
        self.inputs['bias_mutate_rate'] = LabelInput(
            default_Genome, "Bias Mutate Rate",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 0.1}
        )
        self.inputs['bias_mutate_rate'].grid(row=1, column=3)

        # bias_replace_rate
        self.inputs['bias_replace_rate'] = LabelInput(
            default_Genome, "Bias Replace Rate",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 0.1}
        )
        self.inputs['bias_replace_rate'].grid(row=1, column=4)

        # compatibility_threshold
        self.inputs['compatibility_threshold'] = LabelInput(
            default_Genome, "Compatibility Threshold",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 0.1}
        )
        self.inputs['compatibility_threshold'].grid(row=1, column=5)

        # compatibility_disjoint_coefficient
        self.inputs['compatibility_disjoint_coefficient'] = LabelInput(
            default_Genome, "Compatibility Disjoint Coefficient",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 0.1}
        )
        self.inputs['compatibility_disjoint_coefficient'].grid(row=2, column=0)

        # compatibility_disjoint_coefficient
        self.inputs['compatibility_weight_coefficient'] = LabelInput(
            default_Genome, "Compatibility Weight Coefficient",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": -1000, "to": 1000, "increment": 0.1}
        )
        self.inputs['compatibility_weight_coefficient'].grid(row=2, column=1)

        # conn_add_prob
        self.inputs['conn_add_prob'] = LabelInput(
            default_Genome, "Connection add probability of mutate",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1, "increment": 0.1}
        )
        self.inputs['conn_add_prob'].grid(row=2, column=2)

        # conn_delete_prob
        self.inputs['conn_delete_prob'] = LabelInput(
            default_Genome, "Connection delete probability of mutate",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1, "increment": 0.1}
        )
        self.inputs['conn_delete_prob'].grid(row=2, column=3)

        # enabled_default
        self.inputs['enabled_default'] = LabelInput(
            default_Genome, "Enabled attribute of new created conn?",
            input_class=ttk.Checkbutton,
            input_var=tk.BooleanVar())
        self.inputs['enabled_default'].grid(row=2, column=5)

        # conn_delete_prob
        self.inputs['enabled_mutate_rate'] = LabelInput(
            default_Genome, "Probability that mutation will replace",
            input_class=ttk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1, "increment": 0.1}
        )
        self.inputs['enabled_mutate_rate'].grid(row=2, column=4)

        # initial_connection
        initial_connection = self.inputs['initial_connection'] = LabelInput(
            default_Genome, "Initial conn of new genomes",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={
                "values": ["unconnected", "fs_neat_nohidden", "fs_neat_hidden", "full_nodirect", "full_direct",
                           "partial_nodirect #", "partial_direct #"]}
        )
        self.inputs['initial_connection'].grid(row=3, column=0)


        default_Genome.grid(row=3, column=0, sticky=(tk.W + tk.E))
        # default the form
        self.reset()



    def get(self):
        """Retrieve data from form as a dict"""

        # We need to retrieve the data from Tkinter variables
        # and place it in regular Python objects

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        """Resets the form entries"""
        # clear all values
        for widget in self.inputs.values():
            widget.set('')



class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("NEAT Config File")
        self.resizable(width=False, height=False)
        n = ttk.Notebook(self)
        n1 = ttk.Notebook(self)
        f1 = ttk.Frame(n)  # first page, which would get widgets gridded into it
        f2 = ttk.Frame(n)  # second page
        f3 =ttk.Frame(n1)
        f4 =ttk.Frame(n1)
        n.add(f1, text='One')
        n.add(f2, text='Two')
        ttk.Label(
            self,
            text="NEAT Configuration",
            font=("TkDefaultFont", 16)
        ).grid(row=0)
        # Build the form

        self.recordform = DataRecordForm(self)
        self.recordform.grid(row=1, column = 1, padx=10)

        self.textEditor = TextEditor(self)
        self.textEditor.grid(row = 1)

        self.savebutton = ttk.Button(self, text="Save", command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2, padx=10)

        # status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

        self.records_saved = 0

    def on_save(self):
        """Handles save button clicks"""

        # For now, we save to a hardcoded filename with a datestring.
        # If it doesnt' exist, create it,
        # otherwise just append to the existing file
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "abq_data_record_{}.csv".format(datestring)
        newfile = not os.path.exists(filename)

        data = self.recordform.get()

        with open(filename, 'a') as fh:
            csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
            if newfile:
                csvwriter.writeheader()
            csvwriter.writerow(data)

        self.records_saved += 1
        self.status.set(
            "{} records saved this session".format(self.records_saved))
        self.recordform.reset()


if __name__ == "__main__":
    app = Application()
    textEditor = TextEditor()
    app.mainloop()
    textEditor.mainloop()
