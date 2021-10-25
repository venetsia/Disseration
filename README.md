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

By default the value is set to be False. If the value is set to true it means that you will have to provide how many generations you want your training to be (etc. train for 10; train for 20; train for 30...). This means that the nerual network will try to learn how to play the game over N number of generations. You will see this in use in the RUN Neat section where if you choose a NEAT Config file, the software will scan the application and check whether this option is enabled or not and if yes it will display:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/no_fitness_termination_example.PNG)

Here I have preloaded the file in the Editor window so you can clearly see that "no_fitness_termination = True" so when we choose the config file in Run Neat it has made another option visible where we can choose after how many generations to terminate the training. 
##### This option "Terminate after num of generations" will not appear if "no_fitness_termination = False"

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


