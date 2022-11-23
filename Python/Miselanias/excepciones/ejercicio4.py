
def ahorcado(palabra_secreta):
    lista = []
    for i in range(len(palabra_secreta)):
        lista.append(palabra_secreta[i])
    print (lista)
    cont=0
    while cont <6:
        letra=input("Letra que esta en la palabra.\n")
        if letra in lista:
            for j in range(len(lista)):
                if letra==j:
                    del lista[j]
                    print(lista)
            print("si estaban en la palabra:")
        else:
            print("No estaban en la palabra:")
            cont+=1
            if cont ==6:
                print("perdiste")
palabra_secreta=input("ingresa la palabra secreta")
ahorcado(palabra_secreta)