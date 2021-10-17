import random
import tkinter as tk
import numpy as np
from PIL import ImageTk
import pyautogui
import CreateHelpMessage
import ProcessImages
import StickyNote
import train_chat_BOT


education_mode_labels = ["label1", "label2", "chat_bot_dynamic_learn"]
AI_tab = ["label1"]
AI_categories_tab = ["label2"]
label1 =""
label2 =""
agent_label1 =""
clicks = 0
chat_bot_dynamic_learn =""
response_enter =""
chatbot_next =""
#neuron_tab_pic = ""
neuron_tab_label =""
#perceptron_image = ""
perceptron_label = ""
check_answer = ""
how_learn_nn_label =""
reference_from_source = ""

Introduction_tab = False
Artificial_intelligence_tab = False
AI_Categories_tab = False
AI_Categories_tab_2 = False
Intelligent_Agents_tab = False
Neuron_tab = False
Perceptron_tab = False
Components_of_NN = False
Learning_Types = False
Neat_config_choice = False
LoadWinner = False
LoadWinner2 = False
Run_Neat_choice = False
How_Lean_NN = False
ReinforcementL1 = False
ReinforcementL2 = False
ReinforcementL3 = False

class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0



    def hide_old_widgets(self, widget):
        widget.grid_remove()
        return
    def next_button(self, chat_bot_dynamic_learn, response_enter, educatuin_tab):
        global agent_label1
        global reference_from_source
        input = response_enter.get("1.0", tk.END)
        response_enter.delete('1.0', tk.END)
        results = train_chat_BOT.model.predict([train_chat_BOT.bag_of_words(input, train_chat_BOT.words)])[0]
        results_index = np.argmax(results)
        tag = train_chat_BOT.classes[results_index]
        if results[results_index] > 0.7:
            for tg in train_chat_BOT.intents["intents"]:
                if tg["tag"] == tag:
                    responses = tg["responses"]
            if tag =="evaluate":
                agent_label1 = tk.Label(educatuin_tab, image=ProcessImages.image_agent)
                agent_label1.image = ProcessImages.image_agent
                agent_label1.grid(row=1, column=1)
                agent_label1.config(fg="grey75", bg="grey75")
                reference_from_source = tk.Label(educatuin_tab, text = "Figure 2 Agent interacts with Environments through sensors and effectors (Russell & Norvig, 1995, fig. 2.1)")
                reference_from_source.grid(row=2,column=2)
                reference_from_source.config(fg="grey75", bg="grey75")
            elif tag != "evaluate":
                if agent_label1 != "":
                    self.hide_old_widgets(agent_label1)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
            chat_bot_dynamic_learn.insert(tk.END,"You: " + input + "\nAgent: " + random.choice(responses) + "\n")
        else:
            chat_bot_dynamic_learn.insert(tk.END,"I didn't get that, try again please.")
    def check_answer(self,value,widget):
        input = widget.get("1.0", tk.END)
        input = input.lower()
        if value == "Neural Network":
            if input in "hidden layer" or input.lower() in "hidden-layer" or input.find("hidden-layer") == 0 or input.find("hidden layer") == 0:
                widget.config(bg="green")
            else:
                widget.config(bg="red")
        elif value == "Learning Types":
            if input.find("reinforcement learning (rl)") == 0 or input.find("reinforcement learning (rl)") == 0 or input.find("reinforcement learning") == 0 or input.find("reinforcement learning") == 0 or input.find("rl") == 0 or input.find("rl") == 0 or input.find("reinforcement") == 0 or input.find("reinforcement") == 0 :
                widget.config(bg="green")
            else:
                widget.config(bg="red")
    def nada(self):
       return
    def automate(self, hidden_level_text,educatuin_tab):
        hidden_level_value = hidden_level_text.get(1.0, tk.END)
        if hidden_level_value == "False\n":
            # Locate Neat Icon
            window_icon = pyautogui.locateOnScreen("NeatConfigImage.PNG")
            print(window_icon)
            # Click Windows Icon
            pyautogui.click(window_icon)
            hidden_level_text.delete(1.0, tk.END)
            print(hidden_level_text.get(1.0, tk.END))
            hidden_level_text.insert(tk.END, "False")
            print(hidden_level_text.get(1.0, tk.END))
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0, "Lets start with the basics. Each learning algorithm will need a variation of these values.\n"
                               "If we select a game we will see that input and output are automatically generated for us based on the game."
                               "\nNeat section:"
                               "\n-fitness_criterion - how our score is calculated (max, min, etc)"
                               "\n-fitness_threshold - how fit we want the agent to become"
                               "\n-pop_size - how many genomes do we want to start with"
                               "\nGenome Section:"
                               "\n-num_inputs - what can the agent see "
                               "\n-num_outputs - actions agent can perform"
                                        "\nThe values are filled out automatically so you can see."
                                        "\nSo the game is CartPole.\nIt has 4 valid observations for input."
                                        "\nFor output we have 2 valid actions (0 or 1) - move left or right"
                                        "\nBecause of fitness_criterion being max we will look for the best genome."
                                        "\nOur agent will stop learning when a genome reaches a score of 500")
            hidden_level_text.delete(1.0, tk.END)
            print(hidden_level_text.get(1.0, tk.END))
            hidden_level_text.insert(tk.END, "ExampleLevel1")
            print(hidden_level_text.get(1.0, tk.END))
        elif hidden_level_value == "LoadWinnerExample\n":
            window_icon = pyautogui.locateOnScreen("Load_Winner.PNG")
            # Click Windows Icon
            pyautogui.click(window_icon)
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0,
                                   "Okey now that we know how can we run NEAT, we will see an example of the previous NEAT configurations we have chosen."
                                   "\nWe have to choose the game we the winner is trained on."
                                   "\nWe also need to specify the name of the winner file"
                                   "\nNumber of episodes per genomes means how many times/episodes do we want to test our winner on."
                                   "\nWe can also view the checkpoints that our algorithm has made. We can change the directory so the software can detect in different directory for checkpoints."
                                   "\n(they have to be marked as 'neat-checkpoint' in order for the software to detect it.)"
                                   "\nWe will look into the network type later but we should choose the same one we have trained it on."
                                   "\nThe config file can be either saved from editor or chosen from directory"
                                   "\nWhen you are ready you can click 'Load Genomes and winner' and you will observe the checkpoints. They load howeever many genomes (population) the generation has. "
                                   "\nYou can see which one is loaded from the below text field.")
        elif hidden_level_value == "LoadWinnerExample2\n":
            window_icon = pyautogui.locateOnScreen("Load_Winner.PNG")
            # Click Windows Icon
            pyautogui.click(window_icon)
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0,"Lets see another game example. The game we will see is Lunar Lander and we have 8 inputs and 4 outputs.\n"
                                       "Here it took a little longer for NEAT to figure out how to reach the threshold (goal) so we will see checkpoints 10 generations apart and then we will see the winner.")
        elif hidden_level_value == "RunNEATExample\n":
            window_icon = pyautogui.locateOnScreen("RunNeatTab.PNG")
            # Click Windows Icon
            pyautogui.click(window_icon)
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0,
                                   "Now that we have seen what the NEAT algorithm actually does we can now train an agent.\n"
                                   "On this tab you are able to specify which game would you like to train the agent on - for this example we will move onto more complcated games (the Atari games, specifically Breakout-v0).\n"
                                   "The evaluation will be single-processing which means it will run on one core (one agent at a time).\n"
                                   "You can see that there are some red fields and one of them is Winner file name is also in red: Please name your file for the winner.\n"
                                   "Save Checkpoints' is not in red because you can leave empty but if you would like any checkpoints saved. If you select a number bigger than 0 it will save the 0 generation always. Let's say you have inputed 5, it will save every 5 generations. We earlier saw that we can load checkpoints and view them. You can leave it empty."
                                   "The network type will stay FeedForward. - we will se later what it means and what is the other option."
                                   "\nRender Window is also in red so please choose if you would like to view the agent while it is being trained."
                                   "\nThe configuration file is selected but if you would like to include another file you can do so from selecting the dropdown. The config file can be edited or made entirely in app. If you do not know how many inputs and outputs the game needs you can choose 'Check config file for input/output' and it will show you on the 'Enter Command' what modifications will happen in config."
                                   "\nOn the last text field you will be able to view generations, the genomes within them, their fitness, etc."
                                   "\nOnce you select a field on the screen 'Run Per Network' will appear. If you choose 2 for example each genome (agent) being trained will have 2 tries on the game. (if 0 is selected it will just run once)")
    def load_content(self,education_option_selected,educatuin_tab, hidden_level_text):
        selected_indices = education_option_selected.curselection()
        value = education_option_selected.get(selected_indices[0])
        global Artificial_intelligence_tab
        global AI_Categories_tab
        global AI_Categories_tab_2
        global Intelligent_Agents_tab
        global Neuron_tab
        global Perceptron_tab
        global Components_of_NN
        global Learning_Types
        global How_Lean_NN
        global ReinforcementL2
        global ReinforcementL1
        global Neat_config_choice
        global LoadWinner
        global LoadWinner2
        global Run_Neat_choice

        global how_learn_nn_label
        global label1
        global label2
        global reference_from_source
        global chat_bot_dynamic_learn
        global response_enter
        global chatbot_next
        global neuron_tab_pic
        global neuron_tab_label
        global perceptron_image
        global perceptron_label
        global check_answer
        if value == "Artificial Intelligence":
            Artificial_intelligence_tab = True
            if label2 != "":
                self.hide_old_widgets(label2)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if neuron_tab_label != "":
                self.hide_old_widgets(neuron_tab_label)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            if reference_from_source != "":
                self.hide_old_widgets(reference_from_source)
            if how_learn_nn_label != "":
                self.hide_old_widgets(how_learn_nn_label)
            label1 = tk.Label(educatuin_tab, image=ProcessImages.image1)
            label1.image = ProcessImages.image1
            label1.grid(row=1,column = 0)
            label1.config(fg="grey75", bg="grey75")
            reference_from_source = tk.Label(educatuin_tab,
                                             text="(Russell & Norvig, 1995, Chapter 1 Introduction; Taulli, 2019,\n Chapter 1 AI Foundations; Paul Mueller & Massaron, 2018)",
                                             font=("Courier", 14, "bold"))
            reference_from_source.config(bg="grey75")
            reference_from_source.grid(row=2, column=0)

        elif value == "AI categories L1":
            if Artificial_intelligence_tab == True:
                AI_Categories_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label1 = tk.Label(educatuin_tab, image=ProcessImages.image2)
                label1.image = ProcessImages.image2
                label1.grid(row=1, column=0)
                label1.config(fg="grey75", bg="grey75")
                reference_from_source = tk.Label(educatuin_tab,
                                                 text="(Russell & Norvig, 1995, Chapter 1 Introduction; Taulli, 2019, Chapter 1 AI Foundations; Paul Mueller & Massaron, 2018)",
                                                 font=("Courier", 14, "bold"))
                reference_from_source.config(bg="grey75")
                reference_from_source.grid(row=2, column=0)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text = "Please refer to Artificial Intelligence lesson first", font = ("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "AI categories L2":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True:
                AI_Categories_tab_2 = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label1 = tk.Label(educatuin_tab, image=ProcessImages.image3)
                label1.image = ProcessImages.image3
                label1.grid(row=1, column=0)
                label1.config(fg="grey75", bg="grey75")
                reference_from_source = tk.Label(educatuin_tab, text = "(Russell & Norvig, 1995, Chapter 1 Introduction; Taulli, 2019, Chapter 1 AI Foundations; Paul Mueller & Massaron, 2018)", font = ("Courier", 14, "bold"))
                reference_from_source.config(bg="grey75")
                reference_from_source.grid(row=2, column=0)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text = "Please refer to AI categories L1 lesson first", font = ("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Intelligent Agents":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True:
                Intelligent_Agents_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                chat_bot_dynamic_learn = tk.Text(educatuin_tab, name="chat_bot_dynamic_learn", height=50, width=70)
                chat_bot_dynamic_learn.grid(row=1, column=0, sticky=tk.W)
                response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
                response_enter.grid(row=2, column=0, sticky=tk.W)
                chat_bot_dynamic_learn.bind('<Key>', lambda e: 'break')
                chat_bot_dynamic_learn.insert(tk.END, "Welcome, I am a chat bot and I am here to answer some questions.\nFor this specific tab you may want to ask questions such as:"
                                                      "\n\"What is an agent?\"\n\"How and when do we evauate an agent?\"\nYou can refer back to this whenever you would like to ask a question. I am trained in answering a few questions.\n")
                # Run button for Neat using a thread
                chatbot_next = tk.Button(educatuin_tab, text="Send",
                                         command=lambda : self.next_button(chat_bot_dynamic_learn, response_enter, educatuin_tab),
                                         justify=tk.LEFT, anchor="w")
                chatbot_next.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
                CreateHelpMessage.CreateToolTip_For_Education_Mode(response_enter, "Dear User, Welcome to intelligent agents lessen. This chat bot is an intelligent agent trained by a neural network. We will look into this next. For now we will see what an agent is by answering two questions. You can refer back to this chat as it was trained to recognise some topics and answer some questions.")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                label2 = tk.Label(educatuin_tab, text = "Please refer to AI categories lesson first", font = ("Courier", 20, "bold") )
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Neuron":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True:
                Neuron_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                neuron_tab_pic = ImageTk.PhotoImage(file="biological_neuron.png")
                neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
                neuron_tab_label.image = neuron_tab_pic
                neuron_tab_label.grid(row=1, column=0)
                neuron_tab_label.config(fg="grey75", bg="grey75")
                reference_from_source = tk.Label(educatuin_tab,
                                                 text="(Russell & Norvig, 1995, Chapter 19.1 How the brain works)",
                                                 font=("Courier", 14, "bold"))
                reference_from_source.config(bg="grey75")
                reference_from_source.grid(row=2, column=0)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Intelligent Agents lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Neural Network":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and Neuron_tab == True and AI_Categories_tab_2 == True:
                Perceptron_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                perceptron_label = tk.Label(educatuin_tab, image=ProcessImages.perceptron_image)
                perceptron_label.image = ProcessImages.perceptron_image
                perceptron_label.grid(row=1, column=0)
                perceptron_label.config(fg="grey75", bg="grey75")
                response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
                response_enter.grid(row=2, column=0, sticky=tk.W)
                # Run button for Neat using a thread
                check_answer = tk.Button(educatuin_tab, text="Check answer",
                                         command=lambda: self.check_answer(value,response_enter),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Neuron lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Components of a neural network":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True\
                    and Neuron_tab == True and Perceptron_tab == True and AI_Categories_tab_2 == True:
                Components_of_NN = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                neuron_tab_label = tk.Label(educatuin_tab, image=ProcessImages.neuron_tab_pic_1)
                neuron_tab_label.image = ProcessImages.neuron_tab_pic_1
                neuron_tab_label.grid(row=1, column=0)
                neuron_tab_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Neural Network lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Learning Types":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True \
                    and Neuron_tab == True and Perceptron_tab == True and Components_of_NN == True and AI_Categories_tab_2 == True:
                Learning_Types =True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                neuron_tab_label = tk.Label(educatuin_tab, image=ProcessImages.learning_types)
                neuron_tab_label.image = ProcessImages.learning_types
                neuron_tab_label.grid(row=1, column=0)
                neuron_tab_label.config(fg="grey75", bg="grey75")
                response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
                response_enter.grid(row=2, column=0, sticky=tk.W)
                # Run button for Neat using a thread
                check_answer = tk.Button(educatuin_tab, text="Check answer",
                                         command=lambda: self.check_answer(value,response_enter),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Component of neural network lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "How do the neural network learn?":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and \
                    Neuron_tab == True and Perceptron_tab == True and Components_of_NN == True and Learning_Types == True and AI_Categories_tab_2 == True:
                How_Lean_NN = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                how_learn_nn_label = tk.Label(educatuin_tab, image=ProcessImages.how_learn_nn)
                how_learn_nn_label.image = ProcessImages.how_learn_nn
                how_learn_nn_label.grid(row=1, column=0)
                how_learn_nn_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Learning Types lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Reinforcement Learning L1":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and Neuron_tab == True and\
                    Perceptron_tab == True and Components_of_NN == True and Learning_Types == True and How_Lean_NN == True and AI_Categories_tab_2 == True:
                ReinforcementL1 = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                how_learn_nn_label = tk.Label(educatuin_tab, image=ProcessImages.reinforcement_Learning_1)
                how_learn_nn_label.image = ProcessImages.reinforcement_Learning_1
                how_learn_nn_label.grid(row=1, column=0)
                how_learn_nn_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to How do the neural network learn? first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Reinforcement Learning L2":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and Neuron_tab == True and\
                    Perceptron_tab == True and Components_of_NN == True and Learning_Types == True and How_Lean_NN == True and ReinforcementL1 == True and AI_Categories_tab_2 == True:
                ReinforcementL2 = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                how_learn_nn_label = tk.Label(educatuin_tab, image=ProcessImages.reinforcement_Learning_2)
                how_learn_nn_label.image = ProcessImages.reinforcement_Learning_2
                how_learn_nn_label.grid(row=1, column=0)
                how_learn_nn_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Reinforcement Learning L1 first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Reinforcement Learning L3":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and Neuron_tab == True and \
                    Perceptron_tab == True and Components_of_NN == True and Learning_Types == True and How_Lean_NN == True and ReinforcementL1 == True and AI_Categories_tab_2 == True:
                ReinforcementL2 = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                how_learn_nn_label = tk.Label(educatuin_tab, image=ProcessImages.reinforcement_Learning_3)
                how_learn_nn_label.image = ProcessImages.reinforcement_Learning_3
                how_learn_nn_label.grid(row=1, column=0)
                how_learn_nn_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Reinforcement Learning L2 first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "NEAT Config File":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True \
                    and Neuron_tab == True and Perceptron_tab == True and Learning_Types == True and Components_of_NN == True and How_Lean_NN == True and AI_Categories_tab_2 == True:
                Neat_config_choice = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                check_answer = tk.Button(educatuin_tab, text="Start",
                                         command=lambda: self.automate(hidden_level_text,educatuin_tab),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Learning Types lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Load Winner/Checkpoints E1":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True \
                    and Neuron_tab == True and Perceptron_tab == True and Learning_Types == True and Components_of_NN == True\
                    and Neat_config_choice == True and AI_Categories_tab_2 == True:
                LoadWinner = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                check_answer = tk.Button(educatuin_tab, text="See Winner/Checkpoint(s)",
                                         command=lambda: self.automate(hidden_level_text, educatuin_tab),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to NEAT Config File lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Load Winner/Checkpoints E2":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True \
                    and Neuron_tab == True and Perceptron_tab == True and Learning_Types == True and Components_of_NN == True \
                    and Neat_config_choice == True and LoadWinner == True and AI_Categories_tab_2 == True:
                LoadWinner2 = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                check_answer = tk.Button(educatuin_tab, text="See Winner/Checkpoint(s)",
                                         command=lambda: self.automate(hidden_level_text, educatuin_tab),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Load Winner/Checkpoints E1 lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Run NEAT E1":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True \
                    and Neuron_tab == True and Perceptron_tab == True and Learning_Types == True and Components_of_NN == True \
                    and Neat_config_choice == True and LoadWinner == True and LoadWinner2 == True and AI_Categories_tab_2 == True:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                Run_Neat_choice = True
                check_answer = tk.Button(educatuin_tab, text="See how to Run Neat",
                                         command=lambda: self.automate(hidden_level_text, educatuin_tab),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                if reference_from_source != "":
                    self.hide_old_widgets(reference_from_source)
                if how_learn_nn_label != "":
                    self.hide_old_widgets(how_learn_nn_label)
                label2 = tk.Label(educatuin_tab, text="Please refer to Load Winner/Checkpoints E2 lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)

def Activate_Content(education_option_selected, educatuin_tab, hidden_level_text):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab, hidden_level_text)

    education_option_selected.bind('<<ListboxSelect>>', load_content)
def DarkMode():
    for education_label in education_mode_labels:
        try:
            exec(education_label + '.config(bg = "grey75")')
        except:
            pass