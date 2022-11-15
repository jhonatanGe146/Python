"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Ordenae el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)"""

def ordenar(lista):
    import random
    rango=random.randint(10,25)
    for j in range(rango):
        lista.append(round(random.random()*100))
    print("Lista desrodenada:\n",lista)
    repe=True
    while repe:
        repe=False
        for i in range (len(lista)-1):
            if lista[i] > lista[i+1]:
                repe=True
                lista[i],lista[i+1]=lista[i+1],lista[i]       
    print("Lista ordenada de forma ascendente:\n", lista)
    repete=True
    while repete:
        repete=False
        for p in range(len(lista)-1):
            if lista[p] < lista[p+1]:
                repete=True
                lista[p],lista[p+1]=lista[p+1],lista[p] 
    print("La lista ordenad de forma descendente:\n", lista)
lista=[]
print(ordenar(lista))