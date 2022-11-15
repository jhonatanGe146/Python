"""Escribe un programa que pida tres números y que escriba si son los tres
iguales, si hay dos iguales o si son los tres distintos"""


def equal (num1, num2, num3):
    if (num1 == num2 == num3):
        return ("Los tres números son iguales")
    elif (num1 == num2 != num3):
        return ("El número 1 y el número 2 son iguales")
    elif (num2 == num3 != num1):
        return ("el número 2 y el número 3 son iguales")
    elif (num1 == num3 != num2):
        return ("El número 1 y el número 3 son iguales")
    else: 
        return ("Todos los números son distintos")
num1 = float(input ("Ingrese el primer numero: "))
num2 = float (input ("Ingrese el segundo numero: "))
num3 = float (input ("Ingrese el tercer numero: "))     
print (equal(num1,num2,num3))