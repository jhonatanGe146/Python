"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios. 
Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que posicion esta.
si no está agréguelo al fial de la lista"""

def buscar(lista):
    import random
    rango= random.randint(10,25)
    num=int(input("Ingresa el valor a buscar en la lista: "))
    cont=0
    for i in range (rango):
        lista.append(round(random.random()*100))
    print("su lista es :\n",lista)
    if num in lista[:]:
        for j in range(len(lista)):
            if num==lista[j]:
                cont+=1
                print("El número",num,"esta en la posición",j,",",cont,"veces")
    else:        
        print("El valor", num, "no esta en la lista. se agregara de inmediato")
        lista.append(num)
        print(lista)
lista=[]
print(buscar(lista))