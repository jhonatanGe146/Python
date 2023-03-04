class Curso:#Crea una clase llamada (Curso)
    def __init__(self,titulo):#Crea un método constructor que tiene como parámetro (titulo).
        self.__titulo=titulo#Crea una variable de instancia 'privada' (__titulo) que almacena el valor del parámetro (titulo). 

    def getTitulo(self):#Crea un método que no tiene parámatretos y se llama (getTitulo)
        return self.__titulo#Retorna la variable de instancia (__titulo) 

class Aprendiz:#Crea una clase llamada (Aprendiz)
    def __init__(self,nombre):#crea un método constructor que tiene como parámetro (nombre).
        self.__nombre=nombre#Crea una variable  de instancia 'privada' (__nombre) que almacena el valor del párametro nombre.
        self.__cursos=[]#Crea una variable de instancia (__cursos) 'privada' que almacena una lista vaaia

    def agregarCurso(self,nombreCursito):#Crea un método (agregarCurso) que tiene como parámetro (nombreCursito).
        cursito=Curso(nombreCursito)#Crea una variable de instancia 'publica' (cursito) que llama a la clase (Curso) que tiene como parámetro (nombreCursito)
        self.__cursos.append(cursito)#A la variable de instancia 'privada'' (__cursos) se le agrega el (cursito) mediante el método append

    def getCursos(self):#Crea un método llamado (getCursos) que no tine  ningun parámetro
        return self.__cursos#Retorna  la variable de instancia 'privada' (__cursos)
    
ap=Aprendiz('Sofia')#Instancia un objeto de la clase (Aprendiz) y le pasa como argumento ('Sofia')
ap.agregarCurso('Python Basico')#Utiliza el método (agregarCurso) respecto al objeto (ap) y le pasa como argumento ('Python Basico')
ap.agregarCurso('Python Intermedio')#Utiliza el método (agregarCurso) respecto al objeto (ap) y le pasa como argumento ('Python Intermedio')

for c in ap.getCursos():# Un bucle for que recorre el método (getCursos()) respecto al objeto (ap)
    print(c.getTitulo())#Imprime el método (getTitulo()) respecto a  (c) del for

del ap# Elimina la instancia de la clase aprendiz (ap)