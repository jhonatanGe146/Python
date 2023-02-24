#Ejemplo de else con excepciones.

def ErrordeTipo(a,b):
    try:
        c = a/b
    except TypeError:
        print("TypeError: Error en los tipos de datos")
    else:
        print(c)
    
ErrordeTipo('a',2)



def ErrordeMemoria():
    try:
        v=[1]*100000000000
    except MemoryError:
        print("MemoryError:Se produce cuando el sistema no tiene suficiente memoria para en este caso crear la lista.")
    else:
        print(v)

ErrordeMemoria()

