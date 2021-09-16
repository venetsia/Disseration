import argparse
import os
import sys
import threading
from tkinter import END, INSERT
from pathlib import Path
import cv2
import gym
import numpy as np
import neat
import multiprocessing
import pickle
import os.path
from os import path
import tkinter as tk

from TextRedirector import TextRedirector

episodes = 1
starting_pixel = 114
self_y = 192
search_x_start = 22
search_x_end = 139
rock_color = 107
runs_per_net = 15

# Escape dict to be used for fixing string to raw
escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}


# Global Vairables to be used in eval_genomes and assigned from RUN_Program
env_variable =""
network = ""
render_window_variable =""

def eval_genomes(genomes, config) :
    for genome_id, genome in genomes :
        # for runs in range(runs_per_net):

        if network == "Recurrent":
            net = neat.nn.RecurrentNetwork.create(genome, config)
        elif network == "Feed-forward":
            net = neat.nn.FeedForwardNetwork.create(genome,config)
        env = gym.make(env_variable)
        #env = game_selection.get()
        observation = env.reset()
        frame = 0
        high_score = 0
        frame = 0
        my_pos_currrent = 0
        counter = 0
        discount = 0
        # Simulation starts
        while True :
            penalty = 0
            frame += 1
            counter += 1
            img = cv2.cvtColor(observation, cv2.COLOR_BGR2RGB)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if render_window_variable == "True":
                env.render()
            frame += 1
            # Processing observation image to get our set of inputs


            # Giving input as image
            ob = img[starting_pixel :self_y + 2, search_x_start - 5 :search_x_end + 5]
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
            if done :
                break
        env.close()
        fitness = high_score
        print('Genome: ', genome_id, ' Fitness: ', fitness)
        if fitness == None :
            fitness = 0
        # To immediately stop once it kills all enemies achieving its goal

        genome.fitness = fitness
    return
def eval_network(net, net_input):
    activation = net.activate(net_input)
    return np.argmax(activation)

def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    text = text.strip()
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    new_string = new_string.replace("\\n", "")
    new_string = new_string.replace("\n", "")

    return new_string

def run_Program(Output_Console,game_selection, winner_file_name, game_checkpoint, network_type,directory_value, render_window):
    # Load configuration.

    # Empty console that will use for print
    Output_Console.delete('1.0', END)

    # Set Text Widget to be Output
    sys.stdout = TextRedirector(Output_Console, "stdout")

    # Get path for config file
    config_path = directory_value.get("1.0",END)
    # Fix path string
    path_new = raw(config_path)

    # From NEAT integration that will be used for population
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                               neat.DefaultSpeciesSet, neat.DefaultStagnation,
                               path_new)

    # Get Population
    pop = neat.Population(config)
    # Enable statistic reported
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    # Print evolution of genomes
    pop.add_reporter(neat.StdOutReporter(True))

    # Make sure game_checkpoint does not execute if 0
    if int(game_checkpoint.get()) != 0:
        pop.add_reporter(neat.Checkpointer(int(game_checkpoint.get())))


    # assign global variables that will be used in evolving genomes
    global env_variable
    global network
    global render_window_variable
    env_variable = game_selection.get()
    network = network_type.get()
    render_window_variable = render_window.get()

    #pe = neat.ParallelEvaluator(multiprocessing.cpu_count(), eval_genomes)

    #winner = pop.run(pe.evaluate)

    # Get winner
    winner = pop.run(eval_genomes)

    # Get winner name that will be used and fix string
    winner_file_raw = raw(winner_file_name.get("1.0",END))
    # Save the winner.
    with open(winner_file_raw, 'wb') as f:
        pickle.dump(winner, f)

    print(winner)
    return

