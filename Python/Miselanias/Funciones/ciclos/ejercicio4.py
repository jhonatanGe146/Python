""" Generar un número (generarlo random) y adivinarlo dicienfdo si en cada intento es mayor o menor que el número. Decir cuantos números 
ingreso antes de adivinarlo"""

import random
def juego(num):
    numero_secreto=(round(random.random()*100))
    conta=1 
    while num!= numero_secreto:
        if num>numero_secreto:
            print("El número es menor ¡Sigue intentando!")
        else:
            print("El número es mayor ¡Sigue intentando!")
        num=int(input("ingresa un número: "))
        conta+=1
    print("Adivinaste el número en",conta,"intentos")

num= int(input("Puedes adivinar el número secreto de 1-100\n ingresa un número: "))
juego(num)