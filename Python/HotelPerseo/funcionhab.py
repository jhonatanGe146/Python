import sqlite3 
conex=sqlite3.connect('Python/BasesdeDatos/Perseo.db')
curshab=conex.cursor()


def seleccion():
    sentencia=f"SELECT * FROM tb_habitacion"# WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=curshab.execute(sentencia)
    return lista.fetchall()

#print(selects('persona','id','>','400'))

def updatehab():
    campo=str(input('Ingrese el campo a actualizar: '))
    dato=input('Dato a actualizar: ')
    num=int(input('número de habitación a actualizar: '))
    sentencia=f"UPDATE tb_habitacion SET {campo}='{dato}'WHERE habi_idhabitacion='{num}'"
    print(sentencia)
    curshab.execute(sentencia)
    conex.commit()
    print('Modificación Exitosa!!!!')

#modificar('persona','first_name','Faustino',2)

def deletehab():
    dato=int(input('Número de la habitación que quiere eliminar: '))
    sentencia=f"DELETE FROM tb_habitacion WHERE habi_idHabitacion='{dato}'"
    curshab.execute(sentencia)
    conex.commit()
    print('Eliminación Exitosa!!!!')

#eliminar('persona','first_name','Neda')

def inserthab():
    ids=int(input('Ingrese número de la habitación: '))
    dp=str(input('Escriba la descripción de la habitación: '))
    th=int(input('Ingrese el tipo de habitación: '))
    eh=int(input('Ingrese el estado de la habitación: '))
    sentencia=f"INSERT INTO tb_habitacion VALUES ('{ids}','{dp}',{th},{eh})"
    curshab.execute(sentencia)
    conex.commit()
    print('Registro Creado!!!!')


#inserthab()
#deletehab()
updatehab()
print(seleccion()) 