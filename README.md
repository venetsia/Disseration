# NEAT Editor
## Introduction
Welcome to the READ me file for the NEAT Editor software. Here you will get an overview of the application and how to use it and what tasks can you perform with it.

### First Load of application
When you first load the application the first thing you will see is:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/options-FirstLoad.PNG)

Upon clicking:
* YES - Education Mode will load
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/EducationMode-Launch.PNG)

* No - Normal mode of editor will load with all of the content

##### Beware that when you start the program the contents of the lectures are loading on seperate threads so it may be a bit slow in the beginning but after the content is loaded you should have no issues browsing though the tabs and lessons.
### Normal mode
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Neat_normal_mode.PNG)

Upon loading the normal mode you will see the screen above.
You can see here that Education tab is disabled:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Normal_Mode_tabs.PNG)

so if you would like to use the Education Mode you would have to switch to Education Mode by clicking:

![alt text](https://github.com/venetsia/Disseration/blob/master/education_mode_icon.png)

### Education Mode
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/EducationMode-Launch.PNG)
In the education mode you will be able to learn more about Artificial Intelligence and the different Learning methods. 
NEAT is a reinforcement learning algorithm and to understand how to use NEAT you may benefit from knowing some basic information.

#### Education TAB 
In Education tab you will be able to load the lessons that are created to specifically guide you to understand some basic concepts in Artificial Intelligence and show you a few examples on how can you use
the applicaiton to run NEAT, edit NEAT config file and load winner after training has completed.

##### Education Options list
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Education_Options_list.PNG)

Here once you select a lesson (option) the content will only load in Education Tab so make sure if you would like to view the contents you select the Education tab. You are still free to browse though the other tabs while content is loaded.

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Application_tabs.PNG)

##### NEAT Examples in Education Mode
There are a few options in Education List that you can choose but they have to be loaded sequentually for now.
So for example if you would like to run one of the optons circled in red you need to start from NEAT Config File, follow though the buttons and it would automatically guide you though the last example in the sequential list:

(in order to re-run them you would need to re-launch the application)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/NEAT_Examples_Education.png)

## NEAT Config 
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Neat_normal_mode.PNG)

In this tab you will have the freedom to edit the configuration file of NEAT. 
For more details of the NEAT Config file you can see the oficial guidence: https://neat-python.readthedocs.io/en/latest/config_file.html
The application implements each of the descriptions of the NEAT Config parameters as Message Helpers that will appear when your mouse cursor enters either the label or the text box.
Here is an example: 
When your mouse cursor enter or selects the text box it will show a Message Helper that explains what is the parameter.
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Message_Helper_NEAT_Config.PNG)

You may see that the label is read and that is because upon selecting the text box I did not enter (choose any of the values in the dropbox) so when I moved on it colored the label. This is because some of the parameters do not have default values so it is up to the user to choose whatever he/she wants.
Here is an example of some values that have default values (taken from the NEAT Config official guidence page) and some that do not:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Example_Of_Default_Values_for_Parameters.PNG)

You can clearly see that some are marked as red but some are filled out. I have only moved my focus on the text boxes so if there is a default value for the parameter it will be automatically added and if there isn't the label will be colored as red. Once you fill out the box the label will return to its normal color given it is a valid choice.

### Neat Section 
#### 1. An extra note regarding NEAT Section for "No Termination? (no_fitness_termination)":

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/No_fitness_termination.PNG) 

This is an important feature as some training on games can take a while and even never find a solution even so it will run either to Exctinction or until it reaches the threshold.

By default the value is set to be False. If the value is set to true it means that you will have to provide how many generations you want your training to be (etc. train for 10; train for 20; train for 30...). This means that the nerual network will try to learn how to play the game over N number of generations. You will see this in use in the RUN Neat section where if you choose a NEAT Config file, the software will scan the application and check whether this option is enabled or not and if yes it will display:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/no_fitness_termination_example.PNG)

Here I have preloaded the file in the Editor window so you can clearly see that "no_fitness_termination = True" so when we choose the config file in Run Neat it has made another option visible where we can choose after how many generations to terminate the training. 
##### This option "Terminate after num of generations" will not appear if "no_fitness_termination = False"
##### If "Terminate after num of generations" is left blank and we have 'no_fitness_termination = True" the software will set "Terminate after num of generations: 1" so it will terminate the algorithm after 1 generation.

