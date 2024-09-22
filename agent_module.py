
from __future__ import annotations
from collections import deque
from turtle import bgcolor


Direction = tuple[int, int]

Directions = list[Direction]

UP: Direction = (0, -1)
DOWN: Direction = (0, 1)
RIGHT: Direction = (1, 0)
LEFT: Direction = (-1, 0)

COLOR_VISITED = '\033[92m'
COLOR_PATH = '\033[91m'
COLOR_QUEUE = '\033[94m'
COLOR_NORM = '\033[0m'


directions: Directions = [UP, DOWN, LEFT, RIGHT]


class Position:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord= y_coord
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Position):
            return (self.x_coord == other.x_coord) and (self.y_coord == other.y_coord)
        return False
    
    def __str__(self) -> str:
        return f"x:{self.x_coord}, y:{self.y_coord}"
    
    def __hash__(self) -> int:
        return hash((self.x_coord, self.y_coord))
    
    def __iter__(self):
        return iter(self.x_coord, self.y_coord)

class Dimensions:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Grid:
    def __init__(self, dimensions: Dimensions, start: Position, goal: Position, walls: list[Position]):
        self.dimensions = dimensions
        self.start = start
        assert start not in walls, "Start cannot be on a wall."
        assert 0 <= self.start.x_coord <= (dimensions.width - 1)
        assert 0 <= self.start.y_coord <= (dimensions.height - 1)
        self.goal = goal
        assert goal not in walls, "Goal cannot be on a wall."
        assert 0 <= self.goal.x_coord <= (dimensions.width - 1)
        assert 0 <= self.goal.y_coord <= (dimensions.height - 1)
        assert start != goal
        self.agents: list[BfsAgent] = []
        self.walls: list[Position] = walls
        self.finished = False
    
    def add_agent(self, agent: BfsAgent):
        self.agents.append(agent)
        agent.set_grid(self)

    def move_agents(self):
        for agent in self.agents:
            agent.next()
            
    def render(self)->None:
        padding = 2
        gap_str = ' '*padding
        print()
        for row in range(self.dimensions.height):
            for column in range(self.dimensions.width):
                curr_pos = Position(column, row)
                agent_at_start = False
                for agent in self.agents:
                    color = COLOR_NORM
                    if curr_pos in agent.visited:
                        color = COLOR_VISITED
                    else:
                        color = COLOR_NORM
                    if agent.position == curr_pos:
                        print(f'A', end=gap_str)
                        if agent.position == self.start:
                            agent_at_start = True
                    elif self.start == curr_pos and not agent_at_start:
                        print('S', end=gap_str)
                    elif self.goal == curr_pos:
                        print('G', end=gap_str)
                    elif curr_pos in self.walls:
                        print('#', end=gap_str)
                    else:
                        if curr_pos in agent.queue:
                            color = COLOR_QUEUE
                        if curr_pos in agent.shortest_path:
                            color = COLOR_PATH
                        print(f'{color}.{COLOR_NORM}', end=gap_str)
            print()
        print()

    

def translate(position: Position, direction: Direction)->Position:
    return Position(position.x_coord + direction[0], position.y_coord + direction[1])

class BfsAgent:

    def __init__(self) -> None:
        self.visited: list[Position] = []
        self.queue: deque[Position] = deque()
        self.parents: dict[Position, Position]= {}
        self.shortest_path: list[Position] = []

    def set_grid(self, grid: Grid):
        self.grid = grid
        self.position = grid.start

    def _mark_visited(self, pos: Position):
        self.visited.append(pos)

    def _is_visited(self, pos: Position):
        return pos in self.visited
    
    def _in_queue(self, pos: Position) -> bool:
        return pos in self.queue

    def _enqueue_cell(self, pos: Position):
        self.queue.append(pos)

    def next(self):
        self._add_neighbors()
        self.position = self.queue.popleft()
        self._mark_visited(self.position)
        if self.position == self.grid.goal:
            self._shortest_path()
            self.grid.finished = True
    
    def _add_neighbors(self)->None:
        for direction in directions:
            neighbor_pos: Position = translate(self.position, direction)
            if (not self._is_visited(neighbor_pos) and not self._in_queue(neighbor_pos)) and (self._is_valid_pos(neighbor_pos)):
                self._enqueue_cell(neighbor_pos)
                self.parents[neighbor_pos] = self.position

    def _is_valid_pos(self, position: Position)->bool:
        valid_x = 0 <= position.x_coord <= (self.grid.dimensions.width - 1)
        valid_y = 0 <= position.y_coord <= (self.grid.dimensions.height -1)
        not_wall = position not in self.grid.walls
        return valid_x and valid_y and not_wall
    
    def _shortest_path(self):
            finished = False
            while not finished:
                self.shortest_path.append(self.parents[self.position])
                self.position = self.parents[self.position]
                if self.position == self.grid.start:
                    finished = True
                    print('SHORTEST PATH: ')
                    for pos in self.shortest_path:
                        print(pos)

def user_input_grid()->Grid:
    """Get input via command line for grid dimensions, start position and goal position."""
    width = int(input('Enter grid width: '))
    height = int(input('Enter grid height: '))
    dimensions = Dimensions(width, height)
    start_x = int(input('Enter starting x coordinate: '))
    start_y = int(input('Enter starting y coordinate: '))
    start = Position(start_x, start_y)
    goal_x = int(input('Enter goal x coordinate: '))
    goal_y = int(input('Enter goal y coordinate: '))
    goal = Position(goal_x, goal_y)
    done_walls = False
    walls: list[Position] = []
    while not done_walls:
        done_walls_input = input('Enter walls? (any key for yes, or "N" for no): ')
        done_walls = done_walls_input.lower() == 'n'
        if done_walls: 
            break
        wall_count = 1
        wall_x = int(input(f'Enter wall {wall_count} x coordinate'))
        assert 0 <= wall_x < width
        wall_y = int(input(f'Enter wall {wall_count} y coordinate'))
        assert 0 <= wall_y < height
        wall = Position(wall_x, wall_y)
        walls.append(wall)
    return Grid(dimensions, start, goal, walls)

def generate_random()->tuple[Dimensions, Position, Position]:
    raise NotImplementedError

def hard_coded_grid()->Grid:
    walls = [
        Position(5,6), 
        Position(6,7), 
        Position(6,7), 
        Position(6,7), 
        Position(8,9),
        Position(6,4), 
        ]
    return Grid(Dimensions(20, 20), Position(2,3), Position(7,8), walls)
