import tkinter as tk

class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def load_content(self,education_option_selected,educatuin_tab):
        print("Test")
        if education_option_selected.get(education_option_selected.curselection()) == "Introduction":
            # Neat Section
            introduction_to_software_l = tk.Label(educatuin_tab, text='Introduction to the software', font='Helvetica 12 bold underline', justify=tk.LEFT,
                                      anchor="w")
            introduction_to_software_l.grid(row=0, column=0, ipadx=32, pady=1)

            how_does_work_l = tk.Label(educatuin_tab, text='How does the education tool work?',justify=tk.LEFT,anchor="w", font='Helvetica 10 bold')
            how_does_work_l.grid(row=1, column=0, ipadx=32, pady=1)
            explain_how_does_it_work_l = tk.Label(educatuin_tab, text=' Throughout the use of the educational tool you will be able to understand how can you use the software to edit the NEAT config file'
                                                                      'and train a neural network using the NEAT algorithm to play a game of your chouse.\nIn the beginning you will have simple task you need '
                                                                      'to complete in order to proceed.', justify=tk.LEFT,
                                                anchor="w", font='Helvetica 10')
            explain_how_does_it_work_l.grid(row=2, column=0, ipadx=32, pady=1)
            neat_config_tab_l = tk.Label(educatuin_tab, text='NEAT Config Tab', justify=tk.LEFT, anchor="w",
                                       font='Helvetica 10 bold')
            neat_config_tab_l.grid(row=3, column=0, ipadx=32, pady=1)
            explain_how_does_it_work_l = tk.Label(educatuin_tab,
                                                  text=' The NEAT config tab in educational mode has fewer selections so it can make it easier for you to understand essentials when training a neural network. As you progress'
                                                       'more options will become available.\n In addition the tab will allow you to edit any existing config files and structure them appropriately so you can change values.'
                                                       'If you hover over a form value input you will see some information regarding it', justify=tk.LEFT,
                                                  anchor="w", font='Helvetica 10')
            explain_how_does_it_work_l.grid(row=4, column=0, ipadx=32, pady=1)
            neat_config_tab_l = tk.Label(educatuin_tab, text='NEAT Setup Tab', justify=tk.LEFT, anchor="w",
                                         font='Helvetica 10 bold')
            neat_config_tab_l.grid(row=5, column=0, ipadx=32, pady=1)
            explain_how_does_it_work_l = tk.Label(educatuin_tab,
                                                  text=' The NEAT setup tab is where you:\n - Gym Game: choose your game from the gym environment\n - Evaluate Genomes: you can choose how you evauate genomes'
                                                       '\n - Winner file name: choose winner file name'
                                                       '\n - Checkpoint: how often would you like to save checkpoints so you can see progress'
                                                       '\n - Network Type: what kind of network type would you like to use'
                                                       '\n - Render Window: whether or not you would like to see the AI learn\n'
                                                       ' - Config File: configuration file that the neural network will use.',
                                                  justify=tk.LEFT,
                                                  anchor="w", font='Helvetica 10')
            explain_how_does_it_work_l.grid(row=6, column=0, ipadx=32, pady=1)

def Activate_Content(education_option_selected, educatuin_tab):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab)

    education_option_selected.bind('<<ListboxSelect>>', load_content)