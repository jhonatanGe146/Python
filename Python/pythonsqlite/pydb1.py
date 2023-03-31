import sqlite3 as s #importa el módulo sqlite3 y lo remombra a s
cone=s.connect('Python/BasesdeDatos/Pythonbd.db')#define una variable (cone) y realiza una conexion con la bases de datos mediante la ruta relativa
print(type(cone))#Imprime el tipo de dato de la variable (cone)
micurso=cone.cursor()#Define una variable (micurso) y crea un curso mediante la variable(cone).
print(type(micurso))