#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:46:22 2023

@author: abhik_bhattacharjee
"""

from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

class mazeCreate:
    
    def mazeData(self, sizeX, sizeY, targetX, targetY, loopPer):
        mazeDef = maze(sizeX, sizeY)
        mazeDef.CreateMaze(targetX, targetY, loopPercent = loopPer, theme = COLOR.light)
        return mazeDef
    
    def agntMake(self, mazeDef, traceShape, traceColor):
        agnt = agent(mazeDef, footprints=True, shape = traceShape, color = traceColor)
        return agnt
    
    def stepCount(self, mazeDef, name, algo):
        stepLabel = textLabel(mazeDef, f'{name} Steps: ', len(algo)+1)
        return stepLabel

class searchAlgo:
    
    def mazeTrace(self, maze, currentNode, direction):     
        if direction == 'E':
            return (currentNode[0], currentNode[1]+1)
        elif direction == 'W':
            return (currentNode[0], currentNode[1]-1)
        elif direction == 'N':
            return (currentNode[0]-1, currentNode[1])
        elif direction == 'S':
            return (currentNode[0]+1, currentNode[1])
    
    
    def aiAlgo(self, algo, maze, xtarget, ytarget):
        startNode = (maze.rows, maze.cols)
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
                if maze.maze_map[currentNode][direction]==True:        
                    nextNode = self.mazeTrace(maze, currentNode, direction)
                    if nextNode in adjNode:
                        continue
                    adjNode.append(nextNode)
                    container.append(nextNode)
                    
                    algoPath[nextNode] = currentNode
                
        while cell != startNode:
            tracePath[algoPath[cell]] = cell
            cell = algoPath[cell]
        return tracePath

    def mazePlot(self, xshape, yshape, xtarget, ytarget):
        mazeDef = mazeCreate().mazeData(xshape, yshape, xtarget, ytarget, 100)
        
        pathDFS = self.aiAlgo('DFS', mazeDef, xtarget, ytarget)
        pathBFS = self.aiAlgo('BFS', mazeDef, xtarget, ytarget)
        pathAStar = aStar().aStar(mazeDef, xtarget, ytarget)
        
        agnt = mazeCreate().agntMake(mazeDef, 'square', COLOR.red)
        agnt2 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.yellow)
        agnt3 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.green)
        
        mazeCreate().stepCount(mazeDef, 'DFS', pathDFS)
        mazeCreate().stepCount(mazeDef, 'BFS', pathBFS)
        mazeCreate().stepCount(mazeDef, 'A Star', pathAStar)
        
        mazeDef.tracePath({agnt:pathDFS, agnt2:pathBFS, agnt3:pathAStar}, delay=400)
        mazeDef.run()

class aStar:
    
    def calNodeCost(self, node1, node2):
        nodex1,nodey1 = node1
        nodex2,nodey2 = node2
        return (abs(nodex1 - nodex2) + abs(nodey1 - nodey2))
    
    def aStarInit(self, maze, xtarget, ytarget):
        startNode = (maze.rows, maze.cols)
        nodeDist = dict.fromkeys(maze.grid, float('inf'))
        totalNodeCost = dict.fromkeys(maze.grid, float('inf'))
        return startNode, nodeDist, totalNodeCost 

    def aStar(self, maze, xtarget, ytarget):
        startNode, nodeDist, totalNodeCost = self.aStarInit(maze, xtarget, ytarget)
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
                if maze.maze_map[currentNode][direction]==True:
                    nextNode = searchAlgo().mazeTrace(maze, currentNode, direction)

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
        return tracePath        

if __name__=='__main__':
    searchAlgo().mazePlot(10, 19, 6, 9)
    