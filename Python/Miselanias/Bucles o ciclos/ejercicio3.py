"""Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este"""

num=int (input("Digita un número para saber si es perfecto o no : "))
perfe=0
for i in range (1,num):
    resul= num%i
    if resul == 0:
        perfe+=i
if perfe==num:
    print (num, "Es un número perfecto")
else:
    print(num, "No es un número perfecto")