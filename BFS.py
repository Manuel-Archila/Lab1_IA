from Graph_Search import Graph_Search


class Queue():    
    def __init__(self):
        self.size = 0
        self.list = []

    def enqueue(self, data):
        self.list.append(data)
        self.size += 1

    def dequeue(self):
        try:
            self.size -= 1
            return self.list.pop(0)
        except Exception as error:
            print(f'{error} is not possible')     

    def xprint(self, index):
        print(self.list[index])

        

class BFS(Graph_Search):
    def __init__(self, graph, start, goal):
        super().__init__(graph, start, goal)

    def breadth_first(graph, root):

        queue = Queue()
        visited_nodes = list()
        queue.enqueue(root)
        visited_nodes.append(root)
        current_node = root
        
        while queue.size > 0:
            current_node = queue.dequeue()
            adj_nodes = graph[current_node]
            remaining_elements = sorted(set(adj_nodes) - set(visited_nodes))

            if len(remaining_elements) > 0:
                for element in remaining_elements:
                    visited_nodes.append(element)
                    queue.enqueue(element)
        
        return visited_nodes
