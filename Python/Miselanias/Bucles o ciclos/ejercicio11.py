""" Solicitar 2 números al usuario e imprimir el cociente y el
residuo del mayor en el menor sin utilizar la división ni el mod."""

y=int(input("Ingresa un número: "))
x=int (input("Ingresa un número: "))
contador=0
if y > x:
    dividendo=y
    while dividendo !=0:
        dividendo-=x
        contador+=1
else:
    dividendo=x
    while dividendo !=0:
        dividendo-=y
        contador+=1
print ("El cociente es: ",contador)
print("El residuo es: ",dividendo)