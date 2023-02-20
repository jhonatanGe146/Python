#TypeError: se produce cuando se intenta realizar una operación con un tipo de datos inadecuado.
def ErrordeTipo(a,b):
    try:
        c = a/b
    except TypeError:
        print("TypeError: Error en los tipos de datos")
    
ErrordeTipo("5",2)







        
