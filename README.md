# CS7IS2 Artificial Intelligence Assignment 1
## Maze Solver - Search and MDPs

Total Algorithms Implemented:
- Depth First Search (DFS)
- Breadth First Search (BFS)
- A-Star Algorithm
- Markov Decision Process (MDP)
  - Value Iteration
  - Policy Iteration
  
## Prerequisites
- Python 3.9.13
- Pyamaze 1.0.1

## Steps to run the program
To run the Maze solver (All 5 algorithms together), run the following commands in a sequential order:
- If cloning from the GIT repository
```
git clone https://github.com/abhikbhattacharjee/CS7IS2-AI-Maze-Solver.git
cd CS7IS2-AI-Maze-Solver
cd MazeSolver
python main.py
```
- If executing from the zip file provided:
```
cd <directory>
cd MazeSolver
python main.py
```
After triggering the the main script, the user would be presented with the following menu:
```
(base) abhik_bhattacharjee@Abhiks-MacBook-Pro MazeSolver % python main.py

 Please select Maze: 

 1. 5x5 Maze
 2. 30x30 Maze
 3. 50x50 Maze
 4. 25x50 Maze
 5. Custom Maze
 
 Enter Choice:
```

The first 4 options in the menu are the mazes on which the analysis of performance for different algorithms were carried out. For greater flexibility, the user is also provided with an option to create a custom maze and decide whether they want the MDP algorithms to be deterministic or stochastic.

Following is the sample text output generated by the program which shows the number of steps required and time taken by each algorithm to converge to the target state:
```
(base) abhik_bhattacharjee@Abhiks-MacBook-Pro MazeSolver % python main.py

 Please select Maze: 

 1. 5x5 Maze
 2. 30x30 Maze
 3. 50x50 Maze
 4. 25x50 Maze
 5. Custom Maze

 Enter Choice: 2
 Selected 30x30 Maze

 MDP Metrics
 Default Target : (1,1)
 Reward : -4
 Discount : 0.8
 Error : 0.001
 TOTAL STEPS MDP VI: 65
 TOTAL TIME ELAPSED MDP VI: 0.004949092864990234

 TOTAL STEPS MDP PI: 59
 TOTAL TIME ELAPSED MDP PI: 0.0047838687896728516

 TOTAL STEPS A Star: 55
 TOTAL TIME ELAPSED A Star: 0.0005428791046142578

 TOTAL STEPS BFS: 59
 TOTAL TIME ELAPSED BFS: 0.013682842254638672

 TOTAL STEPS DFS: 249
 TOTAL TIME ELAPSED DFS: 0.013682842254638672
 
 Optimal Policy for Policy Iteration Stored in variable 'policy1'
 Optimal Values for states in Value Iteration Stored in variable 'U'
```

To run the Maze solver (Only 3 Search Algorithms), run the following commands in a sequential order after cloning the repo:
```
cd OutTakes
python SearchAlgos.py
```

To run the Maze solver (Only 2 MDP Algorithms), run the following commands in a sequential order after cloning the repo:
```
cd OutTakes
python mdpInit.py
```

A sample end result of a solved 30x30 maze is given below:
- Legend  
  - Blue Arrow: A-Star Algorithm
  - Yellow Arrow: BFS
  - Red Arrow: DFS
  - Black Filled Cells: MDP Policy Iteration
  - Cyan Filled Cells: MDP Value Iteration

<img width="1512" alt="Screenshot 2023-03-10 at 17 45 45" src="https://user-images.githubusercontent.com/42884077/224387101-1bf8ef07-c2b7-4ab7-8f8d-cb620200cf1e.png">


## References
- Stuart Russell and Peter Norvig. Artificial Intelligence: A Modern Approach (3rd ed.)
- [aima-code](https://github.com/aimacode/aima-python): Implementation of algorithms from Russell And Norvig's "Artificial Intelligence - A Modern Approach"
- [Pyamaze](https://github.com/MAN1986/pyamaze)
- [MDP_VI_PI_Q-learning_AIMA.ipynb](https://github.com/tirthajyoti/RL_basics/blob/master/MDP_VI_PI_Q-learning_AIMA.ipynb) by [Tirthajyoti Sarkar](https://github.com/tirthajyoti)
- [Markov Decision Process](https://jsu800.github.io/docs/ml_mdp.pdf) by Joseph Su. Department of Computer Science, Georgia Institute of Technology
