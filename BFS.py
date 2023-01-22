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

    
    
    def actions(self, state):
        return state.Movments()
    
    
    def result(self, state, action):
        action.Padre = state

    
    def goalTest(self, state):    
        return state in self.goal

    
    def step_cost(self, state, action, state2):
        return self.graph.get_step_cost(state, action)

    
    def path_cost(self, path):
        cost = 0
        for i in range(len(path)-1):
            cost += self.step_cost(path[i], path[i+1])
        return cost
    
    def breadth_first(self):
        visited_nodes=[]
        queue = Queue()
        queue.enqueue(self.start)
        visited_nodes.append(self.start)
                
        while queue.size > 0:
        #for i in range(5):
            
            current_node = queue.dequeue()
            childrens = self.actions(current_node)
            
            
            if self.goalTest(current_node):
                return current_node
            
            for child in childrens:
                if child and not (child in visited_nodes):                    
                    visited_nodes.append(child)
                    queue.enqueue(child)
                    self.result(current_node, child)
            
