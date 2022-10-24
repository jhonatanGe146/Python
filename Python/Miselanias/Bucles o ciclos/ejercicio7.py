"""Encontrar un número natural n más pequeño tal que la suma
de los n primeros números naturales (1 + 2 + 3 + 4.....)
exceda de una cantidad (máximo) introducida por el teclado.
Es decir cuantos números de la serie de los naturales debo
sumar para superar el dato máximo."""

maximo=int (input("Digite el valor del dato maximo: "))
x = 0
sum = 0
while (sum < maximo):
    x+=1
    sum=0
    for i in range(0,x+1):
        sum+=1
print (x, "Es el miníno número natural solicitado para sobre pasar el dato máximo")