#### 2. An extra note regarding NEAT Section for Gym Game, Number of input nodes and Number of output nodes
##### NEAT Config
As you may already know, every learning algorithm needs input nodes. For reinforcement learning the algorithm needs to know:
* how many inputs there are (how many observations the agent can get)
* how many outputs there may be (how many actions can the agent perform)

Because we are using an external library (Open AI Gym Environments - https://gym.openai.com/) these parameters are pre-defined in the environment. 
* Input - the input is the observations the agent can make. For example think of each thing you percieve (see/smell/touch) with your eyes/nose/arms/etc an observation that is an input to your brain.
* Output - If we were creating a game for example you will give it certain actions you can perform or for example if we were playing a game on a computer, mobile or console it will have for example the number of buttons (on Xbox controller for example we have Y, X, B, A - they are all mapped to a certain action in a game (maybe some buttons do not do anything on a specific game or there are more buttons (actions) that can be perfomed within a game.).

You can easily get the number of inputs and outputs for the game by selecting the a game in Gym Game dropbox. Once you select a game the inputs and outputs will be automatically set.

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Number_of_inputs_outputs_Neat_config.PNG)

##### Neat Setup

For making life easier for the user of this application if you insert a config file that you have not specifically modified for the game you would like to run it with. There is an option in RUN Neat tab where if selected it will modify the input and output parameter for you when you click Run Neat.
You just need to:
* Select the Game you want to run
* Choose the config file you would like to use
* Enable "Check config File for input/output
  *   You will see what values will be modified and with what in "Enter Command" text box
* Click "Run Neat" and the parameters "num_inputs and "num_outputs" values will be modified. 
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Input_Output_Neat_Setup.PNG)

#### 3. An extra note regarding NEAT Section Initial Connection
When choosing initial connection in the NEAT config tab there are two values that require more information on input. These values are: **partial_nodirect** and **partial_direct**. 
When they are selected "Initial Connection probability" text input will be enabled.
Example when it is not enabled:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/InitialConnection.PNG)

Example when it is enabled:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/InitialConnectionEnabled.PNG)

#### 4. An extra note regarding NEAT Section Random Selector
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/RandomSelector.PNG)

If this is set to True it will select random values for "Default Activation Function" and "Default Aggregation Function" when you move your cursor in the text field and out. Important to note that if these parameters are not specified NEAT will choose a random function for you so this option enables the user to actually see what the random function will be prior to running NEAT.
Example when it is enabled (equals True):

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/RandomSelectorEnabled.PNG)

### Neat Setup

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/NeatSetupFirstLoad.PNG)

In this tab the user is able to train a neural network to play a game chosen from the dropdown list. In order for the user to actually run Neat they need to provide a valid config file (important to have the correct inputs and outputs)

#### 1. Gym Game Selection
In the dropdown you will be able to see that there are a number of specified games. They have all been tested and they are all able to run and render the game. Some games from the Gym Environments (Open AI) do not work so not all games are supported.
##### An exatra feature for Gym Game Selection for inputs/outputs
In order to make it easier for the user to RUN Neat without having to modify manually the config file each time he/she wants to run the algorithm with the same config, an optiion "Check Config File for input/output" has been added. If a game is selected and option is enabled it will show what input and output is needed for the game and it will modify the Config file automatically when you hit "Run NEAT" button.
You just need to:
* Select the Game you want to run
* Choose the config file you would like to use
* Enable "Check config File for input/output
  *   You will see what values will be modified and with what in "Enter Command" text box
* Click "Run Neat" and the parameters "num_inputs and "num_outputs" values will be modified. 
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Input_Output_Neat_Setup.PNG)

#### An extra feature for Gym Game Selection for `game_list_2D = ["LunarLander-v2", "CartPole-v1"]`
##### Runs Per Network

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Runs_Per_Network.PNG)

Games this option is availble for (Atari games do not incldue this option):
`game_list_2D = ["LunarLander-v2", "CartPole-v1"]`

What is it?
This option provides the user the option to input how many tries the agent will have in a genome (the genome will try to learn how to play the game N (runs) times).

#### 2. Evaluate Genomes
The evaluation of the genomes can be Single Processing and MultiProcessing (enabled by the NEAT algorithm). The application for now only gives you the option to run Single-Processing (meaning the algorithm will train an agent one by one, where as if Multi-Processing is added afterwards the genomes will be evaulated dependiong on your harware so it may train 10 agents at once).
#### 3. Winner File Name
User has to choose a name for the winner because once the algorithm runs and finds a solution (the agent reaches a threshold) it will try to save that genome into a file (the winner file)

**Important Note - Files get overwritten so make sure you move Winner File and checkpoints to a different directory**

