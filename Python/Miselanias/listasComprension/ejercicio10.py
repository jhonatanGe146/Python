"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Encuentre la desviación estandar"""

import random
rango=random.randint(10, 25)
lista=[round(random.random()*100) for i in range (rango)]
print(lista)
suma=0
for j in range (len(lista)):
    suma+=lista[j]
promedio=suma/len(lista)
sumat=0
for l in range (len(lista)):
    sumat+=(lista[l]-promedio)**2
divi=sumat/(len(lista)-1)
raiz=divi**0.5
print("La desviación estandar es: ",raiz)