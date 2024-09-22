# Homework Assignment 02

1. Define Grid Structure: Create a Python function to initialize a 2D array representing the grid. Allow
the user to input the size of the grid (rows and columns)

   - See `grid_agent.Grid` class

1. Display Grid Function: Implement a function to display the grid. Print the grid to ensure proper initialization.

   - See `grid_agent.Grid.render()`

1. User Input for Start and Goal:
Prompt the user to input the starting and goal positions on the grid. Ensure
the positions are valid (within grid boundaries).

   - See `grid_agent.user_input_grid()`

1. Basic Grid Display with Start and Goal:
Modify the display function to highlight the start and goal positions.

   - See `grid_agent.Grid.render()`.  `S` indicates Start and `G` indicates Goal in the grid display.

1. Define Search Algorithm Structure
Create a function for a simple Breadth-First search algorithm that takes the
grid, start, and goal positions as parameters.

   - See `grid_agent.BfsAgent` class

1. Initialize Search Algorithm
Initialize necessary data structures (e.g., queue, visited set, path array)
within the search algorithm function.

   - See `grid_agent.BfsAgent` class

1. Implement Search Algorithm Loop:
Build the main loop of the search algorithm to explore neighboring cells and
update the path array.

   - See `grid_agent.BfsAgent` class

1. Reconstruct Optimal Path Function:
Create a function to reconstruct the optimal path from the start to the goal
using the path array.

   - See `grid_agent.BfsAgent` class
   - `_shortest_path()` method adds parents of visited cells to shortest path list

1. Modify Grid Display for Path:
Adapt the grid display function to highlight the optimal path found by the
search algorithm.

   - See `grid_agent.Grid.render()` method. Path is indicated by red dots

1. User Output and Metrics:
Print the final grid with the optimal path marked. Display the length of the
optimal path and the total number of cells visited/explored.

   - See `main.py` in `print_stats()`

1. Additional Features (Optional):
Allow users to specify obstacles (e.g., walls) in the grid.

   - See `grid_agent.user_input_grid()`.  User can input walls as individual positions on grid.

1. Challenges I faced

   - I struggled for a while getting the agent to stop going to the same place twice and just going round in circles. It was a simple mistake, I forgot to have it check to make sure a cell wasn't already in the queue before adding it in my `_add_neighbors()` method. So it wouldn't add a cell that it already visited, but it would add cells that it had not yet visited but were already in the queue.
   - Surprisingly the most important part, `_shortest_path()` was pretty straightforward to write once I looked up that part of the algorithm.  It still amazes me that it works, and I'm not entirely sure I understand exactly *how* it works!
   - Overall, this was a very fun assignment. I really enjoyed the opportunity to implement a nice visual rendering of a search algorithm involving a grid world. There were a lot of "firsts" for me in this assignment, and it was quite edifying.
