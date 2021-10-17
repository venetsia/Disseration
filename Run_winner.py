import heapq
import sys
from operator import attrgetter
from tkinter import END

import neat
import pickle
import numpy as np
import os
import cv2
import gym
import pyglet
import NEAT_Single_Processing
from TextRedirector import TextRedirector

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
game_list_atari = ['SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0","Breakout-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0", "KungFuMaster-vo"]
game_list_2D = ["BipedalWalker-v2", "LunarLander-v2", "CartPole-v1"]

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

def replay_genome_2DBox(genome, config,number_left):
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    fitnesses = []

    for ep in range(int(GENERATION_EP)):
        # env = gym.make("LunarLander-v2")
        env = gym.make(env_variable)
        observation = env.reset()

        fitness = 0.0
        done = False

        while not done:
            # model Prediction
            env.render()
            action = np.argmax(net.activate(observation))
            observation, reward, done, info = env.step(action)
            fitness += reward
        env.close()
        if fitness == None:
            fitness = 0
        if number_left == 0:
            try:
                genome.fitness = "Exit"
                return
            except TypeError:
                print("END")
        fitnesses.append(fitness)

    return np.mean(fitnesses)


def replay_genomes_2DBox(genomes, config):
    number_left = len(genomes)
    for genome_id, genome in genomes:
        # for runs in range(runs_per_net):
        number_left = number_left - 1
        genome.fitness = replay_genome_2DBox(genome, config, number_left)
    try:
        if genome.fitness is None:
            genome.fitness == 0
        else:
            return genome.fitness
    except TypeError:
        try:
            return int(genome.fitness)
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

    if env_variable in game_list_atari:
        replay_winner(genome,config)
    elif env_variable in game_list_2D:
        if network == "Recurrent":
            net = neat.nn.RecurrentNetwork.create(genome, config)
        elif network == "Feed-forward":
            net = neat.nn.FeedForwardNetwork.create(genome, config)
        for ep in range(int(GENERATION_EP)):
            env = gym.make(env_variable)
            observation = env.reset()
            high_score = 0
            done = False
            while not done:
                env.render()
                action = np.argmax(net.activate(observation))
                # action = eval_network(net, observation)
                observation, reward, done, info = env.step(action)
                high_score += reward
                if high_score == None:
                    high_score = 0
                genome.fitness = high_score

            env.close()
            fitness = high_score
            print('Genome: ', genome, ' Fitness: ', fitness)
    return

def replay_checkpoint(config_path,checkpoint_directory):
    config_path = NEAT_Single_Processing.raw(config_path)
    global config_path_global
    config_path_global = config_path
    #checkpoint_directory = NEAT_Single_Processing.raw(checkpoint_directory)
    global config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    print(checkpoint_directory)

    #Call game with only the loaded genome
    global pop
    pop = neat.Checkpointer.restore_checkpoint(checkpoint_directory)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.StdOutReporter(True))
    #print(pop.best_unique_genomes(5))
    # Convert loaded genome into required data structure
    if env_variable in game_list_atari:
        winner = pop.run(replay_function)
    elif env_variable in game_list_2D:
        winner = pop.run(replay_genomes_2DBox)
    return
def pre_process_data(Output_Console_winner,game_selection_winner,winner_file_name_winner, game_checkpoint_winner, checkpoint_directory_value_winner, network_type_winner, directory_value_winner):
    try:
        global env_variable
        global network
        env_variable = game_selection_winner.get()
        network = network_type_winner.get()
        # Set Text Widget to be Output
        sys.stdout = TextRedirector(Output_Console_winner, "stdout")
        directory_temp = ""
        global GENERATION_EP
        GENERATION_EP = game_checkpoint_winner.get()
        checkpoint_directories = checkpoint_directory_value_winner.get("1.0", END)
        directory_check = checkpoint_directories.split("~")
        directory_value_winner_string =  directory_value_winner.get("1.0", END)
        try:
            directory_check.remove("")
        except:
            pass
        try:
            directory_check.remove("\n")
        except:
            pass


        if len(directory_check) > 1:
            print("Loading checkpoints")
            for directory_checkpoint_winner_processed in directory_check:
                directory_temp = directory_checkpoint_winner_processed.replace("\\", "/")
                print("Checkpoint: " + directory_temp)
                replay_checkpoint(directory_value_winner_string, NEAT_Single_Processing.raw(directory_temp))
        elif len(directory_check) == 1:
            print("Loading checkpoint")
            directory_temp = directory_check[0].replace("\\", "/")
            print("Checkpoint: " + directory_temp)
            replay_checkpoint(directory_value_winner_string, NEAT_Single_Processing.raw(directory_temp))
        print("Loading winner")

        replay_genome(directory_value_winner_string, winner_file_name_winner)
        pyglet.app.exit()
    except Exception as e:  # work on python 3.x
        # Empty console that will use for print
        Output_Console_winner.delete('1.0', END)
        Output_Console_winner.insert(END, "Error message: " + str(e))
    return