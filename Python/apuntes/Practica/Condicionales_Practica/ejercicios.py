try:
    """1-Realizar un códigoo donde convierta un número negativoen positivo y viceversa"""

    import random
    numero=round(random.randint(-100,100))
    print ("El numero a convertir es ",numero)
    if numero < 0:
        numero*=-1
    else:
        numero*=-1
    print("El numero puesto es", numero)

    """2-Realizar un codigo donde pida al usuario un numero entero y 
    determne si es positivo, negativo o cero"""

    numero=int(input("Ingresa un numero: "))
    if numero == 0:
        print("El numero es cero")
    elif numero < 0:
        print ("El numero es negativo")
    else:
        print("El numero es positivo")
    
    """3- Realizar un codigo donde pida al usuario un numero entero y 
    determine si es mayor que cero, igual a cero o menor a cero"""

    numero=int(input("Ingresa un numero: "))
    if numero == 0:
        print("El numero es cero")
    elif numero < 0:
        print ("El numero es menor que cero")
    else:
        print("El numero es mayor que cero")

    """4- Realizar un codigo donde pida al usuario tres numeros enteros y determine 
    si estan en oreden creciente y sino escribir un mensaje de que no se ordenan de manera creciente"""

    x=int (input("Ingerse un numero: "))
    y=int (input("Ingerse un numero: "))
    z=int (input("Ingerse un numero: "))
    if x<= y and y <=z:
        print(x , y , z ,"Estan ordenados  de forma ascedente")
    else:
        print(x , y ,z ,"No estan ordenados de forma ascedente")

    """5- Realizar un codigo donde la variable (a) le sea asignada un numero entero y determina
     si esta entre el rango de 10 y 20 o si es mayor """

    a=int (input("Ingerse un numero: "))
    if a>= 10 and a <=20:
        print(a ,"Esta dentro del rango 10-20")
    elif a < 10:
        print(a, "Esta por debajo del rango 10-20")
    else:
        print(a ,"Esta por encima del rango 10-20")



except ValueError:
    print("Has ingresado un valor no soportado")