"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Encuentre la mediana de los números de la lista."""

import random
rango=random.randint(10,25)
lista=[]

media=[]
for i in range (rango):
    lista.append(round(random.random()*100))
if len(lista)%2 > 0:
    media.append(lista[len(lista)//2])
else:
    media.append(lista[len(lista)//2])
    media.append(lista[(len(lista)//2)-1])
    suma=0
    for t in range(len(media)):
        suma+=media[t]
    media=suma//2
print(lista)
print("La mediana es=",media)
print(len(lista))