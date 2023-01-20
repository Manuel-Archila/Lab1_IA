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
    def search(self):
        pass

    def get_path(self):
        return self.path

    def get_visited(self):
        return self.visited

    def get_frontier(self):
        return self.frontier  