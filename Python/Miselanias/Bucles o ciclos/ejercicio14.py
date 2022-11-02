"""Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número."""

from math import trunc


i=100
y=0
x=0
cubo=0
while i < 1000:
    a=trunc(i/100)
    b=trunc(i/10)-(a*10)
    c=i-(a*100+b*10)
    cubo=(a**3)+(b**3)+(c**3)
    if cubo ==i:
        print (i,cubo)
        i+=1
    else:
        i+=1