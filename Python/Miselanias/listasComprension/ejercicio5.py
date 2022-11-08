"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que posicion esta.
si no está agréguelo al fial de la lista"""

import random
rango= random.randint(10,25)
num=int(input("Ingresa el valor a buscar en la lista: "))
lista=[round(random.random()*100) for i in range(rango)]
cont=0

print(lista)
if num in lista[:]:
     for j in range(len(lista)):
        if num==lista[j]:
            cont+=1
            print("El número",num,"esta en la posición",j,",",cont,"veces")
else:        
    print("El valor", num, "no esta en la lista. se agregara de inmediato")
    lista.append(num)
print(lista)
print(len(lista))