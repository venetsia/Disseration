import neat
import pickle
import numpy as np
import os
import cv2
import gym

env_variable =""
network = ""


def run_winner():
    # Load configuration.
    #local_dir = os.path.dirname(__file__)
    #config_path = os.path.join(local_dir, 'configfeedforwardFishing.txt')
    #config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
     #                           neat.DefaultSpeciesSet, neat.DefaultStagnation,
     #                           config_path)

    env = gym.make(env_variable)

    imgarray = []

    xpos_end = 0

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'configfeedforwardFishing.txt')

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    with open('winner7', 'rb') as input_file :
        genome = pickle.load(input_file)

    ob = env.reset()
    ac = env.action_space.sample()

    inx, iny, inc = env.observation_space.shape

    inx = int(inx / 3)
    iny = int(iny / 3)

    if network == "Recurrent":
        net = neat.nn.RecurrentNetwork.create(genome, config)
    elif network == "Feed-forward":
        net = neat.nn.FeedForwardNetwork.create(genome, config)

    #net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)

    current_max_fitness = 0
    fitness_current = 0
    frame = 0
    counter = 0
    xpos = 0
    xpos_max = 0

    done = False

    while not done :

        env.render()
        frame += 1

        ob = cv2.resize(ob, (inx, iny))
        ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
        ob = np.reshape(ob, (inx, iny))
        h_ob, w_ob = ob.shape  # 184,127
        # Sizing it down for faster network decision making, big input takes more time to evaluate
        inx = int(h_ob / 3)
        iny = int(w_ob / 3)
        ob = cv2.resize(ob, (iny, inx))
        ob = np.reshape(ob, (inx, iny))
        imgarray = np.ndarray.flatten(ob)

        ai_decision = net.activate(imgarray)
        action = np.argmax(ai_decision)

        ob, rew, done, info = env.step(action)

        if done:
            done = True

def pre_process_data(game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner):
    global env_variable
    global network
    env_variable = game_selection_winner.get()
    network = network_type_winner.get()

    checkpoints_created = game_checkpoint_winner.get()
    print("Loading checkpoints")
    checkpoint_directories = checkpoint_directory_value_winner.get("1.0", END)
    directory_check = checkpoint_directories.split()
