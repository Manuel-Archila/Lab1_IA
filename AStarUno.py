from Graph_Search import Graph_Search

        
class AStarUno(Graph_Search):
    def __init__(self, graph, start, goal):
        super().__init__(graph, start, goal)
        
        self.costo = [0 for x in range(0,len(goal))]
        self.blancas = [0 for x in range(0,len(goal))]
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
        self.blancas = [0 for x in range(0,len(self.goal))]
        if  path == None:  
            return 10000000
        
        cont=-1
        cont2=-1

        for meta in self.goal:
            cont+=1
            cont2+=1
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
                elif self.graph[y_inicio][x_inicio] == 1:
                    self.blancas[cont2] += 1
                
                    
            while x_inicio != x_meta:
                if  x_inicio<x_meta:
                    x_inicio += 1
                else:
                    x_inicio -= 1
                #print(self.graph[y_inicio][x_inicio],end=" ")
                if self.graph[y_inicio][x_inicio] == 0:
                    self.costo[cont] += 1
                elif self.graph[y_inicio][x_inicio] == 1:
                    self.blancas[cont2] += 1

        return (min(self.costo), min(self.blancas))

    
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
                Conteo_blancas =[]
                
                for child in childrens:
                    if child:
                        arreglo_result =self.path_cost(child)
                        Conteo_costos.append(arreglo_result[0])
                        Conteo_blancas.append(arreglo_result[1])
                    
                    else:
                        Conteo_costos.append(10000000)
                        Conteo_blancas.append(10000000)
                        
                

                while len(Conteo_costos) > 0:
                #for i in range(1):
                    
                    indice = Conteo_costos.index(min(Conteo_costos))
                    #indice = Conteo_blancas.index(min(Conteo_blancas))
                    
                    if Conteo_costos.count(Conteo_costos[indice]) > 1:
                    #if Conteo_blancas.count(Conteo_blancas[indice]) > 1:
                        #indice = Conteo_costos.index(min(Conteo_costos))
                        indice = Conteo_blancas.index(min(Conteo_blancas))     
                    next_nod = childrens[indice]
                    Conteo_costos.pop(indice)
                    Conteo_blancas.pop(indice)
                    childrens.pop(indice)
                    
                    
                    if  next_nod and not (next_nod in visited_nodes):
                        self.result(current_node, next_nod)                    
                        self.astar(next_nod, visited_nodes)

        return self.final