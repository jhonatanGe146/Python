"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
De cada elemento de la lista diga si el elemento está por encima del promedio, debajo del promedio o es igual al promedio de todos los números."""


def promedio (lista):
    import random
    suma=0
    rango=random.randint(10,25)
    for i in range (rango):
        lista.append(round(random.random()*100))
        suma+=lista[i]
    print ("La lista esta conformada asi:\n",lista)
    promedio=round(suma/len(lista))
    print("El promedio de la lista es= ",promedio)
    for j in range (len(lista)):
        if lista[j] == promedio:
            print ("El número", lista[j], "es igual al promedio")
        elif lista[j] > promedio:
            print ("El valor",lista[j], "está por encima de promedio")
        else:
            print ("El valor", lista[j], "está por debajo de promedio")
lista=[]
print(promedio(lista))