# Metodos y asignación de variables
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var, self.nombre)


obj = Classy()
obj.var = 12
obj.nombre = "deimar"
obj.method()


#El parámetro self también se usa para invocar otros métodos desde dentro de la clase.
class Classy:
    def other(self):
        print("otro")

    def method(self):
        print("método")
        self.other()


obj = Classy()
obj.method()

#El metódo constructor no puede retornar nada ya que retorna el objeto recien creado
class Classy:
    def __init__(self, value):
        self.__var = value
        


obj_1 = Classy("objeto")

print(obj_1)


# Ocultar metódos
class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("oculto")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("fallido")

obj._Classy__hidden()



#ver lo que contiene cada objeto y lo que contiene la clase
class Classy2:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy2()

print(obj.__dict__)
print(Classy2.__dict__)

#Mas metodos ademas de __init
def __str__(self):
        return self.name + ' en ' + self.galaxy