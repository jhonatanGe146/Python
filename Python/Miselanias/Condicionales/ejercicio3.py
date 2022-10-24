"""Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa"""

numero = float (input (" Ingresa un número entero positivo: "))
if (numero <= 9):
    print ("El número tiene 1 cifra")
elif (numero <= 99):
    print ("El número tiene 2 cifras")
elif (numero <= 999):
    print ("El número tiene 3 cifras")
elif (numero <= 9999):
    print ("El número tiene 4 cifras")
else:
    print ("El número a excedido los limites")