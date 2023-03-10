#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:17:39 2023

@author: abhik_bhattacharjee
"""

from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
import time

class mazeCreate:
    
    def agntMake(self, mazeDef, traceShape, traceColor, fill = False):
        agnt = agent(mazeDef, footprints=True, shape = traceShape, color = traceColor, filled=fill)
        return agnt
    
    def stepCount(self, mazeDef, name, algo):
        stepLabel = textLabel(mazeDef, f'{name} Steps: ', len(algo)+1)
        return stepLabel
    
    def algoTime(self, mazeDef, name, delta):
        stepLabelT = textLabel(mazeDef, f'{name} Time: ', round(delta, 5))
        return stepLabelT

class searchAlgo:
    
    def mazeTrace(self, mazeDef, currentNode, direction):     
        if direction == 'E':
            return (currentNode[0], currentNode[1]+1)
        elif direction == 'W':
            return (currentNode[0], currentNode[1]-1)
        elif direction == 'N':
            return (currentNode[0]-1, currentNode[1])
        elif direction == 'S':
            return (currentNode[0]+1, currentNode[1])
    
    def aiAlgo(self, algo, mazeDef, xtarget, ytarget):
        start = time.time()
        startNode = (mazeDef.rows, mazeDef.cols)
        target = (xtarget, ytarget)
        cell = (xtarget, ytarget)
        container = [startNode]
        
        adjNode = [startNode]
        
        algoPath = {}
        tracePath = {}
        
        while len(container) > 0:
            if algo == 'DFS':
                currentNode = container.pop()
            elif algo == 'BFS':
                currentNode = container.pop(0)
            if currentNode == target:
                break
            for direction in 'NSEW':
                if mazeDef.maze_map[currentNode][direction]==True:        
                    nextNode = self.mazeTrace(mazeDef, currentNode, direction)
                    if nextNode in adjNode:
                        continue
                    adjNode.append(nextNode)
                    container.append(nextNode)
                    
                    algoPath[nextNode] = currentNode
                
        while cell != startNode:
            tracePath[algoPath[cell]] = cell
            cell = algoPath[cell]
        end = time.time()
        return tracePath, (end-start)

class aStar:
    
    def calNodeCost(self, node1, node2):
        nodex1,nodey1 = node1
        nodex2,nodey2 = node2
        return (abs(nodex1 - nodex2) + abs(nodey1 - nodey2))
    
    def aStarInit(self, mazeDef, xtarget, ytarget):
        startNode = (mazeDef.rows, mazeDef.cols)
        nodeDist = dict.fromkeys(mazeDef.grid, float('inf'))
        totalNodeCost = dict.fromkeys(mazeDef.grid, float('inf'))
        return startNode, nodeDist, totalNodeCost 

    def aStar(self, mazeDef, xtarget, ytarget):
        start = time.time()
        startNode, nodeDist, totalNodeCost = self.aStarInit(mazeDef, xtarget, ytarget)
        nodeDist[startNode] = 0
        totalNodeCost[startNode] = self.calNodeCost(startNode, (xtarget, ytarget))
        algoPath = {}
        tracePath = {}
        nextNode = None
        tempNodeDist = None
        tempTotalNodeCost = None
        currentNode = None
        cell = (xtarget, ytarget)
        container = PriorityQueue()
        container.put((self.calNodeCost(startNode, (xtarget, ytarget)), self.calNodeCost(startNode, (xtarget, ytarget)), startNode))
        
        while not container.empty():
            currentNode = container.get()[2]
            
            if currentNode == (xtarget, ytarget):
                break
            for direction in 'NSEW':
                if mazeDef.maze_map[currentNode][direction]==True:
                    nextNode = searchAlgo().mazeTrace(mazeDef, currentNode, direction)

                tempNodeDist = nodeDist[currentNode] + 1
                tempTotalNodeCost = tempNodeDist + self.calNodeCost(nextNode, (xtarget, ytarget))
                
                if tempTotalNodeCost < totalNodeCost[nextNode]:
                    nodeDist[nextNode] = tempNodeDist
                    totalNodeCost[nextNode] = tempTotalNodeCost
                    container.put((tempTotalNodeCost, self.calNodeCost(nextNode, (xtarget, ytarget)), nextNode))
                    algoPath[nextNode] = currentNode
       
        while cell != startNode:
            tracePath[algoPath[cell]] = cell
            cell = algoPath[cell]
        end = time.time()
        return tracePath, (end-start)