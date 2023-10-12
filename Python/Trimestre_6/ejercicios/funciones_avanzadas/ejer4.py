def decoradora (*args):
    print('Inicia funcion decoradora')
    def acondicionamiento ():
        for i in args:
            print (i())
        return('Trotar y estirar')
    return acondicionamiento
#! Primera Forma de decorar
@decoradora
def tapar ():
    return('Tapando')

def patear ():
    return('Patear')

def cabecear ():
    return('Cabecear')

#! Segunda Forma de decorar
# arquero = decoradora(tapar,patear,cabecear)
# print (arquero())


print (tapar())