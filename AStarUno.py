from Graph_Search import Graph_Search

        
class AStarUno(Graph_Search):
    def __init__(self, graph, start, goal):
        super().__init__(graph, start, goal)
        self.costo = [0,0]
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
        if  path == None:  
            return 10000000
        
        cont=-1
        for meta in self.goal:
            cont+=1
            y_meta = meta.position[0]
            x_meta = meta.position[1]
            y_inicio = path.position[0]
            x_inicio = path.position[1]
            while y_inicio != y_meta:
                if  y_inicio<y_meta:
                    y_inicio += 1
                else:
                    y_inicio -= 1
                #print(self.graph[y_inicio][x_inicio],end=" ")
                if self.graph[y_inicio][x_inicio] == 0:
                    self.costo[cont] += 1
                    
            while x_inicio != x_meta:
                if  x_inicio<x_meta:
                    x_inicio += 1
                else:
                    x_inicio -= 1
                #print(self.graph[y_inicio][x_inicio],end=" ")
                if self.graph[y_inicio][x_inicio] == 0:
                    self.costo[cont] += 1
        return max(self.costo)

    
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
                        Conteo_costos.append(self.path_cost(child))
                    else:
                        Conteo_costos.append(10000000)
                
                while len(Conteo_costos) > 0:
                #for i in range(1):
                    
                    indice = Conteo_costos.index(min(Conteo_costos))                 
                    next_nod = childrens[indice]
                    #print("menor",min(Conteo_costos))
                    #print(Conteo_costos)
                    #print("indice",indice)
                    print("next_nod",next_nod)
                    Conteo_costos.pop(indice)
                    childrens.pop(indice)
                    
                    
                    if  next_nod and not (next_nod in visited_nodes):
                        self.result(current_node, next_nod)                    
                        self.astar(next_nod, visited_nodes)

        return self.final