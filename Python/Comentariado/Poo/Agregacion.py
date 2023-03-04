class Aprendiz:#Crea una clase (Aprendiz)
    def __init__(self,nombre):#Crea el método constructor de la clase (Aprendiz) que  tiene como parámetro (nombre)
        self.__nombre=nombre#Crea una variable de instancia 'privada' (__nombre) que almacena el valor del parámetro (nombre)
        self.__cursos=[]#Crea una variable de instancia 'privada' (__cursos) que almacena una lista vacia  
    def agregarCurso(self,nombreCurso):#Crea un método (agregarCurso) que tiene como parámetro (nombreCurso).
        self.__cursos.append(nombreCurso)#A la variable de instancia 'privada'' (__cursos) se le agrega el (nombreCurso) mediante el método append
    def verCursos(self):#Crea un método (verCursos) que no tiene parámetros 
        return self.__cursos#Retorna la variable de instancia 'privada' (__cursos)

class Curso:#Crea una clase llamada (Curso)
    def __init__(self,nombreCurso):#Crea el método constructor de la clase (Curso) que  tiene como parámetro (nombreCurso)
        self.__nombreCurso=nombreCurso #Crea una variable de instancia 'privada' (__nombreCurso) que almacena el valor del parámetro (nombreCurso)

    def getNombreCurso(self):#Crea el método (getNombreCurso) que no tiene parámetros.
        return self.__nombreCurso#Retorna la variable de instancia 'privada' (__nombreCurso)
    
ob=Aprendiz('Miguel')#Crea una instancia de la clase (Aprendiz) que pasa como argumento ('Miguel')
c1=Curso('Python Basico')#crea una instancia de la clade (Curso) que pasa como argumento ('Python Basico')
c2=Curso('Python Intermedio')#crea una instancia de la clade (Curso) que pasa como argumento ('Python Intermedio')
c3=Curso('Java Basico')#crea una instancia de la clade (Curso) que pasa como argumento ('Java Basico')

ob.agregarCurso(c1)#Utiliza el método (agregarCurso) respecto al objeto (ob) que pasa como argumento (c1)
ob.agregarCurso(c2)#Utiliza el método (agregarCurso) respecto al objeto (ob) que pasa como argumento (c2)
ob.agregarCurso(c3)#Utiliza el método (agregarCurso) respecto al objeto (ob) que pasa como argumento (c3)

for curso in ob.verCursos():#Un bucle for que recorre el método (verCursos()) respecto al objeto (ob)
    print(curso.getNombreCurso())#Imprime el método (getNombreCurso()) respecto a (curso) del for

del ob#Elimina la instancia de la clase (Aprendiz) (ob)
#print(ob)
print('.....',c1.getNombreCurso())#Imprime el método (getNombreCurso) respeto al la instancia de la clase (Curso) (c1)
