try:
    """1- Realizar un codigo donde determine los numeros pares desde 0 hasta 10 con while"""
    par=0
    while par <=10:
        print(par)
        par+=2
    print()
    
    """2- Realizar un codigo donde determine los numeros impares desde 1 hasta 10 con for"""
    for i in range(1,10,2):
        print(i)
    
    """3-Realizar un dos codigos sonde el primero usando for con un rango de 10 sume cada
    numero pero usar un condicional para que se detenga cuando el rango se pasa del 7 con
    un break y el otro for igual pero sin el break"""
    suma=0
    for a in range(11):
        if a <= 7:
         suma+=a
        else: 
            break
    print("La suma es: ", suma)

    suma1=0
    for j in range(11):
        suma1+=j
    print("La suma es: ", suma1)

    """4- Realizar un codigo usando while para que le pida al usuario numeros enteros y que 
    en el transcurso lo vaya sumando y usar un condicional para que se detenga con break 
    cuando el usuario anote un numero mayor a 100 para mostrar al final del codigo la suma 
    de los numeros anotados hasta que se sobrepaso el numero 100"""

    suma2=0
    while True:
        num=int (input("Ingresa un numero: "))
        if num > 100:
            break
        else:
            suma2+=num
    print("La suma es ",suma2)

    """5- Realizar un codigo usando un for en un rango que muestre los numeros del rango en un mensaje"""
    rango=int (input("Ingresa el rango de numeros"))
    for i in range (rango+1):
        print(i ,end=" ")

    """6- Escribir un que pernita generar una tabla de multiplicar de un numero entero positivo N, comenzando desde 1
    si el usuario escribe un numero, el programa no se ejecuta y pide nuevamente el numero """
    while True:
        try:
            N=int(input("Ingresa el numero del que quieres conocer la tabla: "))
            if N > 0:
                for q in range (1,11):
                    print(N,"x", q, "=", (N*q))
                break
            else:
                print("Valor no soportado por favor ingresalo de nuevo")
        except:
            print("Valor no soportado por favor ingresalo de nuevo")
    
    """7- Crear un programa que lea un numero entero positivo N y escriba todos los numeros primos menores a dicho numero"""
    nume=int (input("Digita un numero: "))
    cont=0
    for j in range (1,nume+1):
        divisores=0
        for i in range (1,j):
            x=j%i
            if x==0:
                divisores+=1
        if divisores==1:
            print(j,"es primo")
            cont+=1
    print( cont, "numeros primos entre 0 y",nume)

    """8- Escribir un programa que pida una palabra al usuario y la muestre en la pantalla 10 veces """
    palabra=str (input("Ingrese una palabra"))
    for i in range (10):
        print(palabra)
    
    """9- Escribir un programa que e pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad)"""
    ahno=int(input("Digita tu edad: "))
    print("Has cumplido los siguientes años:\n")
    for j in range (1,ahno+1):
        print(j, "años")
    """10- Escribir un programa que al recibir como datos la altura, peso y genero de N cantidad de personas saca el promedio"""
    print("Elige tu genero para posteriormente seleccionar tu altura y peso o 1 para salir")
    genero=str(input("Ingresa tu genero: "))
    cantidadh=0
    cantidadm=0
    calh=0
    cpeh=0
    caltm=0
    cpem=0
    while True:
        genero=str(input("Ingresa tu genero: "))
        
        if genero=="masculino":
            cantidadh+=1
            al=float(input("Digita tu altura: "))
            pes=float(input("Digita tu peso: "))
            calh+=al
            cpeh+=pes
        elif genero =="femenino":
            cantidadm+=1
            alt=float(input("Digita tu altura: "))
            peso=float(input("Digita tu peso: "))
            caltm+=alt
            cpem+=peso
        elif genero=="1":
            break
    print("El promedio masculino de peso es ", cpeh/cantidadh, "y de altura es ", calh/cantidadh)
    print("El promedio masculino de peso es ", cpem/cantidadm, "y de altura es ", caltm/cantidadm)




except ValueError:
    print("Ingresaste un valor no soportado")