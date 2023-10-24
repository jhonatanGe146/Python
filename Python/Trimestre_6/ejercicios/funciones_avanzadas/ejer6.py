"""1.Función decoradora que recibe como parámetro funciones que trabajan sobre listas.
Estas funciones hacen operaciones estadísticas como suma, promedio,moda,mediana, varianza,
desviación estandar(Estas funciones uds las han desarrollado en el pasado).
La función decoradora analiza que todos los numeros de la lista estén en un rango de 0 a 100.
Si hay numeros fuera de ese rango no se ejecuta la función.
"""
import random


def trabajando_listas (fun):
    print('Inicia El Procesamiento De listas')
    def operando_listas(*args, **kwargs):
        try:
            for i, lista in enumerate(args):
                for valor in lista:
                    if valor < 0 or valor >100:
                        raise TypeError
                 
            fun(*args, **kwargs)
            print()
        except TypeError:
            print("La lista Contiene Valores fuera de rango")

    return operando_listas


lista1=([random.randint(0, 102) for _ in range(random.randint(1, 10))])
lista2=([random.randint(0, 102) for _ in range(random.randint(1, 10))])
lista3=([random.randint(0, 102) for _ in range(random.randint(1, 10))])
print(lista1)
print(lista2)
print(lista3)




#? Funcion para calcular la sumade una lista
@trabajando_listas
def calcular_suma(*args, **kwargs):
    for i in range (len(args)):
        lista=args[i]
        total_sum=0
        for num in lista:
            total_sum+=num
        print(f"La suma de la lista {i} es: {total_sum} ")
        
calcular_suma(lista1,lista2,lista3)



#? Funcion para calcular el promedio de una lista
@trabajando_listas
def calcular_promedio(*args, **kwargs):
    
    for i in range (len(args)):
        lista=args[i]
        total_sum=0
        cont=0
        for num in lista:
            total_sum+=num
            cont+=1
        total_prom= total_sum/cont
        print (f"El promedio de la lista {i} es: {total_prom} ")
calcular_promedio(lista1,lista2,lista3)


#? Funcion para calcular la moda de una lista
@trabajando_listas
def calcular_moda(*args):
    for i, lista in enumerate(args):
        moda = {} 
        max_frecuencia = 0
        valores_moda = []

        for valor in lista:
            if valor not in moda:
                moda[valor] = 1
            else:
                moda[valor] += 1

            if moda[valor] > max_frecuencia:
                max_frecuencia = moda[valor]

        if max_frecuencia == 1:
            print(f"La lista {i} no tiene moda, ya que ningún valor se repite.")
        else:
            for valor, frecuencia in moda.items():
                if frecuencia == max_frecuencia:
                    valores_moda.append(valor)

            print(f"La moda de la lista {i} es: {valores_moda}")

calcular_moda(lista1,lista2,lista3)

#? Funcion para calcular la mediana  de una lista
@trabajando_listas
def calcular_mediana(*args, **kwargs):
    for i, lista in enumerate(args):
        lista_ordenada = sorted(lista)
        n = len(lista_ordenada)

        if n % 2 == 1:  # Lista de longitud impar
            mediana = lista_ordenada[n // 2]
        else:  # Lista de longitud par
            mediana = (lista_ordenada[(n - 1) // 2] + lista_ordenada[n // 2]) / 2

        print(f"La mediana de la lista {i} es: {mediana}")
        
calcular_mediana(lista1,lista2,lista3)


#?Funcioon para calcular la desviacion estandar 
@trabajando_listas
def calcular_desviacionE(*args, **kwargs):
    try: 
        for i in range (len(args)):
            suma=0
            lista=args[i] 
            for j in lista:
                suma+=j
            promedio=suma/len(lista)
            sumat=0
            for l in range (len(lista)):
                sumat+=(lista[l]-promedio)**2
            divi=sumat/(len(lista)-1)
            raiz=divi**0.5
            print (f"La desviación estandar de la lista {i} es: {raiz}")
    except ZeroDivisionError:
        print("Ha ocurrido un fallo")

calcular_desviacionE(lista1,lista2,lista3)


#?Funcion para calcular la varianza
@trabajando_listas
def calcular_varianza(*args, **kwargs):
    for i, lista in enumerate(args):
        try:
            media = sum(lista) / len(lista)
            varianza = sum((x - media) ** 2 for x in lista) / (len(lista) - 1)
            print(f"La varianza de la lista {i} es: {varianza:.2f}")
        except ZeroDivisionError:
            print(f"Error: no se puede calcular la varianza.")

calcular_varianza(lista1,lista2,lista3)
