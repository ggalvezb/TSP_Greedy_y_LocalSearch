import utils
import importlib
import math
import random
import itertools
import numpy as np
import time

importlib.reload(utils)

# Corre para generar un problema aleatorio (desde la instancia berlin 52)
n, distances = utils.generate_euclid_tsp_problem(52, 0, 100)
# print("cantidad de nodos ", n)
# print("distancias= ", distances)

# Run this to use the supplied problem.
# n, distances, optimal_obj_value = utils.load_tsp_problem()

#Generacion de ruta inicial
r_initial = utils.random_initial_value(n, distances)

print("ruta incial= ",r_initial,"\n")
print("distancia ruta= ",utils.objective_tsp(r_initial, distances))



def neighbourhood(current_solution, objective_value):
    for _ in np.arange(100000):
        current_solution = current_solution[:]
    np.random.shuffle(current_solution)

    objective_value=utils.objective_tsp(list(current_solution), distances)    

    return(current_solution, objective_value)


def local_search(current_solution, distances):
    c_solution = current_solution
    c_objective = utils.objective_tsp(c_solution, distances)
    changed = True
    start=time.time()
    fin=0
    while changed:
        # print("fin= ",fin)
        if fin>=10:
            break
        neighbour_sequence, neighbour_objective = neighbourhood(c_solution, c_objective)
        if(neighbour_objective < c_objective):
            c_solution = neighbour_sequence
            c_objective = neighbour_objective
            changed = False
        end=time.time()
        fin=end-start  
          

    return c_solution, c_objective

n=0
ruta_final=r_initial
while n<10:
    ruta_final,distancia_final=local_search(ruta_final,distances)
    print("\n ruta final en iteracion",n,"= ", ruta_final)
    print("\n distancia final en iteracion",n,"= ", distancia_final)
    n+=1

print("\n ruta final= ", ruta_final)
print("\n distancia final", distancia_final)