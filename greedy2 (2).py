import random
import numpy as np
crater_map = np.load('/Users/gianmarcoinnocenti/Desktop/agentesinteligentes/crater_map.npy')
nr, nc = crater_map.shape
print(nc,nr)
scale=10
#----------------------------
# Funcion Objetivo
def objective_function(r,c):

    x=crater_map[r][c]
    return x

# Algoritmo Greedy
def Greedy(objective_function,r,c):
    #renglon inicial
    current_solutionr =r
    #columna inicial
    current_solutionc=c
    #valor de altura original
    current_best = objective_function(current_solutionr,current_solutionc)
    # probar en vecinos
    pos=[-1, 0, 1]
    direction=[]

    for i in pos:
        for j in pos:
        # ver si la altura del vecino es aceptable
            gradient = objective_function(current_solutionr +i,current_solutionc+j) - current_best 
            if gradient>-2 and gradient<0:
                
        #agregar todas las posiciones validas a una lista
                direction.append([crater_map[current_solutionr+i][current_solutionc+j],current_solutionr+i,current_solutionc+j])
    #encontrar que coordenadas es la menor y extraerla
    smallest_list = min(direction, key=lambda x: x[0])
    #r,c vecino optimo
    direction=list(smallest_list[1:3])
    #crear vecino
    candidate_solution=direction
    #encontrar valor altura del vecino
    candidate_best = objective_function(candidate_solution[0],candidate_solution[1])
        # comparar altura de vecino con actual
    if candidate_best < current_best:
            current_solution = candidate_solution
            current_best = candidate_best
           #extraer renglon y columna nueva
            r=current_solution[0]
            c=current_solution[1]
            
    # Return the current best solution
    return r,c

#Iniciar algoritmo
x=2923
y=4972

r=nr-round(y/scale)
c=round(x/scale)

state=(r,c)

print("Altura Inicial:",crater_map[r][c])
best_solution = Greedy(objective_function,r,c)
r,c=best_solution
print("Altura Final: Renglones = {}, f(x) = {}".format(best_solution, objective_function(r,c)))

