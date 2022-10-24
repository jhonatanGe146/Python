"""Determinar los divisores de un número introducido por
teclado"""

num=int (input("Digita un número para determinar sus divisores : "))
divisor=num+1
for i in range (1,divisor):
    resul= num%i
    if resul == 0:
        print (i, "Es divisor de ", num)