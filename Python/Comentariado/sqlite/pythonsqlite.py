import sqlite3 #Importa el módulo sqlite3
#con=sqlite3.connect('C:\\padilla\\sqlite-tools\\db\\pythondb.db')#define una variable (con) y realiza una conexion con la bases de datos mediante la ruta absoluta
con=sqlite3.connect('Python/BasesdeDatos/pythonbd.db')#define una variable (con) y realiza una conexion con la bases de datos mediante la ruta relativa
print(type(con))#Imprime el tipo de dato de la variable (con)
micursor=con.cursor()#Define una variable (micurso) y crea un curso utilizando la conexion de la variable (con).
print(type(micursor))#Imprime el tipo de dato de la variable (micursor)
new_sql="SELECT * from Persona;"#Define una variable (new_sql) y le asigna un string que es una sentencia sql.
micursor.execute(new_sql)#mediante la variable (micursor) utiliza el método (execute) para ejecutar el contenido de la variable (new_sql) 
lista=micursor.fetchall()#Define una variable (lista) y se le asigna el método (fetchall)  respecto a la variable(micursor) que muestra todo lo relacionado con la consulta
for fila in lista:#Define un  bucle for que tiene como variable de iteracion (fila) para recorrer la variable (lista) 
    print(fila[0])#Imprime la variable de iteracion (fila) en la posicion [0]
    print(fila[1])#Imprime la variable de iteracion (fila) en la posicion [1]
    print(fila[2])#Imprime la variable de iteracion (fila) en la posicion [2]
    print(fila[3])#Imprime la variable de iteracion (fila) en la posicion [3]
    print('*'*50)#Imprime un string ('*') multiplicado por 50, es decir 50 *