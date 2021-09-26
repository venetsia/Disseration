from tkinter import END

import neat
import pickle
import numpy as np
import os
import cv2
import gym
import pyglet
import NEAT_Single_Processing

env_variable =""
network = ""
config = ""
pop =""
config_path_global = ""
population_size = ""

episodes = 1
starting_pixel = 114
self_y = 192
search_x_start = 22
search_x_end = 139
rock_color = 107
runs_per_net = 15

EP_STEP = 300           # maximum episode steps
GENERATION_EP = 1     # evaluate by the minimum of 10-episode rewards

def replay_winner(genome,config):
    #number_left = len(genomes)
        #print(number_left)
        # for runs in range(runs_per_net):
    if network == "Recurrent":
        net = neat.nn.RecurrentNetwork.create(genome, config)
    elif network == "Feed-forward":
        net = neat.nn.FeedForwardNetwork.create(genome, config)
    for ep in range(int(GENERATION_EP)):  # run many episodes for the genome in case it's
        env = gym.make(env_variable)
        # env = game_selection.get()
        observation = env.reset()
        frame = 0
        high_score = 0
        frame = 0
        my_pos_currrent = 0
        counter = 0
        discount = 0
        # Simulation starts
        while True:
            penalty = 0
            frame += 1
            counter += 1
            img = cv2.cvtColor(observation, cv2.COLOR_BGR2RGB)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            env.render()
            frame += 1
            # Processing observation image to get our set of inputs

            # Giving input as image
            ob = img[starting_pixel:self_y + 2, search_x_start - 5:search_x_end + 5]
            h_ob, w_ob = ob.shape  # 184,127
            # Sizing it down for faster network decision making, big input takes more time to evaluate
            inx = int(h_ob / 3)
            iny = int(w_ob / 3)
            ob = cv2.resize(ob, (iny, inx))
            ob = np.reshape(ob, (inx, iny))
            imgarray = np.ndarray.flatten(ob)

            ai_decision = net.activate(imgarray)
            action = np.argmax(ai_decision)
            observation, reward, done, info = env.step(action)
            # for the AI to learn how to dodge the bullet

            high_score += reward
            if high_score == None:
                high_score = 0
            genome.fitness = high_score
            if done:
                break

        env.close()
        fitness = high_score

        print('Genome: ', genome, ' Fitness: ', fitness)

    return
def replay_function(genomes, config):
    number_left = len(genomes)
    for genome_id, genome in genomes:
        print(number_left)
        # for runs in range(runs_per_net):
        number_left = number_left - 1

        if network == "Recurrent":
            net = neat.nn.RecurrentNetwork.create(genome, config)
        elif network == "Feed-forward":
            net = neat.nn.FeedForwardNetwork.create(genome, config)
        for ep in range(GENERATION_EP):  # run many episodes for the genome in case it's
            env = gym.make(env_variable)
            # env = game_selection.get()
            observation = env.reset()
            frame = 0
            high_score = 0
            frame = 0
            my_pos_currrent = 0
            counter = 0
            discount = 0
            # Simulation starts
            while True:
                penalty = 0
                frame += 1
                counter += 1
                img = cv2.cvtColor(observation, cv2.COLOR_BGR2RGB)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                env.render()
                frame += 1
                # Processing observation image to get our set of inputs

                # Giving input as image
                ob = img[starting_pixel:self_y + 2, search_x_start - 5:search_x_end + 5]
                h_ob, w_ob = ob.shape  # 184,127
                # Sizing it down for faster network decision making, big input takes more time to evaluate
                inx = int(h_ob / 3)
                iny = int(w_ob / 3)
                ob = cv2.resize(ob, (iny, inx))
                ob = np.reshape(ob, (inx, iny))
                imgarray = np.ndarray.flatten(ob)

                ai_decision = net.activate(imgarray)
                action = np.argmax(ai_decision)
                observation, reward, done, info = env.step(action)
                # for the AI to learn how to dodge the bullet

                high_score += reward
                if high_score == None:
                    high_score = 0
                genome.fitness = high_score
                if done:
                    break

            env.close()
            fitness = high_score

            print('Genome: ', genome_id, ' Fitness: ', fitness)

            if fitness == None:
                fitness = 0
            if number_left == 0:
                try:
                    genome.fitness = "Exit"
                    return
                except TypeError:
                    print("END")
    try:
        if fitness is None:
            fitness == 0
        else:
            return fitness
    except TypeError:
        try:
            return int(fitness)
        except:
            print("Error message")
def replay_genome(config_path, winner_file_name_winner ):
    config_path = NEAT_Single_Processing.raw(config_path)
    winner_name = NEAT_Single_Processing.raw(winner_file_name_winner.get("1.0", END))
    # Load requried NEAT config
    global config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    global pop
    pop = neat.Population(config)
    # Unpickle saved winner
    with open(winner_name, "rb") as f:
        genome = pickle.load(f)


    replay_winner(genome,config)
    return

def replay_checkpoint(config_path,checkpoint_directory):
    config_path = NEAT_Single_Processing.raw(config_path)
    global config_path_global
    config_path_global = config_path
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
    # Convert loaded genome into required data structure

    winner = pop.run(replay_function)
    return
def pre_process_data(game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner):
    global env_variable
    global network
    env_variable = game_selection_winner.get()
    network = network_type_winner.get()

    directory_temp = ""
    global GENERATION_EP
    GENERATION_EP = game_checkpoint_winner.get()
    print("Loading checkpoints")
    checkpoint_directories = checkpoint_directory_value_winner.get("1.0", END)
    print(checkpoint_directories)
    print("Here")
    directory_check = checkpoint_directories.split("\n")
    directory_value_winner_string =  directory_value_winner.get("1.0", END)
    print(directory_value_winner_string)
    print("For loop")
    print(directory_check)
    if len(directory_check) != 0:
        for directory_checkpoint_winner_processed in directory_check:
            directory_temp = directory_checkpoint_winner_processed.replace("\\", "/")
            print("Value: " + directory_temp)
            replay_checkpoint(directory_value_winner_string, NEAT_Single_Processing.raw(directory_temp))

    replay_genome(directory_value_winner_string, winner_file_name_winner)
    print("Exited")
    pyglet.app.exit()
    return