"""Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
valor del medio es 11. No use operadores lógicos"""

        
def middle(num1,num2,num3):
    if num1 > num2 and num1<num3:
        return (num1)
    elif num2 >num1 and num2<num3:
        return(num2)
    elif num3 > num1 and num3<num2:
        return(num3)
    elif num2 < num1 and num2>num3:
        return(num2)
    elif num1 < num2 and num1>num3:
        return(num1)
    elif  num3 < num1 and num3>num2:
        return (num3)
x=int(input("Digete un numero: "))
y=int(input("Digete un numero: "))
z=int(input("Digete un numero: "))
print(middle(x,y,z))