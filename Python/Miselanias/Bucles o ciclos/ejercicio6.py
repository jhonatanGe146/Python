"""Calcular el máximo de números positivos introducidos por
teclado, sabiendo que metemos números hasta que
introduzcamos uno negativo. El negativo no cuenta."""

mayor=0
num = int (input ("Digita un número o -1 para terminar el programa: "))
if num == -1:
    print ("Fin del programa")
else:
    while num != -1:
        if num > mayor:
            mayor = num
        num = int (input ("Digita un número: "))
    print ("El número más grande es:",mayor)