
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
        self.__usuario = [self.Nombre,self.__Direccion,self.__Telefono]
        
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
    def datos_usuario (self):
        return self.__usuario
   
        
    
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


class Bibliotecario():
    __ID=200
    def __init__(self,nom):
        Bibliotecario.__ID+=1
        self.nombreBibliotecario=nom
    
    #setter/getter
    def getNombreBibliotecario(self):
        return f'bibliotecario: {self.nombreBibliotecario}'
    def setNombreBibliotecario(self,no):
        self.nombreBibliotecario=no    
        
    def getCodigoBibliotecario(self):
        return Bibliotecario.__ID

class Pedido():
    def __init__(self, usu, ma, bi):
        self.usu = usu
        self.ma = ma
        self.bi = bi
        self.pedido=[self.usu, self.ma, self.bi]
        
    def getUsu(self):
        return self.usu
    def getma(self):
        return self.ma
    def getbi (self):
        return self.bi
        
    def getresivo (self):
        return self.pedido
        

# y=libro('Cien Años de Soledad','Drama','Gabriel','NN')
# #print (y.Cont_Libro())
# x=Revista('chistes de la semana','comedia','perez','la risa')
# #print(x.Cont_Revis())
# b=Bibliotecario('stiven')
# m=Estudiante('Andres','cra 12', 321155164464)
# dt=(m.datos_usuario())
# db=(b.getNombreBibliotecario())
# #print(m.getCodigoEstudiante())

# m.reserva(x.getTitulo(), x.Cont_Revis())
# m.reserva(y.getTitulo(),y.Cont_Libro())
# re=(m.getReserva())
# m.Entregar('Cien Años de Soledad')
# print(m.getReserva())
# pe=Pedido(dt,re,db)
# print(pe.getresivo())


