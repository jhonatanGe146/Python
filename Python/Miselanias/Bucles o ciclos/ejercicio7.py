"""Encontrar un número natural n más pequeño tal que la suma
de los n primeros números naturales (1 + 2 + 3 + 4.....)
exceda de una cantidad (máximo) introducida por el teclado.
Es decir cuantos números de la serie de los naturales debo
sumar para superar el dato máximo."""

maximo=int (input("Digite el valor del dato maximo: "))
x = maximo+1
sum = 0
cont=0
while (sum < maximo):
    for i in range(0,x):
        sum+=1
        cont+=1
print ( "Para superar el número maximo(",maximo,") hay que sumar 1,",cont,"veces")