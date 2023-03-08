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
mazeDef.CreateMaze(tarx, tary, loopPercent = 100, theme = COLOR.light)

REWARD = -1
DISCOUNT = 0.9
MAX_ERROR = 10**(-3)

ACTIONS = {}


for key, val in mazeDef.maze_map.items():
    ACTIONS[key] = [(k, v) for k, v in val.items() if v == 1]

for k, v in ACTIONS.items():
    ACTIONS[k] = dict(v)
    
for key, val in ACTIONS.items():
    LENGTH = len(val.keys())
    for dire, value in val.items():
        ACTIONS[key][dire] /= LENGTH

# for key, val in ACTIONS.items():
#     for k, v in val.items():
#         if k == 'N':
#             val[k] = 0.8
#         elif k == 'W':
#             val[k] = 0
#         elif k == 'E':
#             val[k] = 0
#         elif k == 'S':
#             val[k] = 0.2
    
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
tracePath = {}
algoPath = {}

while True:
    delta = 0
    for state in ACTIONS.keys():
        if state == target[0]:
            continue
        max_utility = float("-inf")
        max_action = None
        for action, prob in ACTIONS[state].items():
            for direction in action:
                if mazeDef.maze_map[state][direction]==True:  
                    next_state = mazeTrace(mazeDef, state, direction)
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

GLOBAL_VISITED = []
def mazeTrack(currNode, maze):
    node = currNode
    nodeList = dict()
    while True:
        bestNode = None
        bestNodeVal = None
        if node == target[0]:
            # print("Encountered final")
            break
        for direction in 'NWSE':
            if maze.maze_map[node][direction] == True and mazeTrace(maze, node, direction) not in GLOBAL_VISITED:
                directionalNode =  mazeTrace(maze, node, direction)
                if  directionalNode == target[0]:
                    bestNode =  directionalNode
                    bestNodeVal = U[bestNode]
                    break
                if bestNodeVal == None:
                    bestNode = directionalNode
                    bestNodeVal = U[bestNode]
                else:
                    tempNode = directionalNode
                    if bestNodeVal < U[tempNode]:
                        bestNode = tempNode
                        bestNodeVal = U[tempNode]
                GLOBAL_VISITED.append(node)
        tracePath[node] = bestNode
        node = bestNode
    return tracePath
        
track = mazeTrack((x,y), mazeDef)
agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
mazeDef.tracePath({agent1: track}, delay=200)
mazeDef.run()
