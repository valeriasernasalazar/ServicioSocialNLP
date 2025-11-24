import numpy as np
mars_map = np.load(r'C:\Users\Usuario\Downloads\mars_map.npy')
nr, nc = mars_map.shape
import time

start_time = time.time()

# your code here



escala=10.0174
r=nr-round(6450/escala)
c=round(3000/escala)
print(r)
print(c)
print(mars_map[r][c])
print("intento 10")

from simpleai.search import SearchProblem, depth_first, breadth_first, astar, uniform_cost
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer
class CleanUp(SearchProblem):
    def __init__(self, initialstate):
        """ Constructor encargado de inicializar el problema de CleanUp. 
            initialstate: El estado inicial del tablero.
        """
        SearchProblem.__init__(self, initialstate)
        self.goal_state = (9000,5000)
    
    def actions(self, state):
        """ Regresa una lista de las actions posibles de ser realizadas, de acuerdo con nuestro estado.
        state: el estado evaluado.
        """
        #Se obtiene la posición en la que se encuentra el agente
        r= nr-round(state[0]/escala)
        c= round(state[1]/escala)
        # Acciones posibles de realizar de parte del agente
        actions = []
        pos = [1,0]
        for i in pos:
             for j in pos:
                if i!=j:
                    rnew=nr-round((state[0])/escala)+i
                    cnew=round((state[1])/escala)+j
                    #print(rnew,cnew)
                    #print("hola")
                    #Se calcula la diferencia de alturas entre el estado actual y el nuevo estado.
                    #print('hola',rnew,cnew)
                    #print('adios',r,c)
                    if abs(rnew) < nr and ((cnew) < nc and cnew >0):
                        if abs(r) < nr  and c >-nc:
                        
                            if (mars_map[rnew][cnew]-mars_map[r][c]) < 0.25:
                                #print(mars_map[rnew][cnew]-mars_map[r][c])
                                #Se añade a la matriz de posibles acciones
                                actions.append((i*10,j*10))
        #print(actions)
        return actions
    
    def result(self, state, action):
        new_state = list(state)
        new_state[0] = state[0]+action[0]
        new_state[1] = state[1]+action[1]
        print(new_state)
        print(action)
        return tuple(new_state)
    
    def heuristic(self,state):
        rfin=nr-round(7600/escala)
        cfin=round(9000/escala)
        #print(state)
        heur=abs(rfin-state[0]/escala)+abs(cfin-state[1]/escala)
        #print('hreutistica:',abs(rfin-state[0])+abs(cfin-state[1]))
        #heur=(rfin**2+cfin**2)**0.5-(state[0]**2+state[1]**2)**0.5
        return heur
    
    def is_goal(self, state):
        """Analiza si el estado actual es el meta.
        """
        found_goal = state == self.goal_state
        return  found_goal
    
    def cost(self, state, action, state2):
        return 1
    
def display(result):
        if result is not None:
            for i, (action, state) in enumerate(result.path()):
                if action == None:
                    print('Inicio')
                elif i == len(result.path()) - 1:
                    print(i,'Después', action)
                    print('Meta lograda con un costo de', result.cost)
                else:
                    print(i,'- ', action)

                print('  ', state)
        else:
            print('Mala configuración del problema')


state1 = (6400,2850)

#result = depth_first(CleanUp(state1), graph_search=True)
#result = breadth_first(CleanUp(state1), graph_search=True)
#result = astar(CleanUp(state1), graph_search=True)
result = uniform_cost(CleanUp(state1), graph_search=True)
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('Despues de moverse', action, ' metros. Goal achieved!')
        print('Meta lograda con un costo de', result.cost)
    else:
        print('Despues de moverse', action, 'metros en la coordenada real')

    for item in state:
        print("{:2}".format(item), end = " ")
    print()

end_time = time.time()
elapsed_time = end_time - start_time

print("Elapsed time: ", elapsed_time, " seconds")