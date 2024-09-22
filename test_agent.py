
import agent_module


def test_bfs_agent():
    grid = agent_module.hard_coded_grid()
    agent = agent_module.BfsAgent()
    grid.add_agent(agent)
    for i in range(100):
        print(agent.position)
        print(agent.visited)
        assert len(agent.visited) == i
        grid.move_agents()
        grid.render()



