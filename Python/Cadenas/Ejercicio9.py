cadena=str (input("Ingrese el texto: "))

#!9- Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última.
def sub_cadena (cadena):
    lon=len(cadena)
    for i in range (1,lon):
        print(cadena[0:i+1])

#sub_cadena(cadena)

