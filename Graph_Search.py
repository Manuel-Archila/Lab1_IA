from abc import ABC, abstractmethod

class Graph_Search(ABC):
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.path = []
        self.visited = []
        self.frontier = []
        self.frontier.append(start)
        self.visited.append(start)

    

    @abstractmethod
    def actions(self, state):
        return self.graph.get_actions(state)
    
    @abstractmethod
    def result(self, state, action):
        return self.graph.get_result(state, action)

    @abstractmethod
    def goalTest(self, state):
        return state == self.goal

    @abstractmethod
    def step_cost(self, state, action, state2):
        return self.graph.get_step_cost(state, action)

    @abstractmethod
    def path_cost(self, path):
        cost = 0
        for i in range(len(path)-1):
            cost += self.step_cost(path[i], path[i+1])
        return cost

