"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. Muestre cuales y cuantos son primos"""

import random
rango = random.randint(10,25)
lista=[]

contador_primo=0
contador_noprimo=0
for i in range(rango):
    lista.append(round(random.random()*100))
    contador=0
    for j in range(1,lista[i]+1):
        d=lista[i]%j
        if d==0:
            contador+=1
    if contador==2:
        print("El número",lista[i], "es primo")
        contador_primo+=1
    else:
        print("El número",lista[i], "no es primo")
        contador_noprimo+=1
print(lista)
print("La cantidad de números primos es=",contador_primo)
print("La cantidad de números no primos es=",contador_noprimo)