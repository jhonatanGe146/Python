
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
    #setter/getter Tipo_libro
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
        self.__d=[self.Tipo_Material,self.Autor_Material,self.Editorial_libro]
    def getEditorial(self):
        return self.Editorial_libro
    def setEditorial(self,edi):
        self.Editorial_libro=edi
    def Cont_Libro (self):
        return self.__d
    
   

class Revista(Material):
    def __init__(self,titulo,tipo,auto,edi):
        Material.__init__(self,titulo,tipo,auto)
        self.Edicion=edi
        self.__d=[self.Tipo_Material,self.Autor_Material,self.Edicion]
    def getEdicion(self):
        return self.Edicion
    def setEdicion(self,edi):
        self.Edicion=edi
    def Cont_Revis (self):
        return self.__d
       


class Lector:
    def __init__(self,Nom,Dir,Te):
        self.Nombre = Nom
        self.__Direccion = Dir
        self.__Telefono = Te
        self.__reservado={}
        
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
    def getTelefono (self):
        return self.__Telefono
    def setTelefono (self, tele):
        self.__Telefono=tele
    #Reservar libro
    def reserva (self,No_t,material):
        self.__reservado[No_t]=material
    def getReserva (self):
        return f'{self.Nombre} a reservado {self.__reservado}'
    
    #Devolver Libro:
    def Entregar(self, titulo):
        if titulo in self.__reservado:
            print(f'{self.Nombre} a Entregado {titulo}')
            del self.__reservado[titulo]
        else:
            print('No ha reservado este libro')
   
        
    
class Estudiante(Lector):
    __codigo=100
    def __init__(self,Nom,Dir,Te):
        Lector.__init__(self,Nom, Dir, Te)
        Estudiante.__codigo+=1

    def getCodigoEstudiante(self):
        return Estudiante.__codigo
    


class Docente(Lector):
    __codigo=100
    def __init__(self,Nom,Dir,Te):
        Lector.__init__(self,Nom, Dir, Te)
        Docente.__codigo+=1
        
    def getCodigoDocente(self):
        
        return Docente.__codigo


"""class Bibliotecario():  
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

class Pedido():
    def __init__(self, usu, ma, bi=0):
        self.usu = usu
        self.ma = ma
        self.bi = bi
        
    def getNombre(self):
        print(self.usu)
        print(self.ma)
        #print(self.bi)
        
    def Realizarpedido(self):
        pass
        """
        

y=libro('Cien Años de Soledad','Drama','Gabriel','NN')
#print (y.Cont_Libro())

x=Revista('chistes de la semana','comedia','perez','la risa')
#print(x.Cont_Revis())

m=Estudiante('Andres','cra 12', 321155164464)
m.reserva(x.getTitulo(), x.Cont_Revis())
m.reserva(y.getTitulo(),y.Cont_Libro())
print(m.getReserva())
m.Entregar('Cien Años de Soledad')
print(m.getReserva())
#print(m.todo())
