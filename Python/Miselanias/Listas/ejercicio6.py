""" LLene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe ingresar el usuario.
Minimo debe tener 5 elementos maximo 20"""
serie=[]
repe=True

while repe:
    cantidad=int(input("Ingresa la cantidad de elementos(5-20) que quieres visualizar.\n de la serie de Fibonacci: "))
    if cantidad >= 5 and cantidad <=20:
        repe=False
    else:
        print("La cantidad debe estar en el rango de 5 a 20")
x=0
y=1
z=1
for i in range(cantidad):
    z=x+y
    x=y
    y=z
    serie.append(z)
print("La serie de Fibonacci hasta la cantidad desea es: ",serie)