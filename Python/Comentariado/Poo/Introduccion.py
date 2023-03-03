class Vehiculo:#Define una clase llamada (Vehiculo)
    def __init__(self,tipo):#Define un método construtor que tiene como párametro (tipo)
        self.tipo=tipo#Crea una variable de instancia que almacena el argumento (tipo)
    def descripcion(self):#Crea un método llamado(descripcion)
        print('Soy generico no tengo descripcion',self.tipo)#Imprime una cadena (Soy generico no tengo descripcion) y la variable de instancia (self.tipo)
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):#Crea un método llamado (getTipo)
        return self.tipo#retorna la variable de instancia (self.tipo)
        #return Vehiculo.tipo
    def __str__(self):#crea un método llamado (__str__) 
        return 'Soy objeto de la clase Vehiculo'#Retorna una cadena (Soy objeto de la clase Vehiculo)

class Herramienta:#crea una clase llamada (Herramienta)
    def __init__(self,proposito):#Define un método construtor que tiene como párametro (proposito)
        self.__proposito=proposito#Crea una variable de instancia que almacena el argumento (proposito)
    def getProposito(self):#Crea un método llamado (getProposito)
        return self.__proposito#Retorna la variable de instancia (self.proposito)
    def __str__(self):#crea un método llamado (__str__) 
        return 'Soy objeto de la clase Herramienta'#Retorna una cadena (Soy objeto de la clase Herramienta)
class Terrestre(Vehiculo,Herramienta):#Crea una subclase de las superclases (Vehiculo,Herramienta)
    def __init__(self,tipo,proposito):#Crea un método constructor que tiene como parámetros (tipo,proposito)
        Herramienta.__init__(self,proposito)#Llama al método constructor de la super clase (Herramienta)
        Vehiculo.__init__(self,tipo)#Llama al método constructor de la super clase (Vehiculo)     
    def datos(self):#crea un método llamado (datos)
        print('Tipo: ',super().getTipo())#Imprime una cadena (Tipo) y el método (getTipo)
        print('Tipo: ',super().getProposito())#Imprime una cadena (Tipo) y el método (getProposito)
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")#Instancia la clase Terrestre que pasa como argumentos ('terrestre','carga')
t.datos()#Utiliza el método (datos), respecto al objeto (t)
print(t.__str__())#Imprime el método (__str__) respecto al objeto (t)