import queue
import threading
import time
from PIL import ImageTk
import multiprocessing


exitFlag = 0
image1 = ""
image2 = ""
image3 = ""
neuron_tab_pic = ""
perceptron_image = ""
neuron_tab_pic_1 = ""
learning_types = ""
image_agent = ""
learning_how = ""
how_learn_nn = ""
reinforcement_Learning_1 = ""
reinforcement_Learning_2 = ""
reinforcement_Learning_3 = ""
feedforward_vs_recurrent_pic = ""
neuro_neat = ""
neat_running_explanation = ""
neat_results_from_generation = ""
neat_found_winner = ""
filelist = ["AI-Intro.png", "AI_second.png","AI_Seond_Pic.png", "biological_neuron.png", "percepron.png",
            "Types_of_learning.png", "Components_of_Neural_Network.png", "agent.png",
            "How_does_the_neural_network_learn.png", "ReinforcementLearningImage1.png",
            "ReinforcementLearningImage2.png", "ReinforcementLearningImage3.png","feed-forwardVSrecurrent.PNG", "Neuro_NEAT.png", "NeatRunningExplanation.PNG",
            "Neat_Results_From_Generation.PNG", "Neat_Found_winner.PNG"]
threadList = ["Thread-1", "Thread-2", "Thread-3"]
queueLock = threading.Lock()
workQueue = queue.Queue(18)
threads = []
threadID = 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        process_data(self.name, self.q)


def process_data(threadName, q):
    global image1
    global image2
    global image3
    global neuron_tab_pic
    global perceptron_image
    global learning_types
    global neuron_tab_pic_1
    global image_agent
    global how_learn_nn
    global reinforcement_Learning_1
    global reinforcement_Learning_2
    global reinforcement_Learning_3
    global feedforward_vs_recurrent_pic
    global neuro_neat
    global neat_running_explanation
    global neat_results_from_generation
    global neat_found_winner

    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            if data == "AI-Intro.png":
                image1 = ImageTk.PhotoImage(file="AI-Intro.png")
            elif data == "AI_second.png":
                image2 = ImageTk.PhotoImage(file="AI_second.png")
            elif data == "biological_neuron.png":
                neuron_tab_pic = ImageTk.PhotoImage(file="biological_neuron.png")
            elif data == "percepron.png":
                perceptron_image = ImageTk.PhotoImage(file="percepron.png")
            elif data == "Types_of_learning.png":
                learning_types = ImageTk.PhotoImage(file="Types_of_learning.png")
            elif data == "Components_of_Neural_Network.png":
                neuron_tab_pic_1 = ImageTk.PhotoImage(file="Components_of_Neural_Network.png")
            elif data == "agent.png":
                image_agent = ImageTk.PhotoImage(file="agent.png")
            elif data == "How_does_the_neural_network_learn.png":
                how_learn_nn = ImageTk.PhotoImage(file="How_does_the_neural_network_learn.png")
            elif data == "ReinforcementLearningImage1.png":
                reinforcement_Learning_1 = ImageTk.PhotoImage(file="ReinforcementLearningImage1.png")
            elif data == "ReinforcementLearningImage2.png":
                reinforcement_Learning_2 = ImageTk.PhotoImage(file="ReinforcementLearningImage2.png")
            elif data == "AI_Seond_Pic.png":
                image3 = ImageTk.PhotoImage(file="AI_Seond_Pic.png")
            elif data == "ReinforcementLearningImage3.png":
                reinforcement_Learning_3 = ImageTk.PhotoImage(file="ReinforcementLearningImage3.png")
            elif data == "feed-forwardVSrecurrent.PNG":
                feedforward_vs_recurrent_pic = ImageTk.PhotoImage(file="feed-forwardVSrecurrent.PNG")
            elif data == "Neuro_NEAT.png":
                neuro_neat = ImageTk.PhotoImage(file="Neuro_NEAT.png")
            elif data == "NeatRunningExplanation.PNG":
                neat_running_explanation = ImageTk.PhotoImage(file="NeatRunningExplanation.PNG")
            elif data == "Neat_Results_From_Generation.PNG":
                 neat_results_from_generation = ImageTk.PhotoImage(file="Neat_Results_From_Generation.PNG")
            elif data == "Neat_Found_winner.PNG":
                neat_found_winner = ImageTk.PhotoImage(file="Neat_Found_winner.PNG")
        else:
            queueLock.release()
        time.sleep(1)



def process_file():
    # Create new threads
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)

    #Fill the queue
    queueLock.acquire()
    for word in filelist:
        workQueue.put(word)
    queueLock.release()
