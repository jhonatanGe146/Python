"""1.Función decoradora que recibe como parámetro funciones que trabajan sobre listas.
Estas funciones hacen operaciones estadísticas como suma, promedio,moda,mediana, varianza,
desviación estandar(Estas funciones uds las han desarrollado en el pasado).
La función decoradora analiza que todos los numeros de la lista estén en un rango de 0 a 100.
Si hay numeros fuera de ese rango no se ejecuta la función.
"""
import random


def trabajando_listas ():
    print('')
    def operando_listas():
        pass

trabajando_listas()


#? Funcion para sumar valores de una lista
def sumar(*args, **kwargs):
    total_sum=0
    for lista in args:
        for num in lista:
            total_sum+=num
    print("La suma de la lista es= ", total_sum)

#? Funcion para sacar el promedio valores de una lista
def promedio(*args, **kwargs):
    total_sum=0
    cont=0
    for lista in args:
        for num in lista:
            total_sum+=num
            cont+=1
    total_prom= total_sum/cont
    print("El promedio de la suma de lista es= ", total_prom)

#? Funcion para sacar la moda de una lista
def moda (*args, **kwargs): 
    moda=[]
    for lista in args:
        for k in range (0, len(lista)):
            for j in range (1, len(lista)):
                if j != k:
                    if lista[k]==lista[j] and lista[k] not in moda:
                        moda.append(lista[j])
            
    print("La lista es:\n",args)
    print("La moda es=",moda)


l=([random.randint(0, 5) for _ in range(random.randint(1, 5))])
print(l)
sumar(l)
promedio(l)
moda(l)
