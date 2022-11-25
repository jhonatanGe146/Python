
#Comparar lista
def lista_igual(lista1,lista2):  
    if lista1 == lista2:
        return("Son iguales")
    else:
        return("Son diferentes")
#Insertar elemento a la lista 1
def insertar(lista1):
    x=int(input("Elemento que quieres agregar"))
    lista1.append(x)
    print("La lista esta asi:", lista1)
    
#Insertar elemento a la lista 2
def insertar2(lista2):
    y=int(input("Elemento que quieres agregar"))
    lista2.append(y)
    print("La lista esta asi:", lista2)
    





lista1=[]
lista2=[]
while True:
    print("Selecciona la opcion que quieres ejecutar\n")
    print("1-Insertar un elemento a la primera lista")
    print("2-Insertar un elemento a la segunda lista")
    print("3-Comparar lista")
    print("4-salir")
    print()
    control=int(input("Seleccione la opcion:\n"))
    match control:
        case 1:
            insertar(lista1)
        case 2:
            insertar2(lista2)
        case 3:
            print(lista_igual(lista1,lista2))
        case 4:
            print("saliste")
            break
        case _:
            print("NO HAY ESTA OPCION ")
