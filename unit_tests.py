import unittest
from typing import Optional, Callable, Any, Tuple, List
from maze import Maze
from search import bfs, dfs, PathNotFoundError
from directed_graph import DirectedGraph

class IOTest(unittest.TestCase):
    """
    Tests IO for bfs and dfs implementations. Contains basic/trivial test cases.

    Each test instatiates a Maze object and tests the bfs and dfs algorithms on it.
    Note: The tests currently are only testing if the algorithms start and end at the
    correct locations and if the path returned is the correct length (optional).

    You may wish to add path validity checks. How do you know if a path is valid nor not?
    Your path should not teleport you, move through a wall, or go through a cell more than once.
    Maybe you should test for this... We certainly will during grading!

    These tests are not exhaustive and do not check if your implementation follows the
    algorithm correctly. We encourage you to create your own tests as necessary.
    """

    def _check_maze(self, algorithm: Callable[[Maze], Tuple[Optional[List[Any]], dict]], maze: Maze, length: Optional[int] = None) -> None:
        """
        Test algorithm on a Maze
        algorithm: algorithm to test
        maze: Maze to test algorithm on
        length: length that the path returned from algorithm should be.
                Think about why this argument is optional, and when you should provide it.
        """
        path = algorithm(maze)[0]
        self.assertIsNotNone(path, "Algorithm should return a valid path")
        
        if path is not None:
            self.assertEqual(path[0], maze.get_start_state(),
                             "Path should start with the start state")
            self.assertTrue(maze.is_goal_state(path[-1]),
                            "Path should end with the goal state")
            if length:
                self.assertEqual(len(path), length,
                                 f"Path length should be {length}")

    def test_bfs(self) -> None:
        single_cell_maze = Maze(1, 1)
        self._check_maze(bfs, single_cell_maze, 1)

        two_by_two_maze = Maze(2, 2)
        self._check_maze(bfs, two_by_two_maze, 3)

        large_maze = Maze(10, 10)
        self._check_maze(bfs, large_maze)
        # TODO: add tests here!

    def test_dfs(self) -> None:
        single_cell_maze = Maze(1, 1)
        self._check_maze(dfs, single_cell_maze, 1)

        two_by_two_maze = Maze(2, 2)
        self._check_maze(dfs, two_by_two_maze, 3)

        large_maze = Maze(10, 10)
        self._check_maze(dfs, large_maze)
        # TODO: add tests here!

    def test_bfs_simple_path(self):
        """Test BFS on a simple linear graph"""
        # Create adjacency matrix for: 0 -> 1 -> 2
        matrix = [
            [None, 1.0, None],  # State 0 connects to state 1
            [None, None, 1.0],  # State 1 connects to state 2  
            [None, None, None]  # State 2 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix, 
            goal_indices={2},
            start_state=0
        )
        
        path, stats = bfs(graph)
        
        self.assertEqual(path, [0, 1, 2])
        self.assertEqual(stats["path_length"], 3)
        self.assertEqual(stats["states_expanded"], 2)  # Only expand 0 and 1
        
    def test_dfs_simple_path(self):
        """Test DFS on a simple linear graph"""
        # Create adjacency matrix for: 0 -> 1 -> 2
        matrix = [
            [None, 1.0, None],  # State 0 connects to state 1
            [None, None, 1.0],  # State 1 connects to state 2  
            [None, None, None]  # State 2 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={2},
            start_state=0
        )
        
        path, stats = dfs(graph)
        
        self.assertEqual(path, [0, 1, 2])
        self.assertEqual(stats["path_length"], 3)
        self.assertEqual(stats["states_expanded"], 2)  # Only expand 0 and 1
        
    def test_no_path_exists(self):
        """Test when no path exists"""
        # Matrix: 0->1, but 2 is isolated
        matrix = [
            [None, 1.0, None],  # 0 -> 1
            [None, None, None],  # 1 has no outgoing edges
            [None, None, None]   # 2 is isolated
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={2},
            start_state=0
        )
        
        with self.assertRaises(PathNotFoundError):
            bfs(graph)
            
        with self.assertRaises(PathNotFoundError):
            dfs(graph)
            
    def test_start_is_goal(self):
        """Test when start state is already the goal"""
        matrix = [
            [None, 1.0],  # 0 -> 1
            [None, None]  # 1 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={0},  # Start state is also goal
            start_state=0
        )
        
        path, stats = bfs(graph)
        self.assertEqual(path, [0])
        self.assertEqual(stats["path_length"], 1)
        self.assertEqual(stats["states_expanded"], 0)  # No expansion needed
        
        path, stats = dfs(graph)
        self.assertEqual(path, [0])
        self.assertEqual(stats["path_length"], 1)
        self.assertEqual(stats["states_expanded"], 0)  # No expansion needed
        
    def test_multiple_paths_bfs_optimal(self):
        """Test BFS finds optimal path when multiple paths exist"""
        # Create diamond graph: 0 -> {1,2} -> 3
        matrix = [
            [None, 1.0, 1.0, None],  # 0 -> 1, 0 -> 2
            [None, None, None, 1.0],  # 1 -> 3
            [None, None, None, 1.0],  # 2 -> 3
            [None, None, None, None]  # 3 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={3},
            start_state=0
        )
        
        path, stats = bfs(graph)
        self.assertEqual(stats["path_length"], 3)  # Shortest path length
        self.assertTrue(path in [[0, 1, 3], [0, 2, 3]])  # Either path is valid
        
    def test_frontier_size_tracking(self):
        """Test max frontier size is tracked correctly"""
        # Create graph where frontier grows: 0 -> {1,2,3}
        matrix = [
            [None, 1.0, 1.0, 1.0],  # 0 -> 1, 0 -> 2, 0 -> 3
            [None, None, None, None],  # 1 has no outgoing edges
            [None, None, None, None],  # 2 has no outgoing edges
            [None, None, None, None]   # 3 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={3},
            start_state=0
        )
        
        _, stats = bfs(graph)
        self.assertGreaterEqual(stats["max_frontier_size"], 3)
        
    def test_cycle_handling(self):
        """Test algorithms handle cycles correctly"""
        # Create graph with cycle: 0 -> {1,3}, 1 -> 2, 2 -> 1
        matrix = [
            [None, 1.0, None, 1.0],  # 0 -> 1, 0 -> 3
            [None, None, 1.0, None],  # 1 -> 2
            [None, 1.0, None, None],  # 2 -> 1 (creates cycle)
            [None, None, None, None]  # 3 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={3},
            start_state=0
        )
        
        path, stats = bfs(graph)
        self.assertEqual(path, [0, 3])
        self.assertEqual(stats["path_length"], 2)
        
    def test_large_graph_performance(self):
        """Test on larger graph to check performance"""
        # Create chain: 0 -> 1 -> 2 -> ... -> 10
        size = 11
        matrix = []
        for i in range(size):
            row: List[Optional[float]] = [None] * size  # Allow None or float
            if i < size - 1:
                row[i + 1] = 1.0  # Connect to next state
            matrix.append(row)
            
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={10},
            start_state=0
        )
        
        path, stats = bfs(graph)
        self.assertEqual(stats["path_length"], 11)
        self.assertEqual(stats["states_expanded"], 10)
        
    def test_stats_consistency(self):
        """Test that stats are consistent across runs"""
        # Diamond graph
        matrix = [
            [None, 1.0, 1.0, None],  # 0 -> 1, 0 -> 2
            [None, None, None, 1.0],  # 1 -> 3
            [None, None, None, 1.0],  # 2 -> 3
            [None, None, None, None]  # 3 has no outgoing edges
        ]
        
        graph = DirectedGraph(
            matrix=matrix,
            goal_indices={3},
            start_state=0
        )
        
        # Run multiple times to ensure consistency
        for _ in range(5):
            _, stats1 = bfs(graph)
            _, stats2 = bfs(graph)
            self.assertEqual(stats1, stats2)

    def test_maze_small(self):
        """Test BFS and DFS on small mazes"""
        from maze import Maze
        
        # Test 1x1 maze
        single_cell_maze = Maze(1, 1)
        self._check_maze(bfs, single_cell_maze, 1)
        self._check_maze(dfs, single_cell_maze, 1)
        
        # Test 2x2 maze
        two_by_two_maze = Maze(2, 2)
        self._check_maze(bfs, two_by_two_maze, 3)
        self._check_maze(dfs, two_by_two_maze, 3)

   
        
if __name__ == "__main__":
    unittest.main()