import pandas as pd
import numpy as np

#Lectura de datos
dataset="C:/Users/ggalv/Google Drive/Respaldo/Ayudantia Logistica/TSP_Greedy/Datos_TSP.txt"
archivo= pd.read_csv(dataset,delim_whitespace=True,header=None)
# print(type(archivo))


#CONSTRUIR MATRIZ DISTANCIAS
dist=[]
for i in range(280):
	a=archivo.iloc[i]
	a=np.array(a)
	a=np.delete(a,0)
	for j in range(280):
		if i!=j:
			b=archivo.iloc[j]
			b=np.array(b)
			b=np.delete(b,0)
			dist.append(int(np.linalg.norm(a-b)))
		elif i==j:
			dist.append(99999)

distancias=np.array(dist)
distancias=distancias.reshape(280,280)
# print(distancias)			

#VECTOR DE NODOS POR VISITAR
nodos_por_visitar=[]
for i in range(280):
	nodos_por_visitar.append(i)


#HEURISTICA
FO=0
inicio=0
nodos_por_visitar.remove(inicio)
nodos_visitados=[]
nodos_visitados.append(inicio)
nodo_actual=np.argmin(distancias[inicio])
distancia=np.min(distancias[inicio])
FO+=distancia

while len(nodos_por_visitar)!=1:
	nodos_por_visitar.remove(nodo_actual)
	for i in range(len(nodos_visitados)):
		distancias[nodo_actual][nodos_visitados[i]]=999999
	nodos_visitados.append(nodo_actual)
	distancia=np.min(distancias[nodo_actual])
	FO+=distancia
	nodo_actual=np.argmin(distancias[nodo_actual])

nodos_visitados.append(nodo_actual)
FO+=distancias[nodo_actual][0]
nodos_visitados.append(0)

print("distancia recorrida= ", FO)
print("Ruta= ", nodos_visitados)		
