"""Ejercicio 8.
Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno.
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad)"""
import sys
sys.path.append('Python/Trimestre_6')

from funciones import f_ejercicio1


#? Función sencilla
def insertAlum (edad):
    mayores=[]
    while True:
        nombre =str(input("Nombre del Alumno: "))
        if nombre =="*":
            print("Los Estudiantes mayores a", edad , "años son: ")
            print(mayores)
            break
        else:
            old = int (input("Edad del Alumno: "))
            if old > edad:
                mayores.append(nombre)
            
# edad= int(input("Ingrese la edad para comparar: "))
# insertAlum(edad)


def registro_alumnos():
    try:
        alumnos =[]
        while True:

            print("Opciones")
            print("1. Registrar Alumnos")
            print("2. Clasificar Alumnos por edad")
            print("3. Salir")
            ctrl = int (input("Selecciona el numeral: "))
            print()
            match ctrl:
                case 1:
                    while True:
                        alumno=[]
                        print("Opciones")
                        print("1. Registrar un Alumno")
                        print("2. salir")
                        ctrl = int (input("Selecciona opción: "))
                
                        match ctrl:
                                case 1:
                                    f_ejercicio1.EscribirCentrado("Datos del Alumno")  
                                    nombre = str (input("Digite el nombre del Alumno: "))
                                    edad = int (input("Digite la edad del Alumno: "))
                                    if edad < 0:
                                        print("La edad debe sermayor a cero")
                                        print("")
                                    else:
                                        alumno.append(nombre)
                                        alumno.append(edad)
                                        alumnos.append(alumno)
                                        print("")
                                case 2:
                                    print("Devuelta al Menu Principal")
                                    print("")
                                    break
                                case _:
                                    print ("Esta opción no existe")
                                    print("")
                     
                case 2:
                    edad = int(input("Alumnos mayores de que edad: "))
                    print (f"Los Alumnos mayores a {edad} son: ")
                    for i in alumnos:
                        if i[1] > edad:
                            print (i[0])
                    print() 
                    
                
                case 3: 
                    print("Programa Finalizado")
                    print (alumnos)
                    break
                case _:
                    print ("Esta opción no existe")
    except ValueError:
        print("Digito un valor no soportado por el sistema (Opcion o edad)")
        print("")
       
    except Exception as e:
        print(e)
registro_alumnos()  