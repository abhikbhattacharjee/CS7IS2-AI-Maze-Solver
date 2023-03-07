#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:14:29 2023

@author: abhik_bhattacharjee
"""

from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

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
mazeDef.CreateMaze(x, y, loopPercent=100, theme=COLOR.light)

REWARD = -0.01 
DISCOUNT = 0.99
MAX_ERROR = 10**(-3)

NUM_ACTIONS = 4
ACTIONS = {}

def Convert(lst):
    res_dct = map(lambda i: (lst[i], lst[i+1]), range(len(lst)-1)[::2])
    return dict(res_dct)

for key, val in mazeDef.maze_map.items():
    ACTIONS[key] = [(k, v) for k, v in val.items() if v == 1]

for k, v in ACTIONS.items():
    ACTIONS[k] = dict(v)
    
U = target = [(tarx, tary)]

def mazeTrace(maze, currentNode, direction):     
    if direction == 'E':
        return (currentNode[0], currentNode[1]+1)
    elif direction == 'W':
        return (currentNode[0], currentNode[1]-1)
    elif direction == 'N':
        return (currentNode[0]-1, currentNode[1])
    elif direction == 'S':
        return (currentNode[0]+1, currentNode[1])

U = {state: 0 for state in ACTIONS.keys()}
U[target[0]] = 1
policy = {}

while True:
    delta = 0
    for state in ACTIONS.keys():
        if state == target[0]:
            continue
        max_utility = float("-inf")
        max_action = None
        for action, prob in ACTIONS[state].items():
            for direction in 'NSEW':
                if mazeDef.maze_map[state][direction]==True:  
                    next_state = mazeTrace(mazeDef, state, direction)
                    print(next_state)
            reward = REWARD
            if next_state == target[0]:
                reward = 1
            utility = prob * (reward + DISCOUNT * U[next_state])
            if utility > max_utility:
                max_utility = utility
                max_action = action
        delta = max(delta, abs(max_utility - U[state]))
        U[state] = max_utility
        policy[state] = max_action
    if delta < MAX_ERROR:
        break
