#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:10:35 2023

@author: abhik_bhattacharjee
"""
from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
import time
import random
from classMDP import mdpPI
from classMDP import mdpVI
from classSolver import aStar
from classSolver import mazeCreate
from classSolver import searchAlgo
GLOBAL_VISITED = []

def printMetrics(algo, tracePath, delta):
    total = len(tracePath) + 1
    print(f' TOTAL STEPS {algo}: {total}')
    print(f' TOTAL TIME ELAPSED {algo}: {delta}\n')

if __name__=='__main__':
    print("\n Please select Maze: \n")
    print(" 1. 5x5 Maze\n")
    print(" 2. 30x30 Maze\n")
    print(" 3. 50x50 Maze\n")
    print(" 4. 25x50 Maze\n")
    print(" 5. Custom Maze\n")
    menu1 = input("\n Enter Choice: ")
    choice = int(menu1)
    
    if choice == 1:
        print(" Selected 5x5 Maze\n")
        print(" MDP Metrics\n Default Target : (1,1)\n Reward : -4\n Discount : 0.8\n Error : 0.001\n")
        mazeDef = maze(5,5)
        mazeDef.CreateMaze(1, 1, loadMaze='./Maze/maze5.csv', theme = COLOR.light)
        
        track, U, policy, actions, timediff = mdpVI().mazeTrack((5,5), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        path, U1, policy1, timeDiff = mdpPI().mdpPolIter(5, 5, 1, 1, mazeDef)
        pathDFS = searchAlgo().aiAlgo('DFS', mazeDef, 1, 1)
        pathBFS = searchAlgo().aiAlgo('BFS', mazeDef, 1, 1)
        pathAStar = aStar().aStar(mazeDef, 1, 1)
        
        printMetrics('MDP VI', track, timediff)
        printMetrics('MDP PI', path, timeDiff)
        printMetrics('A Star', pathAStar[0], pathAStar[1])
        printMetrics('BFS', pathBFS[0], pathDFS[1])
        printMetrics('DFS', pathDFS[0], pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'DFS', pathDFS[0])
        mazeCreate().algoTime(mazeDef, 'DFS', pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'BFS', pathBFS[0])
        mazeCreate().algoTime(mazeDef, 'BFS', pathBFS[1])
        
        mazeCreate().stepCount(mazeDef, 'A Star', pathAStar[0])
        mazeCreate().algoTime(mazeDef, 'A Star', pathAStar[1])
        
        mazeCreate().stepCount(mazeDef, 'MDP VI', track)
        mazeCreate().algoTime(mazeDef, 'MDP VI', timediff)
        
        mazeCreate().stepCount(mazeDef, 'MDP PI', path)
        mazeCreate().algoTime(mazeDef, 'MDP PI', timeDiff)
        
        agnt = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.red)
        agnt2 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.yellow)
        agnt3 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.blue)
        agnt4 = mazeCreate().agntMake(mazeDef, 'square', COLOR.cyan, fill = True)
        agnt5 = mazeCreate().agntMake(mazeDef, 'square', COLOR.black, fill = True)
        
        mazeDef.tracePath({agnt4: track, agnt5: path, agnt: pathDFS[0], agnt2: pathBFS[0], agnt3: pathAStar[0]}, delay=200)
        mazeDef.run()
    
    elif choice == 2:
        print(" Selected 30x30 Maze\n")
        print(" MDP Metrics\n Default Target : (1,1)\n Reward : -4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(30,30)
        mazeDef.CreateMaze(1, 1, loadMaze='./Maze/maze30.csv', theme = COLOR.light)
        
        track, U, policy, actions, timediff = mdpVI().mazeTrack((30,30), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        path, U1, policy1, timeDiff = mdpPI().mdpPolIter(30, 30, 1, 1, mazeDef)
        pathDFS = searchAlgo().aiAlgo('DFS', mazeDef, 1, 1)
        pathBFS = searchAlgo().aiAlgo('BFS', mazeDef, 1, 1)
        pathAStar = aStar().aStar(mazeDef, 1, 1)
        
        printMetrics('MDP VI', track, timediff)
        printMetrics('MDP PI', path, timeDiff)
        printMetrics('A Star', pathAStar[0], pathAStar[1])
        printMetrics('BFS', pathBFS[0], pathDFS[1])
        printMetrics('DFS', pathDFS[0], pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'DFS', pathDFS[0])
        mazeCreate().algoTime(mazeDef, 'DFS', pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'BFS', pathBFS[0])
        mazeCreate().algoTime(mazeDef, 'BFS', pathBFS[1])
        
        mazeCreate().stepCount(mazeDef, 'A Star', pathAStar[0])
        mazeCreate().algoTime(mazeDef, 'A Star', pathAStar[1])
        
        mazeCreate().stepCount(mazeDef, 'MDP VI', track)
        mazeCreate().algoTime(mazeDef, 'MDP VI', timediff)
        
        mazeCreate().stepCount(mazeDef, 'MDP PI', path)
        mazeCreate().algoTime(mazeDef, 'MDP PI', timeDiff)
        
        agnt = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.red)
        agnt2 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.yellow)
        agnt3 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.blue)
        agnt4 = mazeCreate().agntMake(mazeDef, 'square', COLOR.cyan, fill = True)
        agnt5 = mazeCreate().agntMake(mazeDef, 'square', COLOR.black, fill = True)
        
        mazeDef.tracePath({agnt4: track, agnt5: path, agnt: pathDFS[0], agnt2: pathBFS[0], agnt3: pathAStar[0]}, delay=200)
        mazeDef.run()
    
    elif choice == 3:
        print(" Selected 50x50 Maze\n")
        print(" MDP Metrics\n Default Target : (1,1)\n Reward : -4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(50,50)
        mazeDef.CreateMaze(1, 1, loadMaze='./Maze/maze50.csv', theme = COLOR.light)
        
        track, U, policy, actions, timediff = mdpVI().mazeTrack((50,50), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        path, U1, policy1, timeDiff = mdpPI().mdpPolIter(50, 50, 1, 1, mazeDef)
        pathDFS = searchAlgo().aiAlgo('DFS', mazeDef, 1, 1)
        pathBFS = searchAlgo().aiAlgo('BFS', mazeDef, 1, 1)
        pathAStar = aStar().aStar(mazeDef, 1, 1)
        
        printMetrics('MDP VI', track, timediff)
        printMetrics('MDP PI', path, timeDiff)
        printMetrics('A Star', pathAStar[0], pathAStar[1])
        printMetrics('BFS', pathBFS[0], pathDFS[1])
        printMetrics('DFS', pathDFS[0], pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'DFS', pathDFS[0])
        mazeCreate().algoTime(mazeDef, 'DFS', pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'BFS', pathBFS[0])
        mazeCreate().algoTime(mazeDef, 'BFS', pathBFS[1])
        
        mazeCreate().stepCount(mazeDef, 'A Star', pathAStar[0])
        mazeCreate().algoTime(mazeDef, 'A Star', pathAStar[1])
        
        mazeCreate().stepCount(mazeDef, 'MDP VI', track)
        mazeCreate().algoTime(mazeDef, 'MDP VI', timediff)
        
        mazeCreate().stepCount(mazeDef, 'MDP PI', path)
        mazeCreate().algoTime(mazeDef, 'MDP PI', timeDiff)
        
        agnt = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.red)
        agnt2 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.yellow)
        agnt3 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.blue)
        agnt4 = mazeCreate().agntMake(mazeDef, 'square', COLOR.cyan, fill = True)
        agnt5 = mazeCreate().agntMake(mazeDef, 'square', COLOR.black, fill = True)
        
        mazeDef.tracePath({agnt4: track, agnt5: path, agnt: pathDFS[0], agnt2: pathBFS[0], agnt3: pathAStar[0]}, delay=200)
        mazeDef.run()
    
    elif choice == 4:
        print(" Selected 25x50 Maze\n")
        print(" MDP Metrics\n Default Target : (1,1)\n Reward : -4\n Discount : 0.8\n Error : 0.001")
        mazeDef = maze(25,50)
        mazeDef.CreateMaze(1, 1, loadMaze='./Maze/maze2550.csv', theme = COLOR.light)
        
        track, U, policy, actions, timediff = mdpVI().mazeTrack((25,50), 1, 1, -4, 0.8, 10**(-3), mazeDef)
        path, U1, policy1, timeDiff = mdpPI().mdpPolIter(25, 50, 1, 1, mazeDef)
        pathDFS = searchAlgo().aiAlgo('DFS', mazeDef, 1, 1)
        pathBFS = searchAlgo().aiAlgo('BFS', mazeDef, 1, 1)
        pathAStar = aStar().aStar(mazeDef, 1, 1)
        
        printMetrics('MDP VI', track, timediff)
        printMetrics('MDP PI', path, timeDiff)
        printMetrics('A Star', pathAStar[0], pathAStar[1])
        printMetrics('BFS', pathBFS[0], pathDFS[1])
        printMetrics('DFS', pathDFS[0], pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'DFS', pathDFS[0])
        mazeCreate().algoTime(mazeDef, 'DFS', pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'BFS', pathBFS[0])
        mazeCreate().algoTime(mazeDef, 'BFS', pathBFS[1])
        
        mazeCreate().stepCount(mazeDef, 'A Star', pathAStar[0])
        mazeCreate().algoTime(mazeDef, 'A Star', pathAStar[1])
        
        mazeCreate().stepCount(mazeDef, 'MDP VI', track)
        mazeCreate().algoTime(mazeDef, 'MDP VI', timediff)
        
        mazeCreate().stepCount(mazeDef, 'MDP PI', path)
        mazeCreate().algoTime(mazeDef, 'MDP PI', timeDiff)
        
        agnt = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.red)
        agnt2 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.yellow)
        agnt3 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.blue)
        agnt4 = mazeCreate().agntMake(mazeDef, 'square', COLOR.cyan, fill = True)
        agnt5 = mazeCreate().agntMake(mazeDef, 'square', COLOR.black, fill = True)
        
        mazeDef.tracePath({agnt4: track, agnt5: path, agnt: pathDFS[0], agnt2: pathBFS[0], agnt3: pathAStar[0]}, delay=200)
        mazeDef.run()
    
    elif choice == 5:
        print(" Selected Custom Maze\n")
        
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
        print("\n Stochastic? \n")
        sx = input("\n (y/n) ")
        sc = str(sx)
        if sc == 'y':
            stochastic = True
        elif sc =='n':
            stochastic = False
        
        mazeDef = maze(x, y)
        mazeDef.CreateMaze(tarx, tary, loopPercent=100, theme = COLOR.light)
        
        track, U, policy, actions, timediff = mdpVI().mazeTrack((x,y), tarx, tary, -4, 0.8, 10**(-3), mazeDef, stochastic)
        path, U1, policy1, timeDiff = mdpPI().mdpPolIter(x, y, tarx, tary, mazeDef)
        
        pathDFS = searchAlgo().aiAlgo('DFS', mazeDef, tarx, tary)
        pathBFS = searchAlgo().aiAlgo('BFS', mazeDef, tarx, tary)
        pathAStar = aStar().aStar(mazeDef, tarx, tary)
        
        printMetrics('MDP VI', track, timediff)
        printMetrics('MDP PI', path, timeDiff)
        printMetrics('A Star', pathAStar[0], pathAStar[1])
        printMetrics('BFS', pathBFS[0], pathDFS[1])
        printMetrics('DFS', pathDFS[0], pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'DFS', pathDFS[0])
        mazeCreate().algoTime(mazeDef, 'DFS', pathDFS[1])
        
        mazeCreate().stepCount(mazeDef, 'BFS', pathBFS[0])
        mazeCreate().algoTime(mazeDef, 'BFS', pathBFS[1])
        
        mazeCreate().stepCount(mazeDef, 'A Star', pathAStar[0])
        mazeCreate().algoTime(mazeDef, 'A Star', pathAStar[1])
        
        mazeCreate().stepCount(mazeDef, 'MDP VI', track)
        mazeCreate().algoTime(mazeDef, 'MDP VI', timediff)
        
        mazeCreate().stepCount(mazeDef, 'MDP PI', path)
        mazeCreate().algoTime(mazeDef, 'MDP PI', timeDiff)
        
        agnt = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.red)
        agnt2 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.yellow)
        agnt3 = mazeCreate().agntMake(mazeDef, 'arrow', COLOR.blue)
        agnt4 = mazeCreate().agntMake(mazeDef, 'square', COLOR.cyan, fill = True)
        agnt5 = mazeCreate().agntMake(mazeDef, 'square', COLOR.black, fill = True)
        
        mazeDef.tracePath({agnt4: track, agnt5: path, agnt: pathDFS[0], agnt2: pathBFS[0], agnt3: pathAStar[0]}, delay=200)
        mazeDef.run()
    
    else:
        print(" Wrong Option Selected! \n Exiting!\n")
        
    print("\n Optimal Policy for Policy Iteration Stored in variable 'policy1'\n")
    print("\n Optimal Values for states in Value Iteration Stored in variable 'U'\n")