class Persona:#Define una clase.    
    def __init__(self,nombre ,documento):#Define una método constructor llamado (__init__), tiene como parametro (self y nombre).        
        self.__nombre=nombre#A self.__nombre se le asigna el valor del parámetro nombre.        
        self.__documento= documento #Crea un atributo o variable (self.__documento) la cual almacena lo de la variable documento
        #print('Constructor Activado')# Comentario que imprime una cadena ('Constructor Activado')     
    def getNombre(self):#Define un método llamado (getNombre) que tiene como parametro (self).       
        return self.__nombre# Devuelve el valor de (__nombre) de la instancia de la clase 
    def setNombre(self,nombre):#Define un método llamado (setNombre) que tiene como parametro (self y nombre).        
        self.__nombre=nombre#A la instancia de la clase (self.__nombre) se le  asigna el valor del parámetro (nombre)                    
    def getDocumento(self):#Define un método  (getDocumento) que no tiene parámetros      
        return self.__documento#Retorna el (__documento) de la instancia de la clase
    def setDocumento(self,documento):#Define un método  (setDocumento) que tiene un parámetro       
        self.__documento=documento#Realiza una actualización al (__documento) el cual se le asigana el valor ingresado como parámetro.



class Aprendiz(Persona):#Define una clase (Aprendiz) que toma con argumento la clase (Persona), es un subclase.
    def __init__(self, nombre, documento, ficha):#Define un método  constructor  llamado (__inint__), que tiene como parámetro (self,nombre,documento,y ficha)
        Persona.__init__(self,nombre, documento)#LLama el método constructor de la clase Persona que tiene como parámetro (self,nombre, documento) 
        self.__ficha=ficha#Crea un atributo o variable (sefl.__ficha) la cual almacena lo de la variable ficha
    def get_ficha(self):#Define un método llamado (get_ficha) que tiene como parámetro (self).
        return self.__ficha#Retorna lo que se ha almacenado en el atributo (self.__ficha)
    def todo (self):#Define un método llamado (todo) que tiene como parámetro (self).
        print(self.getNombre())#Llama e imprime el método (getNombre()) de la clase padre persona.
        print(self.getDocumento())#Llama e imprime el método (getDocumento()) de la clase padre persona.
        print(self.get_ficha())#llama e imprime el método (get_ficha()) de la clase hija  Aprendiz.
        return " "#Retorna un espacio en blanco.
    


apren=Aprendiz('Andres',1100502146,2560664)#Crea una instancia o objeto llamado (apren) de la clase (Aprendiz) y se pasa como parámetros ('Andres',1100502146,2560664)
print(apren.todo())#Llama e imprime el método (todo) respecto al objeto (apren)


vo=Persona('Gloria',1098100329)#Crea una instancia o objeto llamado (vo) de la clase (Persona) y se pasa como parámetros ('Andres',1100502146)
vo1=Aprendiz('Gloria',1098100329,25305024)#Crea una instancia o objeto llamado (vo1) de la clase (Aprendiz) y se pasa como parámetros ('Gloria', 1098100329,25305024)
print(vo1.todo())#Llama e imprime el método (todo) respecto al objeto o instancia (vo1)


ob=Persona('Maria', 1102032932393)#Creción o instancia de la clase (Persona()) que pasa como argumento un str (nombre), en este caso ('Maria) y su  documento.
print(ob.getNombre())#Llama e imprime el método (getNombre) respecto al objeto o instancia (ob)
