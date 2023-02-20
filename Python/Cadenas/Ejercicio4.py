cadena=str (input("Ingrese el texto: "))

#!4- Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas
def cadena_forma(cadena):
    print(cadena.capitalize())#Cambia todas las letras de la cadena a mayúsculas.    
    print(cadena.lower())#Convierte todas las letras de la cadena en minúsculas.       
    print(cadena.swapcase())#Intercambia las mayúsculas y minúsculas de las letras      
    print(cadena.title())#Hace que la primeras letra de cada palabra sea mayúscula.    
    print(cadena.upper())#Convierte todas las letras de la cadena en letras mayúsculas.    
    return ""

#print( cadena_maymis (cadena))