"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
De cada elemento de la lista diga si el elemento está por encima del promedio, debajo del promedio o es igual al promedio de todos los números."""

import random
rango=random.randint(10,25)
lista=[round(random.random()*100) for i in range(rango)]
suma=0
for i in range (rango):
    suma+=lista[i]
print ("La lista esta conformada asi:\n",lista)
promedio=round(suma/len(lista))
print("El promedio de la lista es= ",promedio)
for j in range (len(lista)):
    if lista[j] == promedio:
        print ("El número", lista[j], "es igual al promedio")
    elif lista[j] > promedio:
        print("El valor",lista[j], "está por encima de promedio")
    else:
        print("El valor", lista[j], "está por debajo de promedio")