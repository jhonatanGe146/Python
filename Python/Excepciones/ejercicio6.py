#AttributeError: se produce cuando se intenta acceder a un atributo que no existe en un objeto.
def ErrordeAtributos():    
    try:       
        cadena="hola"
        nombre=input("Nombre del la persona: ")
        cadena.append(nombre)
        print(cadena)
    except AttributeError:
        print('AttributeError:Un error que se genera cuando falla una asignación o una referencia de atributo.')
        
ErrordeAtributos()