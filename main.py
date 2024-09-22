
# Introduction
# This assignment introduces students to the implementation of Artificial Intelligence
# search algorithms using Python.
# Objectives
# Implementing a grid-based search algorithm in Python using functions, arrays, and
# 2D arrays. The assignment focuses on building a modular and structured program
# through step-by-step process.

import time
import agent_module
import os

def print_stats(agent: agent_module.BfsAgent)->None:
            print('AGENT POSITION: ', agent.position)
            print('visited: ', len(set(agent.visited)), f' (marked in {agent_module.COLOR_VISITED}green{agent_module.COLOR_NORM})')
            print('queue: ', len(set(agent.queue)), f' (marked  in {agent_module.COLOR_QUEUE}blue{agent_module.COLOR_NORM})')
            print('optimal path steps: ', len((agent.shortest_path)), f' (marked  in {agent_module.COLOR_PATH}red{agent_module.COLOR_NORM})')


if __name__ == '__main__':

    grid = agent_module.hard_coded_grid()
    print(f"Welcome to Will Lapinel's {agent_module.COLOR_VISITED}BFS Simulator!{agent_module.COLOR_NORM}")
    custom = input('Customize settings? "Y" (any other key to use default settings)? ')
    if custom.lower() == 'y':
         grid = agent_module.user_input_grid()
    agent = agent_module.BfsAgent()
    grid.add_agent(agent)
    max_iterations=1000
    print("\033[?25l", end="")
    for i in range(max_iterations):
        print("\033[H", end="")
        if i != max_iterations - 1:
            if os.name == 'nt':
                os.system('cls')
            # For Mac and Linux
            else:
                os.system('clear')
        if grid.finished:
            print_stats(agent)
            grid.render()
            time.sleep(2)
            print("\033[?25h", end="")
            exit() 
        grid.move_agents()
        print_stats(agent)
        grid.render()
        time.sleep(0.2)
    print('Max iterations reached.')






