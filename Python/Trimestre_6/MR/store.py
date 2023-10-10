import sqlite3 as s
import sys
sys.path.append('Python/Trimestre_6')

from funciones import f_ejercicio1 as centrar

#! Creación de la base de batos
# conexion = sqlite3.connect("bd_store.db")
# cursor = conexion.cursor()
# cursor.execute("""CREATE TABLE cliente (
#     nro_documento VARCHAR (10) PRIMARY KEY,
# 	  nombre_cli VARCHAR (70),
#     email_cli VARCHAR (100),
#     movil_cli VARCHAR (12),
#     dirreccion_cli VARCHAR (70)
# );""") 
# conexion.commit()
# conexion.close()
#! -------------------------
conexion=s.connect('Python/BasesdeDatos/bd_store.db')#define una variable (cone) y realiza una conexion con la bases de datos mediante la ruta relativa
cursor=conexion.cursor()#Define una variable (micurso) y crea un curso mediante la variable(cone).
class customer ():# Estructura de una clase
    def __init__(self, nro_documento, nombre_cli, email_cli, movil_cli, dirreccion_cli):
        self.__nro_documento = nro_documento
        self.__nombre_cli = nombre_cli
        self.__email_cli = email_cli
        self.__movil_cli = movil_cli
        self.__dirreccion_cli = dirreccion_cli
        cursor.execute("""INSERT INTO cliente VALUES (?, ?, ?, ?, ?)""",
                       (self.__nro_documento, self.__nombre_cli, self.__email_cli, self.__movil_cli, self.__dirreccion_cli))
        conexion.commit()
        conexion.close()
    def login(self, email, nro_doc):
        cursor.execute("SELECT * FROM cliente WHERE email_cli = ? AND nro_documento = ?", (email, nro_doc))

        # Obtener los resultados de la consulta
        resultado = cursor.fetchone()

        if resultado:
            print("Inicio de sesión exitoso.")
            # Aquí puedes realizar acciones adicionales si el inicio de sesión es exitoso
        else:
            print("Inicio de sesión fallido. Verifica tu correo electrónico y número de documento.")

        # Cerrar la conexión
        conexion.close()

    
  
def sistema ():
    centrar.EscribirCentrado("Bienvenidos a Senator")
    print("Funciones Del Sistema")
    print("1. Registrarse")
    print("2. Login")
    
    ctrl = int (input("Selecciona opción: "))
    match ctrl:
        case 1:
            nro_doc= str (input("Digite Su Número de Documento: "))
            nombre= str (input("Digite Su Primer Nombre y Apellido: "))
            email= str (input("Digite Su Correo Electronico: "))
            movil= str (input("Digite Su Telefeno: "))
            direccion= str (input("Digite Su Dirrecion De Residencia: "))
            customer(nro_doc, nombre, email, movil, direccion)
            print()
        case 2:
            email = input("Digite Su Correo Electrónico: ")
            nro_doc = input("Digite Su Número de Documento: ")
            
            # Verificar si el cliente existe y si las credenciales son correctas
            cursor.execute("SELECT * FROM cliente WHERE nro_documento = ? AND email_cli = ?", (nro_doc, email))
            cliente_existente = cursor.fetchone()
            
            if cliente_existente:
                print("Inicio de sesión exitoso.")
                # Aquí puedes permitir el acceso al sistema al cliente existente
            else:
                print("Inicio de sesión fallido. Verifica tus credenciales.")
            
            
            
       
   
 
sistema()
   
   
    
    
    
    
    
    
def hh ():
    cursor.execute("""SELECT * FROM cliente""")

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Mostrar los resultados
    for fila in resultados:
        print(fila)

    # Cerrar la conexión
    conexion.close()
##hh()