** When NEAT creates the checkpoints and winner file it saves them in the same directory where the content root is (where the application is being executed from) **but each time you run the algorithm if you specify the same name for the winner it will overwrite the file, the same goes with Neat Checkpoints as they are marked neat-checkpoint-[number], next time you run the same ammount of checkpoints (if reached) - they will be overwritten. So that is why you need to make sure you move the files you want to keep in a different directory so you can load them later.** . If you for example train a winner and go to the Load Winner Tab to load it immediately, the information will be copied over the tabs.**


#### 4. Save Checkpoint
This option enables the user to save a checkpoint every N generations. For example we choose "Save checkpoint: 5" - it will save a checkpoint every 5 generations so you can either start the training again from that certain generation or rewatch the generation saved later in "Load Winner" so you can see the difference in the performance of the agents N generations apart.

**Important Note - Files get overwritten so make sure you move Winner File and checkpoints to a different directory**

** When NEAT creates the checkpoints and winner file it saves them in the same directory where the content root is (where the application is being executed from)** but each time you run the algorithm if you specify the same name for the winner it will overwrite the file, the same goes with Neat Checkpoints as they are marked neat-checkpoint-[number], next time you run the same ammount of checkpoints (if reached) - they will be overwritten. So that is why you need to make sure you move the files you want to keep in a different directory so you can load them later.** . If you for example train a winner and go to the Load Winner Tab to load it immediately, the information will be copied over the tabs.**

#### 5. Network Type
You have two options here:
* Feedforward network
* Recurrent network

**Important Note** If Recurrent has been selected here and your Config file has feed_forward = True, the parameter from the config file will be ignored and the network will be recurrent.

If this "Feedforward?" is set to True:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/GenomeSelectionFeedForwardExample.PNG)

But We have chosen Recurrent Network in NEAT Setup the network will be Recurrent as it will ignore value in Config File.

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/NEAT_Setup_NetworkType.PNG)

#### 6. Render Game
You can choose to render the game while you are training the neural network. Bear in mind that a rendered window of the game selected will be generated on each genome being trained. So for example we have a population of 100, for the first generation the window will be rendered 100 times and then it can decrease or increase depending on how the genomes perform. 
If this is set to Default it will not render the window but you can still view what is going on in the text field on the bottoom where it says "## See the evolution of genomes while running NEAT ## (this will be availble with Render - True as well).

#### 7. Config File

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/DirectoryChoiceNeatSetup.PNG)

Here we have 3 options:
* From Text Editor - if you have edited or configured the configuration file from the Editor selecting this option will give you the chance to save the file and it will be chosen as Config Directory,
* Choose file from directory - with this option you can browse directories on your computer to choose the config file
* Restore from checkpoint - you can choose to restore a checkpoint. **Important** - This will restore the checkpoint that has been been for that generation so it will run with the same config parameters it was once run and no modifications in Neat Setup will affect it.

The config file ("**Restore from Checkpint**" is excluded - so it only applies for "From Text Editor" and "Choose file from directory") is scanned for no_fitness_termination = True and if found it will make "Terminate after num of generations:" visible
#### An extra note regarding NEAT Section for "No Termination? (no_fitness_termination)":

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/No_fitness_termination.PNG) 

This is an important feature as some training on games can take a while and even never find a solution even so it will run either to Exctinction or until it reaches the threshold.

By default the value is set to be False. If the value is set to true it means that you will have to provide how many generations you want your training to be (etc. train for 10; train for 20; train for 30...). This means that the nerual network will try to learn how to play the game over N number of generations. You will see this in use in the RUN Neat section where if you choose a NEAT Config file, the software will scan the application and check whether this option is enabled or not and if yes it will display:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/no_fitness_termination_example.PNG)

Here I have preloaded the file in the Editor window so you can clearly see that "no_fitness_termination = True" so when we choose the config file in Run Neat it has made another option visible where we can choose after how many generations to terminate the training. 
##### This option "Terminate after num of generations" will not appear if "no_fitness_termination = False"
##### If "Terminate after num of generations" is left blank and we have 'no_fitness_termination = True" the software will set "Terminate after num of generations: 1" so it will terminate the algorithm after 1 generation.

#### 8. Enter Command Field
This field is used so you can see the inputs and outputs for the game selected.

