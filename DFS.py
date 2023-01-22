from Graph_Search import Graph_Search

        
class DFS(Graph_Search):
    def __init__(self, graph, start, goal):
        super().__init__(graph, start, goal)
        self.final = None

    
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

    
    def deep_first(self, start, visited_nodes=[]):
        visited_nodes.append(start)
        current_node = start

        if self.goalTest(current_node):
            self.final = current_node
            return self.final
            
        else:
            childrens = self.actions(current_node)
            if self.final is None:
                for child in childrens:
                    if child and not (child in visited_nodes):
                        self.result(current_node, child)                    
                        self.deep_first(child, visited_nodes)

        return self.final




        

                
            
