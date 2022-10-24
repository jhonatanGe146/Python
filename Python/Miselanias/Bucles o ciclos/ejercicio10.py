"""Algoritmo para hallar el m.c.d de dos números m y n por
el algoritmo de Euclides."""
m= int (input("Digita el primer número: "))
n= int (input ("Digita el segundo número: "))
while not (m==0):
    a=m
    b=n
    if m < 0:
        m=-a
        n=b
    if n < 0:
        m=am=-b
    else:
        m=b
        n = a%b
print (n)
