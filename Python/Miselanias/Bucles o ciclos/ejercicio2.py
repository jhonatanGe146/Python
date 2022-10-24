""" Determinar si un numero es o no es primo """

numero = int (input ("Digita un número: "))
cont=0
if numero > 1:
    for i in range (2, numero):
        division= numero%i
        if division==0:
            cont+=1
    if cont==0:
        print ("El número", numero, "es primo")
    else:
        print("El número", numero, "es no primo")
else:
    print(numero, "no es un número primo")