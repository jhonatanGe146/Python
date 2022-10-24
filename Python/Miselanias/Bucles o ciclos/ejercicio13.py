"""Solicitar al usuario un número de hasta 9 dígitos e
imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576"""


num=int(input("Digitar número  hasta de 9 dígitos: "))
cifra=0
while num != 0:
    c=num%10
    cifra=cifra*10+c
    num=num//10
print (cifra)