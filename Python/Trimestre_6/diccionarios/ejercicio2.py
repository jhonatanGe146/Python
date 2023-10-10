"""Ejercicio 2.
Escribe un programa que lea una cadena y devuelva un diccionario 
con la cantidad de apariciones de cada carácter en la cadena."""




def count_caracter():
    try:
        texto= str (input("Ingresa el texto: "))
        diccionario_texto = {}
        
        for i in texto:
            if i in diccionario_texto:
                diccionario_texto[i]+=1
            else:
                diccionario_texto[i]=1
                
        
        print("Diccionario Caracter Cantidad")
        for k in diccionario_texto.items():
            clave , valor = k
            print(f"{clave} = {valor} ")


            
    except ValueError:
        print ("ERROR!! Debe ingresar un numero")
        count_caracter()


count_caracter()
