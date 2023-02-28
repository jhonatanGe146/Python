class Persona:#Define una clase.    
    def __init__(self,nombre ,documento):#Define una método constructor llamado (__init__), tiene como parametro (self y nombre).        
        self.__nombre=nombre#A self.__nombre se le asigna el valor del parámetro nombre.        
        self.__documento= documento 
        #print('Constructor Activado')# Comentario que imprime una cadena ('Constructor Activado')     
    def getNombre(self):#Define un método llamado (getNombre) que tiene como parametro (self).       
        return self.__nombre# Devuelve el valor de (__nombre) de la instancia de la clase 
    def setNombre(self,nombre):#Define un método llamado (setNombre) que tiene como parametro (self y nombre).        
        self.__nombre=nombre#A la instancia de la clase (self.__nombre) se le  asigna el valor del parámetro (nombre)                    
    def getDocumento(self):#Define un método  (getDocumento) que no tiene parámetros      
        return self.__documento#Retorna el (__documento) de la instancia de la clase
    def setDocumento(self,documento):#Define un método  (setDocumento) que tiene un parámetro       
        self.__documento=documento#Realiza una actualización al (__documento) el cual se le asigana el valor ingresado como parámetro.



class Aprendiz(Persona):
    def __init__(self, nombre, documento, ficha):
        Persona.__init__(self,nombre, documento)
        self.__ficha=ficha
    def get_ficha(self):
        return self.__ficha
    def todo (self):
        print(self.getNombre())
        print(self.getDocumento())
        print(self.get_ficha())
        return " "
    
pers=Persona('Andres',1100502146)
print(pers.getDocumento())
pers.setDocumento(1098100329)
print(pers.getDocumento())


print()
print()
apren=Aprendiz('Andres',1100502146,2560664)
print(apren.todo())
#metodo para ver el documentos #metodo para ver todos los datos de aprendiz

vo=Persona('Gloria',1098100329)
vo1=Aprendiz('Gloria',1098100329,25305024)
print(vo1.todo())


"""ob=Persona('Maria')#Creción o instancia de la clase (Persona()) que pasa como parametro un str (nombre), en este caso ('Maria) 
print(ob.getNombre())#Imprime lob.setNombre('Ana')
print(ob.getNombre())#print(type(ob))"""