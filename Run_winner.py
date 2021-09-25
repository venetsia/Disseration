from tkinter import END

import neat
import pickle
import numpy as np
import os
import cv2
import gym

import NEAT_Single_Processing

env_variable =""
network = ""
config = ""
pop =""

def replay_function(genome, config):
    env = gym.make(env_variable)
    imgarray = []

    xpos_end = 0


    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    ob = env.reset()
    ac = env.action_space.sample()

    inx, iny, inc = env.observation_space.shape

    inx = int(inx / 8)
    iny = int(iny / 8)

    if network == "Recurrent":
        net = neat.nn.RecurrentNetwork.create(genome, config)
    elif network == "Feed-forward":
        net = neat.nn.FeedForwardNetwork.create(genome, config)

    current_max_fitness = 0
    fitness_current = 0
    frame = 0
    counter = 0
    xpos = 0
    xpos_max = 0

    done = False

    while not done:

        env.render()
        frame += 1

        ob = cv2.resize(ob, (inx, iny))
        ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
        ob = np.reshape(ob, (inx, iny))

        for x in ob:
            for y in x:
                imgarray.append(y)

        nnOutput = net.activate(imgarray)

        ob, rew, done, info = env.step(nnOutput)
        imgarray.clear()

        xpos = info['x']
        xpos_end = info['screen_x_end']

        if xpos > xpos_max:
            fitness_current += 1
            xpos_max = xpos

        if fitness_current > current_max_fitness:
            current_max_fitness = fitness_current
            counter = 0
        else:
            counter += 1

        if done or counter == 250:
            done = True

def replay_genome(config_path, winner_file_name_winner ):
    config_path = NEAT_Single_Processing.raw(config_path)
    winner_file_name_winner = NEAT_Single_Processing.raw(winner_file_name_winner)
    # Load requried NEAT config
    global config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    global pop
    pop = neat.Population(config)
    # Unpickle saved winner
    with open(winner_file_name_winner, "rb") as f:
        genome = pickle.load(f)


    replay_function()

def replay_checkpoint(config_path,checkpoint_directory):
    config_path = NEAT_Single_Processing.raw(config_path)
    #checkpoint_directory = NEAT_Single_Processing.raw(checkpoint_directory)
    global config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    print("Inside replay")
    print(checkpoint_directory)



    #Call game with only the loaded genome
    global pop
    pop = neat.Checkpointer.restore_checkpoint(checkpoint_directory)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.StdOutReporter(True))

    pop.run(replay_function)


def pre_process_data(game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner):
    global env_variable
    global network
    env_variable = game_selection_winner.get()
    network = network_type_winner.get()

    directory_temp =""

    checkpoints_created = game_checkpoint_winner.get()
    print("Loading checkpoints")
    checkpoint_directories = checkpoint_directory_value_winner.get("1.0", END)
    directory_check = checkpoint_directories.split(",")
    directory_value_winner_string =  directory_value_winner.get("1.0", END)
    print(directory_value_winner_string)
    print("For loop")
    for directory_checkpoint_winner_processed in directory_check:
        directory_temp = directory_checkpoint_winner_processed.replace("\\", "/")
        print(directory_temp)
        replay_checkpoint(directory_value_winner_string, NEAT_Single_Processing.raw(directory_temp))

    replay_genome(directory_value_winner_string, winner_file_name_winner)
