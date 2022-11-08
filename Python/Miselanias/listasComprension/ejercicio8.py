"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Encuentre la moda de los números de la lista"""

import random
rango=random.randint(10,25)
lista=[round(random.random()*100) for i in range(rango)]
moda=[]

for j in range (len(lista)):
    for k in range (len(lista)):
        if j != k:
            if lista[k]==lista[j] and lista[k] not in moda:
                moda.append(lista[j])
print("La lista es:\n",lista)
print("La moda es=",moda)