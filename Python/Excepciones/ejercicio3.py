#NameError: se produce cuando se intenta utilizar una variable o una función que no ha sido definida.
def ErrordeNombre():
    try:
        vari=0
        print(Vari)
    except NameError:
        print("NameError: Llamar a algo no definido")
        
ErrordeNombre()