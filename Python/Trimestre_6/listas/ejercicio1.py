"""Ejercicio 1.
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y 
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
"""

import random

def Calcular_C():
    valores= []
    print (f"Valores   Cuadro   Cubo")
    for i in range (10):
        valores.append(random.randint(1,10))
    for j in valores:
        cuadro = j**2
        cubo = j**3
        print (f"  {j}        {cuadro}       {cubo} ")

Calcular_C()