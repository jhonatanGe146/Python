#IndexError: se produce cuando se intenta acceder a un índice que está fuera del rango de una lista, tupla o matriz.
def ErrordeIndice():
    lista = [1, 2, 3]
    try:
        print(lista[3])
    except IndexError:
        print("IndexError: Índice fuera de rango")

ErrordeIndice()