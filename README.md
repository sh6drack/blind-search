[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zfxHeKS3)
# assignment-1-blind-search

# TASK 2
In your README, describe maze generation as a basic search problem (which we described in english above). What are the states and transitions? What are the start and goal states?

States are different configurations of the grid with walls where each state represents which walls exist in the maze.

Start State: A completely walled grid where every possible wall between adjacent cells exists

Goal State:A perfect maze with exactly one path between any two cells (no cycles, all cells connected)

Transitions: Remove a wall between two adjacent cells, connecting those cells

# TESTS
 existing tests in unit_tests.py verify:
- BFS and DFS both find valid paths on small and large  mazes
- Returned paths correctly start at the maze start state and end at the goal state
- Path lengths match expected values for small mazes where optimal length is known (1 for 1x1 maze, 3 for 2x2 maze)
- Both algorithms handle edge cases like single-cell mazes

Collaborators (if any):

AI Use Description: 
Used Claude AI for debugging BFS/DFS implementation and understanding assignment requirements

You must acknowledge use here and submit transcript if AI was used for portions of the assignment
