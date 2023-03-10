from Aprendiz import * #Importa el modulo de Aprendiz
from Curso import * #Importa el modulo de Curso

nombre=input('ingrese nombre del aprendiz')#Pide por teclado un dato str y lo almacena en la variable (nombre)
Documento=int(input('ingrese documento del aprendiz'))#Pide por teclado un dato entero y lo almacena en la variable (documento)
ficha=input('ingrese ficha del aprendiz')#Pide por teclado un dato str y lo almacena

ap=Aprendiz(ficha,nombre,documento)#Instancia un objeto (Aprendiz) que pasa como parámetro (ficha,nombre,documento)

nombreCurso=input('ingrese nombre del curso')#Pide por teclado un dato str y lo almacena en la variable (nombreCurso)
horas=int(input('ingrese intensidad horaria del curso'))#pide por teclado un dato entero y lo almacena en la variable (horas)
c1=Curso(nombreCurso,horas)#Instancia un objeto (Curso) que pasa como parámetro (nombreCurso,horas)
ap.agregarCurso(c1)#Usa el metodo (agregarCurso) respecto a ap y le psa con argumento (c1)

with open('herencia/aprendices.txt','a') as flujo: #Abre o crear un archivo que texto que esta ubicado en la ruta relatica (herencia/aprendices.txt) y define el modo de usar esos datos ('a' o escribir) y lo renombra a (flujo)
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')#Agrega  al archivo (aprendices.txt) los valores que retornan cada metodo y da un salto de linea
