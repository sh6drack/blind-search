[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zfxHeKS3)
# assignment-1-blind-search

# TASK 2
In your README, describe maze generation as a basic search problem (which we described in english above). What are the states and transitions? What are the start and goal states?

States are different configurations of the grid with walls where each state represents which walls exist in the maze.

Start State: A completely walled grid where every possible wall between adjacent cells exists

Goal State:A perfect maze with exactly one path between any two cells (no cycles, all cells connected)

Transitions: Remove a wall between two adjacent cells, connecting those cells

# TESTS
def test_bfs_simple_path(self):
    """Tests BFS finds correct path and statistics on a basic linear 3-node graph (0->1->2)."""

def test_dfs_simple_path(self):
    """Tests DFS finds correct path and statistics on a basic linear 3-node graph (0->1->2)."""

def test_no_path_exists(self):
    """Tests both algorithms properly raise PathNotFoundError when goal state is unreachable."""

def test_start_is_goal(self):
    """Tests edge case where start state equals goal state, expecting immediate return with zero expansions."""

def test_multiple_paths_bfs_optimal(self):
    """Tests BFS finds shortest path in diamond-shaped graph with two equal-length routes to goal."""

def test_frontier_size_tracking(self):
    """Tests max_frontier_size statistic correctly tracks peak memory usage during search."""

def test_cycle_handling(self):
    """Tests algorithms avoid infinite loops in graphs containing cycles by using visited set."""

def test_large_graph_performance(self):
    """Tests scalability on 11-node linear chain to verify performance on larger state spaces."""

def test_stats_consistency(self):
    """Tests search statistics remain identical across multiple runs on the same graph."""

def test_maze_small(self):
    """Tests both algorithms work correctly on actual Maze objects with 1x1 and 2x2 dimensions."""
    
Collaborators (if any):

AI Use Description: 
Used Claude AI for debugging BFS/DFS implementation, understanding assignment requirements, and generating tests

You must acknowledge use here and submit transcript if AI was used for portions of the assignment
