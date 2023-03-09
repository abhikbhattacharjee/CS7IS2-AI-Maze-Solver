#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:43:54 2023

@author: abhik_bhattacharjee
"""

from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
GLOBAL_VISITED = []

class mdpVI():
    
    def mdpVIInit(self, xTarget, yTarget, reward, gamma, error):
        self.REWARD = reward
        self.DISCOUNT = gamma
        self.MAX_ERROR = error
        self.ACTIONS = {}
        self.U = self.target = [(xTarget, yTarget)]
        self.policy = {}
        self.tracePath = {}
        self.algoPath = {}
        return self.REWARD, self.DISCOUNT, self.MAX_ERROR, self.ACTIONS, self.U, self.target, self.policy, self.tracePath, self.algoPath

    def mdpVIActions(self, mazeDef):
        for key, val in mazeDef.maze_map.items():
            self.ACTIONS[key] = [(k, v) for k, v in val.items() if v == 1]

        for k, v in self.ACTIONS.items():
            self.ACTIONS[k] = dict(v)
        
        for key, val in self.ACTIONS.items():
            for k, v in val.items():
                if k == 'N':
                    val[k] = 0.80
                elif k == 'W':
                    val[k] = 0.1
                elif k == 'E':
                    val[k] = 0.05
                elif k == 'S':
                    val[k] = 0.05
                
        self.U = {state: 0 for state in self.ACTIONS.keys()}
        self.U[self.target[0]] = 1
        
        return self.ACTIONS, self.U
    
    def mazeTrace(self, mazeDef, currentNode, direction):     
        if direction == 'E':
            return (currentNode[0], currentNode[1]+1)
        elif direction == 'W':
            return (currentNode[0], currentNode[1]-1)
        elif direction == 'N':
            return (currentNode[0]-1, currentNode[1])
        elif direction == 'S':
            return (currentNode[0]+1, currentNode[1])
    
    def mdpValIter(self, xTarget, yTarget, reward, gamma, error, mazeDef):
        REWARD, DISCOUNT, MAX_ERROR, ACTIONS, U, target, policy, tracePath, algoPath = self.mdpVIInit(xTarget, yTarget, reward, gamma, error)
        ACTIONS, U = self.mdpVIActions(mazeDef)
        while True:
            delta = 0
            for state in ACTIONS.keys():
                if state == target[0]:
                    continue
                max_utility = float("-infinity")
                max_action = None
                for action, prob in ACTIONS[state].items():
                    for direction in action:
                        if mazeDef.maze_map[state][direction]==True:  
                            next_state = self.mazeTrace(mazeDef, state, direction)
                    utility = 0
                    reward = REWARD
                    if next_state == target[0]:
                        reward = 1
                    utility += prob * (reward + DISCOUNT * U[next_state])
                    if utility > max_utility:
                        max_utility = utility
                        max_action = action
                delta = max(delta, abs(max_utility - U[state]))
                U[state] = max_utility
                policy[state] = max_action
            if delta < MAX_ERROR:
                break
            return U, policy, ACTIONS
            
    def mazeTrack(self, currNode, xTarget, yTarget, reward, gamma, error, mazeDef):
        U, policy, ACTIONS = self.mdpValIter(xTarget, yTarget, reward, gamma, error, mazeDef)
        node = currNode
        while True:
            bestNode = None
            bestNodeVal = None
            if node == self.target[0]:
                break
            for direction in 'NWSE':
                if mazeDef.maze_map[node][direction] == True and self.mazeTrace(mazeDef, node, direction) not in GLOBAL_VISITED:
                    directionalNode =  self.mazeTrace(mazeDef, node, direction)
                    if  directionalNode == self.target[0]:
                        bestNode =  directionalNode
                        bestNodeVal = self.U[bestNode]
                        break
                    if bestNodeVal == None:
                        bestNode = directionalNode
                        bestNodeVal = self.U[bestNode]
                    else:
                        tempNode = directionalNode
                        if bestNodeVal < self.U[tempNode]:
                            bestNode = tempNode
                            bestNodeVal = self.U[tempNode]
            GLOBAL_VISITED.append(bestNode)
            self.tracePath[node] = bestNode
            node = bestNode
        return self.tracePath, U, policy
    
if __name__=='__main__':
    print("\n Please select Maze: \n")
    print(" 1. 5x5 Maze\n")
    print(" 2. 30x30 Maze\n")
    print(" 3. 50x50 Maze\n")
    print(" 4. 100x100 Maze\n")
    print(" 5. 25x50 Maze\n")
    menu1 = input("\n Enter Choice: ")
    choice = int(menu1)
    
    if choice == 1:
        print(" Selected 5x5 Maze\n")
        print(" Default Target : (1,1)\n Reward : 4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(5,5)
        mazeDef.CreateMaze(loadMaze='./Maze/maze5.csv')
        track, U, policy = mdpVI().mazeTrack((5,5), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
        mazeDef.tracePath({agent1: track}, delay=200)
        mazeDef.run()
    elif choice == 2:
        print(" Selected 30x30 Maze\n")
        print(" Default Target : (1,1)\n Reward : 4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(30,30)
        mazeDef.CreateMaze(loadMaze='./Maze/maze30.csv')
        track, U, policy = mdpVI().mazeTrack((30,30), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
        mazeDef.tracePath({agent1: track}, delay=200)
        mazeDef.run()
    elif choice == 3:
        print(" Selected 50x50 Maze\n")
        print(" Default Target : (1,1)\n Reward : 4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(50,50)
        mazeDef.CreateMaze(loadMaze='./Maze/maze50.csv')
        track, U, policy = mdpVI().mazeTrack((50,50), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
        mazeDef.tracePath({agent1: track}, delay=200)
        mazeDef.run()
    elif choice == 4:
        print(" Selected 100x100 Maze\n")
        print(" Default Target : (1,1)\n Reward : 4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(100,100)
        mazeDef.CreateMaze(loadMaze='./Maze/maze100.csv')
        track, U, policy = mdpVI().mazeTrack((100,100), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
        mazeDef.tracePath({agent1: track}, delay=200)
        mazeDef.run()
    elif choice == 5:
        print(" Selected 25x50 Maze\n")
        print(" Default Target : (1,1)\n Reward : 4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(25,50)
        mazeDef.CreateMaze(loadMaze='./Maze/maze2550.csv')
        track, U, policy = mdpVI().mazeTrack((25,50), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        agent1 = agent(mazeDef, shape = 'arrow', footprints = True, color = COLOR.red)
        mazeDef.tracePath({agent1: track}, delay=200)
        mazeDef.run()
    else:
        print(" Wrong Option Selected! \n Exiting!\n")
