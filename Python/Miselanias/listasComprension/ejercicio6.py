""" LLene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe ingresar el usuario.
Minimo debe tener 5 elementos maximo 20"""
import random
serie=[0,1]
rango=(round(random.randint(10,25)))
for i in range (2,rango):
    serie.append(serie[i-1]+serie[i-2])
print(serie)
print(len(serie))

serie=[0,1]
rango=int(input("Ingrese el rango: "))
if rango>=5 and rango<=25:
    for i in range(2,rango):
        serie.append(serie[i-1]+serie[i-2])
else:
    print("!Error¡, no esta dentro del rango")
print(serie)
print(len(serie))