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
import time

def mdpPolIter(x, y, tarx, tary, mazeDef):
    start = time.time()
    target = [(tarx, tary)]
    actions = {}
    for key, val in mazeDef.maze_map.items():
        actions[key] = [(k, v) for k, v in val.items() if v == 1]

    for k, v in actions.items():
        actions[k] = dict(v)

    U = {state: 0 for state in actions.keys()}
    U[target[0]] = 10**(8)
    policy = {s: random.choice('NSEW') for s in actions.keys()}
    
    REWARD = {state: -40 for state in actions.keys()}
    REWARD[target[0]] = 10**(8)
    DISCOUNT = 0.9
    is_policy_changed = True
    iterations = 0
    
    while is_policy_changed:
        is_policy_changed = False
        is_value_changed = True
        while is_value_changed:
            is_value_changed = False
            for state in actions.keys():
                if state == target[0]:
                    continue
                max_utility = float("-infinity")
                max_action = None
                for action, prob in actions[state].items():
                    for direction in action:
                        if mazeDef.maze_map[state][direction]==True:  
                            next_state = mdpVI().mazeTrace(mazeDef, state, direction)
                    reward = REWARD[state]
                    if next_state == target[0]:
                        reward = 10**(7)
                    utility = reward + DISCOUNT*(prob*U[next_state])
                    if utility > max_utility:
                        max_utility = utility
                        max_action = action
                    policy[state] = max_action
                    U[state] = max_utility
                    if policy[state] != max_action:
                        is_policy_changed = True
                        policy[state] = max_action
                iterations += 1
    currNode = (x,y)   
    tracePath = {}
    while currNode != target[0]:
        test = mdpVI().mazeTrace(mazeDef, currNode, policy[currNode])
        tracePath[currNode] = test
        currNode = test
    end = time.time()
    return tracePath, U, policy, (end-start)

if __name__=='__main__':
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
    
    path, U1, policy1, timeDiff = mdpPolIter(x, y, tarx, tary, mazeDef)
    track, U2, policy2, actions, timediff = mdpVI().mazeTrack((x,y), tarx, tary, -4, 0.8, 10**(-3), mazeDef, stochastic = False)
    
    
    agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
    agent2 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.yellow)
    mazeDef.tracePath({agent1: path, agent2:track}, delay = 200)
    mazeDef.run()
