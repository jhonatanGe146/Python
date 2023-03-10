flujo=open('archivos/inicio.txt','w')
#datos=flujo.read()
#print(datos)
for i in range(10):
    flujo.write('\n ',i)
datos=flujo.read()
print(datos)


#Para crear o Llamar un archivo se debe saver ya sea la ruta absoluta o relativa.
#Si el archivo no esta creado se creara
#Existen un metodo open para abrir o crear el archivo
#Se tiene que poner como parámetro el nombre del archivo y como lo quiere usar (r: leer. w: escribir a: actualizar)
# Se debe cerrar el archivo (close())

