"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Sume los pares y saque el promedio de los impares"""

import random
rango= random.randint(10,25)
lista=[]
pares=[]
impares=[]
suma_par=0
suma_impar=0
for i in range (rango):
    lista.append(round(random.random()*100))
    res=lista[i]%2
    if res == 0:
        pares.append(lista[i])
        suma_par+=lista[i]
    else:
        impares.append(lista[i])
        suma_impar+=lista[i]
promedio= suma_impar / (len(impares))
print("La lista es\n",lista)
print()
print("Los números pares son:\n",pares)
print("Su suma es= ",suma_par)
print()
print("Los números impares son:\n", impares)
print("Su promedio es= ",promedio)

