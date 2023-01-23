from Graph_Search import Graph_Search

        
class AStarDos(Graph_Search):
    def __init__(self, graph, start, goal):
        super().__init__(graph, start, goal)
        
        self.costo = [0 for x in range(0,len(goal))]
        self.final = None
        
    
    def actions(self, state):
        return state.Movments()
    
    
    def result(self, state, action):
        action.Padre = state

    
    def goalTest(self, state):    
        return state in self.goal

    
    def step_cost(self, state, action=0, state2=0):
        pass
                     
    
    def path_cost(self, path):
        self.costo = [0 for x in range(0,len(self.goal))]
        
        if  path == None:  
            return 10000000
        
        cont=-1
        

        for meta in self.goal:
            cont+=1

            y_meta = meta.position[0]
            x_meta = meta.position[1]
            y_inicio = path.position[0]
            x_inicio = path.position[1]
            
            self.costo[cont] = abs(y_meta - y_inicio) + abs(x_meta - x_inicio)
            

        return (min(self.costo))

    
    def astar(self, start, visited_nodes=[]):
        visited_nodes.append(start)
        current_node = start

        if self.goalTest(current_node):
            self.final = current_node
            return self.final
            
        else:
            childrens = self.actions(current_node)
            if self.final is None:
                Conteo_costos =[]
                
                for child in childrens:
                    if child:
                        arreglo_result =self.path_cost(child)
                        Conteo_costos.append(arreglo_result)
                    
                    else:
                        Conteo_costos.append(10000000)
                        
                

                while len(Conteo_costos) > 0:
                    
                    indice = Conteo_costos.index(min(Conteo_costos))    
                    next_nod = childrens[indice]
                    Conteo_costos.pop(indice)
                    childrens.pop(indice)
                    
                    
                    if  next_nod and not (next_nod in visited_nodes):
                        self.result(current_node, next_nod)                    
                        self.astar(next_nod, visited_nodes)

        return self.final