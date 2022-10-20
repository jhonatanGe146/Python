"""Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores"""

nota = float (input ("Ingresar una nota entre 0 a 10: "))
if (nota <= 5.9):
    print ("Insuficiente")
elif (nota <= 6.9):
    print ("Suficiente")
elif (nota <= 7.9):
    print ("Bien")
elif (nota <= 8.9):
    print ("Excelente")
else:
    print ("Superior")