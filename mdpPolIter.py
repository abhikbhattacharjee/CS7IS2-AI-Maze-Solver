#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 23:05:44 2023

@author: abhik_bhattacharjee
"""
from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
from mdpClass import mdpVI
import random

print("\n Enter maze size: \n")
ipx = input("\n X: ")
x = int(ipx)
ipy = input("\n Y: ")
y = int(ipy)
print("\n Enter Target: \n")
tx = input("\n X: ")
tarx = int(tx)
ty = input("\n Y: ")
tary = int(ty)

mazeDef = maze(x, y)
mazeDef.CreateMaze(tarx, tary, loopPercent = 100, theme = COLOR.light)

# mazeDef.CreateMaze(loadMaze='./Maze/maze100.csv')

target = [(tarx, tary)]

track, U, policy, actions, timediff = mdpVI().mazeTrack((x,y), tarx, tary, -40, 0.9, 10**(-3), mazeDef, stochastic = False)

U = {state: 0 for state in actions.keys()}
U[target[0]] = 10**(8)
policy = {s: random.choice('NSEW') for s in actions.keys()}

REWARD = {state: -40 for state in actions.keys()}
REWARD[target[0]] = 10**(8)
DISCOUNT = 0.9
theta = 0.001

is_policy_changed = True
iterations = 0

while is_policy_changed:
    is_policy_changed = False
    is_value_changed = True
    while is_value_changed:
        delta = 0
        is_value_changed = False
        for state in actions.keys():
            if state == target[0]:
                continue
            old_action = policy[state]
            max_utility = float("-infinity")
            max_action = None
            for action, prob in actions[state].items():
                for direction in action:
                    if mazeDef.maze_map[state][direction]==True:  
                        next_state = mdpVI().mazeTrace(mazeDef, state, direction)
                # utility = 0
                reward = REWARD[state]
                if next_state == target[0]:
                    reward = 10**(7)
                # utility += prob * (reward + DISCOUNT * U[next_state])
                utility = REWARD[state] + DISCOUNT*(prob*U[next_state])
                if utility > max_utility:
                    max_utility = utility
                    max_action = action
                    # is_value_changed == True
                policy[state] = max_action
                U[state] = max_utility
                if policy[state] != max_action:
                    is_policy_changed = True
                    policy[state] = max_action
            iterations += 1
            
    
currNode = (x,y)   
tracePath = {}
agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
while currNode != target[0]:
    test = mdpVI().mazeTrace(mazeDef, currNode, policy[currNode])
    tracePath[currNode] = test
    currNode = test
    print(test)
mazeDef.tracePath({agent1: tracePath}, delay = 200)
mazeDef.run()