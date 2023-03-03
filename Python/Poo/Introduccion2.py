class Vehiculo:
    def __init__(self,tipo):
        self.__tipo = tipo
        
    def descripcion(self):
        print ('soy generico no tengo descripción :( )')
        
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        print('Soy generico de la clase Vehiculo')
    
    
    
    
    
class Herramienta:
    def __init__(self, prop):
        self.__proposito = prop
        

    def getProposito(self):
        return self.__proposito
    
    def __str__(self):
        print('Soy generico de la clase Herramienta')
    
    
    
    
    

class Acuatico (Herramienta,Vehiculo):
    def __init__(self,tipo,propo):
        Vehiculo.__init__(self,tipo)
        Herramienta.__init__(self,propo)
        
    def datos(self):
        print('tipo', super().getTipo())
        print('tipo', super().getProposito())
        
    
    
    

    
m=Acuatico('Barco','transportar')
m.__str__()
#print(m.getTipo())
m.datos()