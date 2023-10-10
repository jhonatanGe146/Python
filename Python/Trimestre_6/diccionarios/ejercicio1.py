"""Ejercicio 1.
Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves 
sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves."""


def diccionario_cuadrado():
    try:
        limite= int (input("Ingresa el numero limite: "))
        diccionario_cuadra = {}
        
        for i in range (1, limite+1):
            diccionario_cuadra[i]=i**2

        print("Diccionario Cuadrado")
        for k in diccionario_cuadra.items():
            clave , valor = k
            print(f"{clave} = {valor} ")
    except ValueError:
        print ("ERROR!! Debe ingresar un numero")
        diccionario_cuadrado()


diccionario_cuadrado()
