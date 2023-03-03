
#! Estructura Base de una clase
class Ejemplo ():# Estructura de una clase
    def __init__(self,var):# Metódo constructor, se ejecuta en el momento de instancia una clase, identifica el objeto para el cual se invoca el método.
        self.__var=var
        print('Metodo Constructor')
    def set_ejemplo (self,var):
        self.__var=var
    def get_ejemplo (self):
        return self.__var
    
objet=Ejemplo('hola')
print(objet.get_ejemplo())
objet.set_ejemplo('chao')
print(objet.get_ejemplo())

#! Estructura con variables de clase e instancia de una clase

class Ejemplo2 ():
    __lista=[]#Variable de clase debido a que esta fuera de todos los métodos de la clase.
    def __init__(self,tele):
        self.__telefono=tele#Variable de instancia porque esta dentro de un método.
        Ejemplo2.__lista.append(self.__telefono)
    def set_telefono (self,tele):
        self.__telefono=tele
    def get_telefono (self):
        return self.__telefono
    def get_lista ():
        return Ejemplo2.__lista
    
objet2=Ejemplo2(321456887)
objeto3=Ejemplo2(32148448)

# Crear un atributo exclusivo de un objeto 
objeto3.tele2=321554488

#Uso de gettters/setters
print(objet2.get_telefono())
objet2.set_telefono(12345)
print(objet2.get_telefono())

#Imprimir la variable de clase
print(Ejemplo2.get_lista())

#Imprimir la variable exclusiva del objeto3(tele2)
print(objeto3.tele2)
#del objeto3.tele2
print(objeto3.tele2)
#print(objet2.tele2)

#Diferencias de objetos
print(objeto3.__dict__)
print(objet2.__dict__)

#!Verificacion de atributos
class ExampleClass:
    attri = 1
    def __init__(self):
        self.attr = 1

m=ExampleClass()
print(hasattr(m, 'attr'))
print(hasattr(ExampleClass,'attri'))
print(hasattr(ExampleClass, 'prop'))