def Biblioteca (var):    
    while True:
        print('1- Crear')
        print('2- Consultas')
        print('3- Actualizar')
        print('4- Salir')
        print()
    
        ctrl=str (input("Seleciona una opcion: "))
        match ctrl:
            case '1':
                print()
                print('1- Crear estudiante')
                print('2- Crear Docente')
                print('3- Crear libro')
                print('4- Crear revista')
                print('5- Crear bibliotecario')
                ctrl=str (input("Seleciona una opcion: "))
                match ctrl:
                    case '1':
                        c1=str(input('Nombre del estudiante: '))
                        c2=str(input('Dirección del estudiante: '))
                        c3=str(input('Telefono del estudiante: '))
                        var=Estudiante(c1,c2,c3)
                    case '2':
                        c1=str(input('Nombre del Docente: '))
                        c2=str(input('Dirección del Docente: '))
                        c3=str(input('Telefono del Docente: '))
                        var=Docente(c1,c2,c3)
                    case '3':
                        c1=str(input('Titulo del libro: '))
                        c2=str(input('Genero del libro: '))
                        c3=str(input('Autor del libro: '))
                        c4=str(input('Editorial del libro: '))
                        var=libro(c1,c2,c3,c4)
                    case '4':
                        c1=str(input('Titulo de la revista: '))
                        c2=str(input('Genero de la revista: '))
                        c3=str(input('Autor de la revista: '))
                        c4=str(input('Edicion de la revista: '))
                        var=Revista(c1,c2,c3,c4)
                    case '5':
                        c1=str(input('Nombre del bibliotecario: '))
                        var=Bibliotecario(c1)
    
            case '2':
                print()
                print('1- Consultar estudiante')
                print('2- Consultar Docente')
                print('3- Consultar libro')
                print('4- Consultar revista')
                print('5- Consultar bibliotecario')
                print()
                ctrl=str (input("Seleciona una opcion: "))
                match ctrl:
                    case '1':
                        while True:
                            print()
                            print('1- Consultar Nombre estudiante')
                            print('2- Consultar Dirección estudiante')
                            print('3- Consultar Telefono estudiante')
                            print('4- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            match ctrl:
                                case '1':
                                    print('Nombre del estudiante:',var.getNombre())
                                case '2':
                                    print('Dirección del estudiante:',var.getDireccion())
                                case '3':
                                    print('Telefono del estudiante:',var.getTelefono())
                                case '4':
                                    break
                    case '2':
                        while True:
                            print()
                            print('1- Consultar Nombre Docente')
                            print('2- Consultar Dirección Docente')
                            print('3- Consultar Telefono Docente')
                            print('4- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            match ctrl:
                                case '1':
                                    print('Nombre del Docente:',var.getNombre())
                                case '2':
                                    print('Dirección del Docente:',var.getDireccion())
                                case '3':
                                    print('Telefono del DOCENTE:',var.getTelefono())
                                case '4':
                                    break
                    case '3':
                        while True:
                            print()
                            print('1- Consultar Titulo del libro')
                            print('2- Consultar Genero del libro')
                            print('3- Consultar Autor del libro')
                            print('4- Consultar Editorial del libro')
                            print('5- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            match ctrl:
                                case '1':
                                    print('Nombre del Docente:',var.getTitulo())
                                case '2':
                                    print('Dirección del Docente:',var.getTipo())
                                case '3':
                                    print('Telefono del DOCENTE:',var.getAutor())
                                case '4':
                                    print('Editorial del libro', var.getEditorial())
                                case '5':
                                 
                                    break
                    case '4':
                        while True:
                            print()
                            print('1- Consultar Titulo de la revista')
                            print('2- Consultar Genero de la revista')
                            print('3- Consultar Autor de la revista')
                            print('4- Consultar Editocion de la revista')
                            print('5- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            match ctrl:
                                case '1':
                                    print('Nombre del Docente:',var.getTitulo())
                                case '2':
                                    print('Dirección del Docente:',var.getTipo())
                                case '3':
                                    print('Telefono del DOCENTE:',var.getAutor())
                                case '4':
                                    print('Editorial del libro', var.getEdicion())
                                case '5':
                                 
                                    break
                    case '5':
                        while True:
                            print()
                            print('1- Consultar Nombre Bibliotecario')
                            print('2- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            match ctrl:
                                case '1':
                                    print('Nombre del Bibliotecario:',var.getNombreBibliotecario())
                                case '2':
                                    break   
                        
            case '3':
                print()
                print('1- Actualizar Estudiante')
                print('2- Actualizar Docente')
                print('3- Actualizar libro')
                print('4- Actualizar revista')
                print('5- Actualizar bibliotecario')
                print()
                ctrl=str (input("Seleciona una opcion: "))
                match ctrl:
                    case '1':
                        
                        while True:
                            print()
                            print('1- Actualizar Nombre estudiante')
                            print('2- Actualizar Dirección estudiante')
                            print('3- Actualizar Telefono estudiante')
                            print('4- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            print()
                            match ctrl:
                                case '1':
                                    nom=str(input('Ingrese nombre para actualizar; '))
                                    var.setNombre(nom)
                                case '2':
                                    dir=str(input('Ingrese dirrección para actualizar: '))
                                    var.setDireccion(dir)
                                case '3':
                                    tel=str(input('Ingrese Teléfono para actualizar: '))
                                    var.setTelefono(tel)
                                case '4':
                                    break
                    case '2':
                        while True:
                                print()
                                print('1- Actualizar Nombre Docente')
                                print('2- Actualizar Dirección  Docente')
                                print('3- Actualizar Telefono  Docente')
                                print('4- Salir')
                                ctrl=str (input("Seleciona una opcion: "))
                                print()
                                match ctrl:
                                    case '1':
                                        nom=str(input('Ingrese nombre para actualizar; '))
                                        var.setNombre(nom)
                                    case '2':
                                        dir=str(input('Ingrese dirrección para actualizar: '))
                                        var.setDireccion(dir)
                                    case '3':
                                        tel=str(input('Ingrese Teléfono para actualizar: '))
                                        var.setTelefono(tel)
                                    case '4':
                                        break
                    case '3':
                        while True:
                                print()
                                print('1- Actualizar Titulo del libro')
                                print('2- Actualizar Genero del libro')
                                print('3- Actualizar Autor del libro')
                                print('4- Actualizar la editorial del libro')
                                print('5- Salir')
                                ctrl=str (input("Seleciona una opcion: "))
                                print()
                                match ctrl:
                                    case '1':
                                        nom=str(input('Ingrese titulo para actualizar: '))
                                        var.setTitulo(nom)
                                    case '2':
                                        dir=str(input('Ingrese Genero para actualizar: '))
                                        var.setTipo(dir)
                                    case '3':
                                        tel=str(input('Ingrese autor para actualizar: '))
                                        var.setAutor(tel)
                                    case '4':
                                        edi=str(input('Ingrese editotial para actualizar: '))
                                        var.setEditorial(edi)
                                    case '5':
                                        break
                    case '4':
                        while True:
                                print()
                                print('1- Actualizar Titulo de la revista')
                                print('2- Actualizar Genero de la revista')
                                print('3- Actualizar Autor de la revista')
                                print('4- Actualizar la edición de la revista')
                                print('5- Salir')
                                ctrl=str (input("Seleciona una opcion: "))
                                print()
                                match ctrl:
                                    case '1':
                                        nom=str(input('Ingrese titulo para actualizar: '))
                                        var.setTitulo(nom)
                                    case '2':
                                        dir=str(input('Ingrese genero para actualizar: '))
                                        var.setTipo(dir)
                                    case '3':
                                        tel=str(input('Ingrese autor para actualizar: '))
                                        var.setAutor(tel)
                                    case '4':
                                        edi=str(input('Ingrese edicion para actualizar: '))
                                        var.setEditorial(edi)
                                    case '5':
                                        break
                    case '5':
                        while True:
                            print()
                            print('1- Actualizar Nombre del bibliotecario')
                            print('2- Salir')
                            ctrl=str (input("Seleciona una opcion: "))
                            print()
                            match ctrl:
                                case '1':
                                    nom=str(input('Ingrese nombre para actualizar: '))
                                    var.setNombreBibliotecario(nom)
                                case '2':
                                    break
                                    
            case '4':
                print('Saliste de programa')
                break
               
               
    

with open ('Python/Evaluaciones/Aprendicez.txt','r') as flujo:
    ap=flujo.readlines()
    x=ap.remove('\n')
    #ap2=ap.split(',')
    for i in ap:
        x=(i.split(','))  
        print(x)
lista=[]
    
        