It can be done automatically with the "Check config file for input/output":
In order to make it easier for the user to RUN Neat without having to modify manually the config file each time he/she wants to run the algorithm with the same config, an optiion "Check Config File for input/output" has been added. If a game is selected and option is enabled it will show what input and output is needed for the game and it will modify the Config file automatically when you hit "Run NEAT" button.
You just need to:
* Select the Game you want to run
* Choose the config file you would like to use
* Enable "Check config File for input/output
  *   You will see what values will be modified and with what in "Enter Command" text box
* Click "Run Neat" and the parameters "num_inputs and "num_outputs" values will be modified. 
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Input_Output_Neat_Setup.PNG)

Or you can manually insert the command if you want:
Simply paste or input one of the below commands and pres enter
`print(env.action_space)`
`print(env.observation_space)`

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/EnterCommandNeatSetup.PNG)

#### 9. "See the evolution of genomes while running NEAT"

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/SeeNeatRunningDefault.PNG)

In this text field you will be able to see what is the progress on your training while still be able to use the software. 
Example when you start training your neural network (agents) to play the game:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/RunningNeatInTextFieldExample.PNG)

**Beware** the software might appear a bit slow but it is beacause it is running the NEAT algorithm (the whole training) on another thread (**running concurrently**) of your computer so when you for example scroll down in takes a second for the task switch to occur.
Example of Task Switching in concurrency:
Imagine your training is one of the bars, when you scroll down it, your operating system will handle the user input (I/O) and scroll down and continue with the training.

![image](https://user-images.githubusercontent.com/15977217/138787485-fd49e24a-238f-4c00-bbc9-1e7d75f83537.png)

#### 10. Runs Per Network

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Runs_Per_Network.PNG)

Games this option is availble for (Atari games do not incldue this option):
`game_list_2D = ["LunarLander-v2", "CartPole-v1"]`

What is it?
This option provides the user the option to input how many tries the agent will have in a genome (the genome will try to learn how to play the game N (runs) times).

#### 11. "Terminate after num of generations:"
The config file ("**Restore from Checkpint**" is excluded) is scanned for no_fitness_termination = True and if found it will make "Terminate after num of generations:" visible
##### An extra note regarding NEAT Section for "No Termination? (no_fitness_termination)":

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/No_fitness_termination.PNG) 

This is an important feature as some training on games can take a while and even never find a solution even so it will run either to Exctinction or until it reaches the threshold.

By default the value is set to be False. If the value is set to true it means that you will have to provide how many generations you want your training to be (etc. train for 10; train for 20; train for 30...). This means that the nerual network will try to learn how to play the game over N number of generations. You will see this in use in the RUN Neat section where if you choose a NEAT Config file, the software will scan the application and check whether this option is enabled or not and if yes it will display:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/no_fitness_termination_example.PNG)

Here I have preloaded the file in the Editor window so you can clearly see that "no_fitness_termination = True" so when we choose the config file in Run Neat it has made another option visible where we can choose after how many generations to terminate the training. 
##### This option "Terminate after num of generations" will not appear if "no_fitness_termination = False"
##### If "Terminate after num of generations" is left blank and we have 'no_fitness_termination = True" the software will set "Terminate after num of generations: 1" so it will terminate the algorithm after 1 generation.

### Load Winner


![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/RunWinnerDefault.PNG)

**Important Note**

Beware that in oredr to run Winner you will need to specify the same things you have when you have trained the neural network.
Why?
Imagine you train your neural network to play Space Invaders and it is trained with the actions and observations of that game and you try to load the winner genome (that has the actions and observations of Space Invaders) with another game. It will not know what to do because it has not been trained to play the different game.


#### 1. Gym Game
In the dropdown you will be able to see that there are a number of specified games. They have all been tested and they are all able to run and render the game. Some games from the Gym Environments (Open AI) do not work so not all games are supported.

#### 2. Winner File Name

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/WinnerFile_LoadWinner.PNG)

You can specify winner file name either:
* Enter the winnner file name that you would like to run (given it is in the same directory where it was saved)
* Click on "Select File" button and you will be able to select the file located in a different folder.

**Important Note - Files get overwritten so make sure you move Winner File and checkpoints to a different directory**

Why would I need to use "Select File"? - When NEAT creates the checkpoints and winner file it saves them in the same directory where the content root is (where the application is being executed from) **but each time you run the algorithm if you specify the same name for the winner it will overwrite the file, the same goes with Neat Checkpoints as they are marked neat-checkpoint-[number], next time you run the same ammount of checkpoints (if reached) - they will be overwritten. So that is why you need to make sure you move the files you want to keep in a different directory so you can load them later.** . If you for example train a winner and go to the Load Winner Tab to load it immediately, the information will be copied over the tabs.


