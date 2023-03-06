
#! Clase Padre Material
class Material:
    def __init__(self,titulo,tipo,auto):
        self.Titulo_Material = titulo
        self.Tipo_Material = tipo
        self.Autor_Material = auto
        
    def getTitulo(self):
        return self.Titulo_Material
    def setTitulo(self,titulo):
        self.Titulo_Material=titulo
    #setter/getter Tipo_libro}
    def getTipo(self):
        return self.Tipo_Material
    def setTipo(self,tipo):
        self.Tipo_Material=tipo
    #setter/getter Autor_libro
    def getAutor(self): 
        return self.Autor_Material
    def setAutor(self,autor):
        self.Autor_Material=autor
    
    
        
class libro(Material):
    def __init__(self,titulo,tipo,auto,edi):
        Material.__init__(self,titulo,tipo,auto)
        self.Editorial_libro=edi
    def getEditorial(self):
        return self.Editorial_libro
    def setEditorial(self,edi):
        self.Editorial_libro=edi
   

class Revista(Material):
    def __init__(self,titulo,tipo,auto,edi):
        Material.__init__(self,titulo,tipo,auto)
        self.Edicion=edi
    def getEdicion(self):
        return self.Edicion
    def setEditorial(self,edi):
        self.Edicion=edi
       
# y=libro('Cien Años de Soledad','Drama','Gabriel','NN')
# print(y.getTitulo())
# y.setTitulo('el principito')
# print(y.getTitulo())
# print(y.getEditorial())
# x=Revista('chistes de la semana','comedia','perez','la risa')
# print(x.getTitulo())
# x.setTitulo('el principito')
# print(x.getTitulo())
# print(x.getEdicion())


class Lector:
    def __init__(self,Nom,Dir,Te):
        self.Nombre = Nom
        self.__Direccion = Dir
        self.__Telefono = Te
        self.__libro=[]
        
    #setter/getter Nombre
    def getNombre(self):
        return self.Nombre
    def setNombre(self,nombre):
        self.Nombre=nombre
    #setter/getter dirección
    def getDireccion(self):
        return self.__Direccion
    def setDireccion(self,direccion):
        self.__Direccion=direccion
    #setters/getter Telefono
    def getTelefeno (self):
        return self.__Telefono
    def setTelefono (self, tele):
        self.__Telefono=tele
    #Reservar libro
    def resevar(self, material):
        self.__libro.append(material)
    def getRervados(self):
        for i in self.__libro:
            print(i.getTitulo(),' ')


        
    



class Estudiante(Lector):
    __codigo=100
    def __init__(self,Nom,Dir,Te):
        Lector.__init__(self,Nom, Dir, Te)
        Estudiante.__codigo+=1
        

    def getCodigoEstudiante(self):
        return Estudiante.__codigo
    
# es=Estudiante('jhon','cra 12',321)
# print(es.getCodigoEstudiante())

class Docente(Lector):
    __codigo=100
    def __init__(self,Nom,Dir,Te):
        Lector.__init__(self,Nom, Dir, Te)
        Docente.__codigo+=1
        
    def getCodigoDocente(self):
        
        return Docente.__codigo
    
    
# s=Docente('Samuel','cr 15',32144)
# print(s.getCodigoDocente())
# print(s.getDireccion())
# s.setTelefono(32323256)
# print(s.getTelefeno())

class Bibliotecario():
    __ID=200
    def __init__(self,nom):
        Bibliotecario.__ID+=1
        self.nombreBibliotecario=nom
    
    #setter/getter
    def getNombreBibliotecario(self):
        return self.nombreBibliotecario
    def setNombreBibliotecario(self,no):
        self.nombreBibliotecario=no    
    
    
    def getCodigoBibliotecario(self):
        return Bibliotecario.__ID

# b=Bibliotecario()
# print(b.getCodigoBibliotecario())



class Pedido():
    def __init__(self,usu,ma,bi):
        self.pedido=[]
        self.__Usuario=usu
        self.Material=ma
        self.Bicliotecario=bi
    def getUsuario(self):
        return self.__Usuario
    def getMaterial(self):
        return self.Material
    def getBibliotecario(self):
        return self.Bicliotecario
    def getTodo(self):
        print(self.getUsuario())
        print(self.getMaterial())
        print(self.getBibliotecario())
        
        


y=libro('Cien Años de Soledad','Drama','Gabriel','NN')
x=Revista('chistes de la semana','comedia','perez','la risa')

m=Estudiante('Andres','cra 12', 321155164464)
b=Bibliotecario('Maicol')
print(b.getNombreBibliotecario())
m.resevar(y)
m.resevar(x)
v=m.getRervados()
ped=Pedido(m,v,b)
#ped.getTodo()
print(ped.getUsuario())