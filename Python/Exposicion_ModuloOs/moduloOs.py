
#!Módulo os
'''Este módulo permite interactuar con tu sistema operativo usando Python,
Esto lo hace por medio de funciones tanto para Unix como Windows'''


'''Las funciones permiten operar con archivos y directorios, ademas de obtener
información sobre el sistemas operativo, manejar procesos u operar Stream de E/S
usando descriptores'''

import os

#!Obtener información sobre el sistema operativo
#? Función uname() devuelve como atributos:
# systemname: almacena el nombre del sistema operativo.
# nodename: almacena el nombre de la máquina en la red.
# release: almacena el release (actualización) del sistema operativo.
# version: almacena la versión del sistema operativo.
# machine: almacena el identificador de hardware, por ejemplo, x86_64.

#print(os.uname())


#?Función name() distigue el sistema operativo.
# posix: obtendrás este nombre si usas Unix.
# nt: obtendrás este nombre si usas Windows.
# java: obtendrás este nombre si tu código está escrito en Jython.

# print(os.name())

import platform
#print(platform.uname())


#! Creando directorios en Python.

#?Función mkdir() crea un directorio ya sea con ruta relativa o absoluta.
    #d:/Python/Python/Exposicion_ModuloOs
    #Python/Exposicion_ModuloOs
#os.mkdir('Python/Exposicion_ModuloOs/prueba_directorio')
    #Hay Ten en cuenta que ejecutar el programa dos veces generará un FileExistsError.
    #Ademas se puede pasar un argumento mode para especificar los permisos del directorio.
#?Función listdir() devuelve una lista que contiene los nombres de los archivos
#? y directorios que se encuentran en la ruta pasada como argumento.

#print(os.listdir())



#!Creación recursiva de directorios.
#?Función makedirs() permite la creación recursiva de directorios:

#os.makedirs('Python/Exposicion_ModuloOs/prueba_directorio/directorio_recursivo')
#print(os.listdir())


#?Función chdir() para moverse entre directorio, cambia el directorio de trabajo actual.
#os.chdir('Python/Exposicion_ModuloOs/prueba_directorio')


#?Función getcwd() devuelve la información solo el directorio de trabajo actual
print(os.getcwd())


#?Función rmdir() Eliminar directorios vacios.
#os.rmdir('Python/Exposicion_ModuloOs/prueba_directorio/directorio_recursivo')

#?Funcion removedirs() elimina un directorio y sus subdirectorios.
#os.removedirs('directorio_recursivo')

#?Función system()  ejecuta un comando que se le pasa como cadena.

value = os.system("mkdir directorio_con_system")
print(value)
