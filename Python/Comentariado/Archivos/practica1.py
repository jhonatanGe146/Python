from Aprendiz import * #Importa el modulo de Aprendiz
from Curso import * #Importa el modulo de Curso

nombre=input('ingrese nombre del aprendiz')#Pide por teclado un dato str y lo almacena en la variable (nombre)
Documento=int(input('ingrese documento del aprendiz'))#Pide por teclado un dato entero y lo almacena en la variable (documento)
ficha=input('ingrese ficha del aprendiz')#Pide por teclado un dato str y lo almacena

ap=Aprendiz(ficha,nombre,documento)#Instancia un objeto (Aprendiz) que pasa como parámetro (ficha,nombre,documento)

nombreCurso=input('ingrese nombre del curso')#Pide por teclado un dato str y lo almacena en la variable (nombreCurso)
horas=int(input('ingrese intensidad horaria del curso'))#pide por teclado un dato entero y lo almacena en la variable (horas)
c1=Curso(nombreCurso,horas)#Instancia un objeto (Curso) que pasa como parámetro (nombreCurso,horas)
ap.agregarCurso(c1)#Usa el metodo (agregarCurso) respecto a ap

with open('herencia/aprendices.txt','r') as flujo:#Abre el archivo y lo pone en modo lectura ('r', leer) y lo renombra a flujo
    datos=flujo.read()#Almacen los datos resultantes del metodo (read) respecto a flujo en la variable (datos)    
    print(datos)#Imprime la variable (datos)
    #flujo.write('2560664,maria,123')#Esta mal porque abrio el archivo en modo lectura
aprendices=[]#crea una variable (aprendices) y le asigana el valro de una lista vacia
with open('herencia/aprendices.txt','r') as flujo:#Abre el archivo y lo pone en modo lectura ('r', leer) y lo renombra a flujo
    for linea in flujo:#bucle que recorrer los datos del flujo 
        #print(linea)#Imprime la el valor que toma la linea respecto a (flujo)
        aprendices.append(linea.rsplit())#Inserta a la lista aprendices la linea que usa el metodo (rsplit())

datosxlinea=[]#Crea una variable y se le asigna una lista vacia
for aprendiz in aprendices:#bucle que recorre la lista aprendices
    datosxlinea.append(aprendiz[0].split(','))#Inserta a la lista (datosxlinea) el valor de aprendiz en la posicion [0] y que a su vez utiliza el metodo (split()) que tiene como especificador (',')

#print(ob.getNombre())#Imprime el metodo (getNombre) del objeto (ob)

print(datosxlinea)#Imprime la lista (datosxlinea)

listaDeObjetos=[]#Crea una variable y se le asigna una lista vacia
for apr in datosxlinea:#Bucle que recorre la lista de (datosclinea):
     f=apr[0]#variable que almacena el valor de apr de (datosXlinea) en la posicion [0]
     n=apr[1]#variable que almacena el valor de apr de (datosXlinea) en la posicion [1]
     d=apr[2]#variable que almacena el valor de apr de (datosXlinea) en la posicion [2]
     ob=Aprendiz(f,n,d)#Instancia un objeto (Aprendiz) que pasa como parametro las variable mencionadas anteriormente(f,n,d)
     print(ob)#Imprime el objeto ob de la clase (Aprendiz)
     listaDeObjetos.append(ob)#Inserta a la lista (listaDeObjetos) el ob que se crea en la linea anterior

for xx in listaDeObjetos:#Bucle que recorre la lista (listaDeObjetos)
    print(xx.getNombre())#Imprime el metodo (getNombre) del valor que toma xx de (listaDeObjetos) 
    print(xx.getDocumento())#Imprime el metodo (getDocumento) del valor que toma xx de (listaDeObjetos) 
    print(xx.getFicha())#Imprime el metodo (getFicha) del valor que toma xx de (listaDeObjetos) 