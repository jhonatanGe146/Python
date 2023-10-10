"""Ejercicio 10.
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
Carga la tabla con valores numéricos enteros.
Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla."""
import random

def lista_dosD():
    tabla =[]
    for i in range (5):
        fila=[]
        for j in range (5):
            fila.append(round(random.random()*100))
        tabla.append(fila)
        

        
        
    print("Tabla 5x5")
    for i in tabla:
        x=0
        suma_fila = sum (i)
        
        for j in i:
            print(f"{j} ", end='\t')
        print(f"Suma = {suma_fila}")

   # Calcular y mostrar la suma de cada columna individualmente
    for j in range(5):
        suma_columna = 0
        for i in range(5):
            suma_columna += tabla[i][j]
        print(f"Suma de la columna {j + 1}: {suma_columna}")

    
        
    
lista_dosD()
