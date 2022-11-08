"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Encuentre la suma y el promedio de los números de la lista"""

import random
rango=random.randint(10, 25)
lista=[round(random.random()*100)for i in range (rango)]
suma=0
print(lista)
for p in range(len(lista)):
    suma+=lista[p]
promedio=suma/len(lista)
print("La suma de la lista es= ", suma)
print("El promedio de la lista es= ",promedio)