"""Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
valor del medio es 11. No use operadores lógicos"""

num1 = float (input ("Digitar el primer número: "))
num2 = float (input ("Digitar el segundo número: "))
num3 = float (input ("Digitar el tercer número: "))

if num1 > num2:
    if num1 < num3:
        print (num1)
if num2 >num1:
    if num2 < num3:
        print (num2)
if num3 > num1:
    if num3 < num2:
        print(num3)
if num2 < num1:
    if num2 > num3:
        print (num2)
if num1 < num2:
    if num1 > num3:
        print (num1)
if  num3 < num1:
    if num3 > num2:
        print (num3)
