
#!Sobreescritura de métodos:












#! Polimorfismo: Es la capacidad de los objetos de diferentes clases para ser tratados de manera uniforme.

'''class Animal:
    v="hace"
    def hacer_sonido(self):
        pass
    
    def FunctionName(self):
        print('Funcion heredada')
        

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")
        
        


buldog=Perro()
(buldog.hacer_sonido())
egipcio=Gato()
egipcio.hacer_sonido()

'''


#!Herencia múltiple
'''class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left,Right):
    pass


obj = Sub()
print(obj.fun())
'''


#? Ejemplo:

class Habitacion:
    Estado='Activa'
    def __init__(self,num,pre):
        self.numero=num
        self.precio=pre
    def descripcion (self):
        pass
    

class simple(Habitacion):
    def __init__(self,num,pre):
        Habitacion.__init__(self,num,pre)
        
    def descripcion(self):
        return 'Habitacion simple, cama descansable'  

class doble (Habitacion):
    def __init__(self,num,pre):
        Habitacion.__init__(self,num,pre)
        
    def descripcion(self):
        return 'Habitacion doble, cama relajante'
    
class triple (Habitacion):
    def __init__(self,num,pre):
        Habitacion.__init__(self,num,pre)
    
    def descripcion(self):
        return 'Habitacion triple, cama de lujo'
        
    
T=triple(305,200000)
D=doble(102,110000)
S=simple(52,56320)

print(T.descripcion())
print(D.descripcion())
print(S.descripcion())
        
        
