# Tested on:

- Widnows 10
Processor: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz   2.81 GHz
Installed RAM: 16.0 GB (15.9 GB usable)
System type: 64-bit operating system, x64-based processor
Windows Edition: Windows 10 Home
Version: 21H1
OS Build: 19043.1288

- Windows 11
Processor: Intel(R) Core(TM) i7-8750H CPU @ 2.20 GHz 2.21 GHz
Installed RAM: 16.0 GB (15.9 GB usable)
System type: 64-bit operating system, x64-based processor
Windows Edition: Windows 11 Home
Version: 21H2
OS Build: 22000.258

**Display Resolution: 1920 x 1080**

**Not Tested on: Linux, MAC OS, any other Windops OS**

# How to run the program
## Pre-requirements
###  - Have Python 3.7.0 installed 
#### in order to run the program you will need Python 3.7.0 from official website - https://www.python.org/downloads/release/python-370/
##### If you scroll down you will see the files (install the one according to your machine)

![image](https://user-images.githubusercontent.com/15977217/140250964-195d6337-d05f-4075-8254-c1859a348fd3.png)

###  - Have PyCharm instaled from https://www.jetbrains.com/pycharm/ (it is free to use) - program is not limited to only this IDE  

### - Install Visual Studio and install C++ dependencies (otherwise Atari games would not load)

Following guidence on https://github.com/openai/gym/issues/1726

You need to:
1. Download VS build tools here: https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16
2. C++ Builld tools via:
- Run the VS build setup and select "C++ build tools" (or it can be under "Desktop Development with C++" in new versions of the VS Build Tool) and install it.

**If you cannot find Windows 10 SDK (10.18362.0) do not worry, just install the newest version there is for Windows 10, currently up to 04.11.2021 it is Windows 10 SDK(10.0.19041.0)**

![image](https://user-images.githubusercontent.com/15977217/140330921-f1b03bc0-c214-4401-8a83-85afbeeda8f2.png)

- Visual Studio 2019 - under Desktop Develipment with C++)

![image](https://user-images.githubusercontent.com/15977217/140331978-705ad222-b1d8-442b-95bf-2c4452d107ed.png)

![image](https://user-images.githubusercontent.com/15977217/140332544-2511c795-e6a6-412b-90a2-8b1fe2541893.png)

3. Restart PC
4. Only after the restart you should install the library requirements (atari_py (integrated in gym library) needs the C++ build tools otherwise it will not find the modules)
**If you try to run the program without the build tools it will run but the Atari games will not work as it will fail to find the modules**

## How to load in PyCharm via GIT
1a. Click on "Get From VCS"
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/VSC.png) 

OR

1b. Click on "Git" and then clone 

![image](https://user-images.githubusercontent.com/15977217/140252759-bee76b25-6e9e-4c34-a059-2cabb97cad33.png)

2.You should see the below screen: 

![image](https://user-images.githubusercontent.com/15977217/140252849-357b949d-9e18-4b09-bd52-21005c09e09f.png)


**Important if you do not have GIT it will say so under the "Directory" and you will have the option to install it - You should install GIT if you would like to "Clone" the program ** 

3. On the main page of the github project you should see the button "Clone"

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/clone.png) 

Click on "Clone" and then copy the link from HTTPS

4. Paste the link you have copied from github to Pycharm in the URL text field

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/paste.png)

**On "Directory" you are specifying where would you like to save the project on your computer (locally)**

5. Click "Clone" button

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/paste.png)

6. The following screen will open: (Click on Project)

![image](https://user-images.githubusercontent.com/15977217/140334975-9556439a-7cb3-4704-9a2a-9fcd5a7fae0f.png)

**On the bottom you will see that it is performing some checks so you should proceed after it is done (when you see:)**

![image](https://user-images.githubusercontent.com/15977217/140335150-6b952cc9-3070-4006-a871-9fea2b3ee8aa.png)

7. Expand the project:

![image](https://user-images.githubusercontent.com/15977217/140335275-d273d60a-98ba-46d8-86f1-eaa8b944c2cf.png)

8. We need to first choose an "Interpreter" (Python language)

- First time using PyCharm you will see:
 
![image](https://user-images.githubusercontent.com/15977217/140335771-aad85f58-7bc6-461c-9291-d63ebb561bea.png)

- Non first time user of PyCharm:

![image](https://user-images.githubusercontent.com/15977217/140335926-103b9cdb-c97e-4f75-8703-895ad4eddae6.png)

9. Click on File -> Settings:

![image](https://user-images.githubusercontent.com/15977217/140336105-88d2db1f-4f94-4e5a-905e-2fd0538ec523.png)

10. Click on "Project:<Directory you have chosen from step 4>" (In my case it would be NeatEditor following from that example, but due to more testing I have named the Directory DissertationTestint - So it would have whatever name you have chosen there for that specific load):

![image](https://user-images.githubusercontent.com/15977217/140336308-60e81c74-cf5e-4b44-a15c-7a270edd3046.png)

11. Click on Project Interpreter

![image](https://user-images.githubusercontent.com/15977217/140337232-f5e8eee3-54a6-4521-af98-f233fe9d1acf.png)

12. Click on the "COG" and Choose "Add"

**Depending on whether or not this is your first time using PyCharm the PythonInterpreter may be saying "No Interpreter" or something like mine - you can ignore this as we will add a new one**

![image](https://user-images.githubusercontent.com/15977217/140337703-ae6be931-2bf0-4fb7-ab8b-4a0c1ea29023.png)


![image](https://user-images.githubusercontent.com/15977217/140337644-3903444e-fd42-44fb-a408-d3aa9db555c1.png)

13. Choose "New Environment"

![image](https://user-images.githubusercontent.com/15977217/140338124-5faed25b-a37e-474e-a0e4-f1ec06098a65.png)

14. On "Location" change **venv** to **venv1** (for example) - this is where it will store the language you are using and all of the installed libraries

![image](https://user-images.githubusercontent.com/15977217/140338757-ef568fe7-321f-4746-8251-715997bafaa3.png)

**Why change it?**
When you hover over the text field it will let you know that it is not empty so after many tests it is easier to create a new Virtualenv Environment
![image](https://user-images.githubusercontent.com/15977217/140338646-4141c72e-b474-4cdd-8d7e-de132c510357.png)


15. Choose the Python 3.7.0 version by clicking on "..." and paste the path to your python.exe 

![image](https://user-images.githubusercontent.com/15977217/140343708-80c1b0d5-2dbb-4934-bb6a-3e4ad3907e43.png)

Outcome after  pasting path:
![image](https://user-images.githubusercontent.com/15977217/140344875-f97b25ca-18b2-4b9a-ad4f-1b0e28b533cf.png)

**How to find path to exe?**
15.1. Search for Python in Search Bar and click on "Open File Location"

![image](https://user-images.githubusercontent.com/15977217/140339033-170f8bcc-abb7-4160-b05f-597e98a81b39.png)

15.2. Right Click on Python 3.7 (64-bit) and select "Properties"

![image](https://user-images.githubusercontent.com/15977217/140339468-99460bb1-205c-446c-b237-bf09391664db.png)

15.3. Click on Target text filed (anywhere)

![image](https://user-images.githubusercontent.com/15977217/140339738-a44d225c-8d81-4607-b3a0-be6350a2151f.png)

15.4. On Keyboard press "Ctrl + A"/ right click and choose "Select all" to select the whole path and "Ctrl + C"/ or right click and select "Copy" to copy

![image](https://user-images.githubusercontent.com/15977217/140340381-558b1008-7006-4f37-8068-dbb4fdb33a63.png)

15.5. Paste in the text field

![image](https://user-images.githubusercontent.com/15977217/140346686-8366f6ca-8c69-4565-9d3e-09b9f313a71d.png)


**If you are having issues with this for some reason:**
- Click on "Open File Location" and copy the whole path (in my case it is: C:\Users\User\AppData\Local\Programs\Python\Python37)
 
![image](https://user-images.githubusercontent.com/15977217/140341945-4a3c1103-f280-4444-8cbb-ad8d1861360e.png)

- Paste in the path and add python.exe or choose the python.exe 

![image](https://user-images.githubusercontent.com/15977217/140347133-30722895-7ddf-4652-b107-d626f67f6ea2.png)

16. Press "OK"

![image](https://user-images.githubusercontent.com/15977217/140347960-417916aa-0e02-4937-b017-9387a4051141.png)

17. Wait for "Creating Virtual Environment" to finish

![image](https://user-images.githubusercontent.com/15977217/140348770-22070ed0-1bd3-447d-8110-74d74a9456c1.png)

18. Click on "OK"

![image](https://user-images.githubusercontent.com/15977217/140351116-4feaeb4f-9697-4c20-9f3a-915e6b2879f5.png)

19. Wait until you do not see anything loading on the bottom and you see: (**Loading may be: "Indexing", "Finding binaries", etc - you will see it on bottom right corner after "Creating Virtual Environment" dissappears)

![image](https://user-images.githubusercontent.com/15977217/140349730-92523fa6-eb9d-4c66-aa7c-1286db33be47.png)

20. Double click on "TextEditor.py"

![image](https://user-images.githubusercontent.com/15977217/140352070-42a113dc-8231-406b-a176-65949dcdc335.png)

21. Scroll to the top until you see:

![image](https://user-images.githubusercontent.com/15977217/140352902-481f2fa1-dc84-4088-9c79-0d42b8cf2f6d.png)


![image](https://user-images.githubusercontent.com/15977217/140352639-00e832e6-fd87-48f2-a91d-9e2e87a459ad.png)

21. Click on "Install Requirements":

![image](https://user-images.githubusercontent.com/15977217/140353269-4032a9cb-3ae4-4639-9255-d414632df3a0.png)

22. Click on "Install"

![image](https://user-images.githubusercontent.com/15977217/140354715-e03827f6-9a45-4166-ab00-0e5cb6f7d506.png)

**Important Notice**
For some reason it does not install opencv-python == 4.5.3.56 so after you no longer see "Installing package <name == version>: (if you did see it within the checked parameters you can skip 23)

![image](https://user-images.githubusercontent.com/15977217/140356170-ad87f086-fb45-420e-b24b-4de54ed747b3.png)

23. Check if  opencv-python == 4.5.3.56 is installed

![image](https://user-images.githubusercontent.com/15977217/140356170-ad87f086-fb45-420e-b24b-4de54ed747b3.png)

After you see:

![image](https://user-images.githubusercontent.com/15977217/140364372-96c9a8ca-2106-4aa5-b4f8-0744ccfe5386.png)

Go to "File -> Settings"

![image](https://user-images.githubusercontent.com/15977217/140364867-872b8f5f-111c-4257-b1dd-27fd2a320701.png)

Click on "+"

![image](https://user-images.githubusercontent.com/15977217/140365482-7a779384-b3c3-447d-8ba7-ef5f6551e0a9.png)

Type: opencv-python, and tick the "Specify version" and choose from the dropdown 4.5.3.56 and click "Install Package"

![image](https://user-images.githubusercontent.com/15977217/140366142-686dba4c-6267-4919-b595-a491a781809a.png)

Close the "Available Packages" window (click on "x")

![image](https://user-images.githubusercontent.com/15977217/140367803-a8c1d426-72f0-42fd-9ca4-96badfa57303.png)

Close the "Settings" window by clicking "OK"

![image](https://user-images.githubusercontent.com/15977217/140368600-40e2d12f-9811-4f60-b48f-f61d1e3c8f8d.png)


You should see shortly 

![image](https://user-images.githubusercontent.com/15977217/140367127-51e70c2a-d7e0-41e7-a98d-07abdff743ea.png)

24. Right Click on TextEditor.py and select "Run TextEditor"

![image](https://user-images.githubusercontent.com/15977217/140369592-e3a69d9d-85da-4185-a4fa-7648a75728dc.png)

# NEAT 
## [NEAT] section
- `fitness_criterion` - this function determinesthe termination criterion from the genome fitness. 
   - max - For example if you choose max it will terminate whenver a single genome reaches the `fitness_threshold` you have set up - Terminate when "Best fitness:" reaches `fitness_threshold`
   - mean - If you set it up to mean it will terminate when the whole population reaches an avarage of the fitness threshold (shown in NEAT training output) - Terminate (find winner) when "Population's average fitness" reaches `fitness_threshold`
   ![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/NEAT_output.PNG)
- `fitness_threshold` - determine what fitness does the population/genome has to reach in order to find winner (terminate)
- `no_fitness_termination` - if set to `True` you can choose for how many generations to run the algorithm for.
- `pop_size` - how many genomes per generation you have in the beginning
- `reset_on_extinction` 
   -  on choosing`False` - Because the training may not find a solution it will terminate when all of the genomes are removed from the population (Total extinctions)
   -  on choosing  `True` - If total extinction is reached by from the training, the training will restart from scratch with same configuration file and other settings.
## [DefaultStagnation] section
- `species_fitness_func` - how to calculate the species fitness
- `max_stagnation` - the number training you will see that the species/genomes age so after this N number if it has not shown improvement it will be removed from the generation
- `species_elitism` - how many species are protected from removal (prevent total extinctions) 
## [DefaultReproduction] section
- `elitism` - how many most fit individuals to be preserved from one generation to another
- `survival_threshold` - fraction of the species that are allowed to reproduce in each generation
- `min_species_size` - minimal number of genomes per species after reproduction

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

## NEAT Editor 

(**If text fields in form are empty and you Config File has some value - clicking on "Update Config" will not remove your value**)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Neat_normal_mode.PNG)

In the Editor you would be able to open or create a new config file using the software. 

Using the buttons below you will be able to either open an existing file, configure a new one clean or with default values and edit them and then save changes.

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/ButtonsforEditor.PNG)

The form you can see on the left includes all the values of NEAT Config file that can be added onto the Config form. 

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/NeATEDITORCONFIGFORM.PNG)

Via this form you will be able to insert the value you wish to add into the config file. It is easy to use because when you move your cursor mouse on the parameter you can see what it actually is and decide what value you want. (**See NEAT Config for more information**)

### Open an existing config file

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/OpenBTN.PNG)

When you click this button you will be able to open an existing config file and you can edit whichever values you want in the form.

**When you open an existing file it will group the parametrs in groups if they are not - for example parameters that have to be under `[NEAT]`, `[DefaultStagination]`, `# Activation Options`, `# Network parameters`, etc. - so it is easier for you to find them and for the software to know where to insert the value if it is missing from form**

### Config Layout

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/ConfigLayoutBTN.PNG) 

Using this button you will get a clean (empty) NEAT Config file - the parameters without the values and you can use the form to include add values to any of the parameters you want.

The text you will get is:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/ConfigLayoutText.PNG)

**Notice that there is some text in "[]" or starting with # - the software uses these to recognise where the parameters need to go as they are grouped together for an easy to use and understand interface.**

### Default Config

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/DefaultConfigBTN.PNG) 

1. Using this button you will get the NEAT Config text with default values (if the parameter has a default value).
The default values for the parameters have been taken from the official Python NEAT guidence page - **https://neat-python.readthedocs.io/en/latest/config_file.html**

Example:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/DefaultConfigText.PNG)

### Update Config

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/UpdateConfigBTN.PNG) 

When you input the values you would like for the parameters you can click "Update Config" and it will insert these values for the parameters.

#### Example before clicking the button with no text in form: (**If text fields in form are empty and you Config File has some value - clicking on "Update Config" will not remove your value**)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/BeforeClickingUpdateConfigButton.PNG)

#### Example before clicking button with text in form:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/BeforeClickingUpdateConfigButtonWithValue.PNG)

#### Example after clicking button with text in form:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/AfterClickingUpdateConfigButton.PNG)

2. Insert parameter into Config file if it is missing from Config file and you have added a value in form **(one with value, one without)**

#### Example before clicking Update Config with missing parameters (one with value, one without)

**It will add the parameter only if the parameter has a value within form**

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/MissingValuesBeforeClickingUpdateConfig.PNG)

#### Example after clicking Update Config with missing parameters (one with value, one without)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/MissingValuesAfterClickingUpdateConfig.PNG)

3. Insert parameter into Config file if it is missing from Config file and you have added a value in form **(both with value)**

####  Example before clicking Update Config with missing parameters (both with value)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/MissingValuesBeforeClickingUpdateConfigBothWithValues.PNG)

####  Example after clicking Update Config with missing parameters (both with value)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/MissingValuesAfterClickingUpdateConfigBothWithValues.PNG)

### Save As

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/SaveASBTN.PNG)

Once you have done the changes you want for the Config file you can easily save the file with the button "Save As" in a directory of your choice.

## NEAT Config 
![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Neat_normal_mode.PNG)

(**If text fields in form are empty and you Config File has some value - clicking on "Update Config" will not remove your value**)

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

More information on what these are:

![alt text](https://github.com/venetsia/Disseration/blob/master/feed-forwardVSrecurrent.PNG)

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

#### Log file - keep track of what settings you have chosen when you train a neural network
Later on when you would like to view your winner and checkpoints you may not remember what you have chosen. That is why the software creates a logfile and inserts whatever you run into it so you can recall later on.

**If you do not remember a logfile has been generated for you so you can see what you have run**

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/logfile.PNG)

You can easily see what you have run with what names and where the config file is located.

#### 12. Run Neat Example

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/RunNEATFOrmFilledOut_With_Render.PNG)

![a;t text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/RunNEATFOrmFilledOut_With_RenderExample.PNG)

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

#### 3. Number of ep. per genome:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Number_of_ep_per_genome.PNG)

With this option when you run to see the Winner genome and checkpoints it will run each genomes N number of times.
For example if you input 2 episodes per genome, the winner genome and genomes within checkpoints will run 2 times.

#### 4. Checkpoint(s) Directory 

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Checkpoints_Winner.PNG)

This option is not mandatory as you can only Load the winner genome so if you wish to not see any checkpoints you can skip it.

Process on getting the checkpoints:
1. Click on Browse Folder and you should see:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Checkpoints_Directory_Locator.PNG)

* Eventhoug you do not see anything in the directory, if you have saved them in the folder when you click "Select Folder" it will search for any files named: `neat-checkpoint-` and it will show:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Checkpoints_Directory_Selected.PNG) 

You can delete any of the checkpoints you do not want to see (**You have to delete the whole line starting with `~`. Example in my case if I do not want to see neat-checkpoint-0 I simply have to delete:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/neat-Checkpoint-0-directory.PNG)

So you will simply get this after deleting the line:

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/neat-Checkpoint-0-directory-Deleted.PNG)

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/deleted-neat-checkpoint-0.PNG)

2. Num of Checkpoints (**hidden feature only enabled if you would like to view checkpoints**)
Because the checkpoints are originally used to restore the training from a certain generation, a modification has been made so you can choose to view N number of genomes in that generation and not view the whole generation (for example if you started with 100 population on generation 0, running generation 0 would run 100 genomes per N episoder). 
Modification includes ommitting the genomes with fitness of None and when you select N number of genomes in checkpoint it will get the N number of genomes with the highest fitness in that generation (checkpoint).

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Num_genomes_in_checkpoint.PNG)

#### 5. Num of Checkpoints (**hidden feature only enabled if you would like to view checkpoints**)
Because the checkpoints are originally used to restore the training from a certain generation, a modification has been made so you can choose to view N number of genomes in that generation and not view the whole generation (for example if you started with 100 population on generation 0, running generation 0 would run 100 genomes per N episoder). 
Modification includes ommitting the genomes with fitness of None and when you select N number of genomes in checkpoint it will get the N number of genomes with the highest fitness in that generation (checkpoint).

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Num_genomes_in_checkpoint.PNG)

#### 6. Network Type

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/network_type_winner.PNG)

You have two options here:
* Feedforward network
* Recurrent network

More information on what these are:

![alt text](https://github.com/venetsia/Disseration/blob/master/feed-forwardVSrecurrent.PNG)

You would need to choose the same network you have trained it on. 

**If you do not remember a logfile has been generated for you so you can see what you have run**

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/logfile.PNG)

You can easily see what you have run with what names  and where the config file is located.

#### 7. Config File

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Config_File_Winner.PNG)

Options:
* Automatic - if you have just run or filled out NEAT Set up to train your neural network it will automatically copy those details here
* From Text Editor - this will enable you to save the current config you have edit (**but bear in mind that results can be inpredictable if you run with different config file for loading the genomes)
* Choose file from directory - choose a Config file from directory

Once filled out you will see the directory you have chosen in the "Directory" text field (non-editable):

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/Config_File_WinnerFilled.PNG)

#### 8. Load Genomes and Winner

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/LoadGenomesAndWinner.PNG)

Once you have filled out the form you can click the button and it will load the checkpoints and winner

**You will see a rendered window of the game**

1. You will see the which checkpoint is being shown and when are you viewing the winner from: "## Load checkpoints/ winner ##"

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/LoadCheckpoints%20and%20WinnerTextField.PNG)

2. Example of a filled out form

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/ExampleFilledoutFormForLoadWinner.PNG)

3. Example when "Load Genomes and winner" button is clicked

![alt text](https://github.com/venetsia/Disseration/blob/master/ReadMePictures/LoadWinnerExample.png)

**You can load the example as well: all files are in folder CartPoleExample**

## Dark Mode/ Ligh Mode

If you would to use Dark mode of the application you can click on:

![alt text](https://github.com/venetsia/Disseration/blob/master/off.png)

In order to switch back to light mode click on:

![alt text](https://github.com/venetsia/Disseration/blob/master/on.png)

## Normal Mode/ Education Mode

If you would like to use Educatio mode click on:

![alt text](https://github.com/venetsia/Disseration/blob/master/education_mode_icon.png)

If you would like to switch to Normal Mode click on:

!alt text](https://github.com/venetsia/Disseration/blob/master/normal_mode_pic.png)
