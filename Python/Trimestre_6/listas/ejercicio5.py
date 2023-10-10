"""Ejercicio 5.
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor."""

import random

#? Ordenar con función
def Ordenar_Num():
    valores= []
    for i in range (10):
        valores.append(round (random.random()*100))
    print("Lista No Ordenada")
    print(valores)
    print()
    print("Lista Ordenada")
    print(sorted(valores))
                
Ordenar_Num()