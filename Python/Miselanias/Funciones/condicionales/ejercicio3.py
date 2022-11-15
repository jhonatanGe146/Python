"""Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa"""

def digits (numero):
    if (numero <= 9):
        return ("El número tiene 1 cifra")
    elif (numero <= 99):
        return ("El número tiene 2 cifras")
    elif (numero <= 999):
        return ("El número tiene 3 cifras")
    elif (numero <= 9999):
        return ("El número tiene 4 cifras")
    else:
        return ("El número a excedido los limites")
numero = float (input (" Ingresa un número entero positivo: "))
print (digits(numero))