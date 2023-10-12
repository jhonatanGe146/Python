def decoradora(funcion): #? Se define la función base que tiene como parámetro (funcion)
    print('inicia función decoradora') # * Imprime ('inicia función decoradora')
    def acondicionamiento(): #? Se define la función interna (acondicionamiento())
        #print(funcion())
        return f'trotar y estirar \n {funcion()}'  # * Retorna la cadena de texto 'trotar y estirar' junto con un salto de linea y 
    return acondicionamiento

def tapar():
    return 'tapando'
    #print('tapando')

arquero=decoradora(tapar)
print(arquero())

@decoradora
def patear():
    return 'pateando'
print(patear())

@decoradora
def cabecear():
    return 'cabeceando'
print(cabecear())