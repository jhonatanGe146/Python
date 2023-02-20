cadena=str (input("Ingrese el texto: "))

#!7- De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.
def cont_caracter (cadena):
    vocal=0
    vocal_tilde=0
    consonante=0
    carac_espe=0
    numero=0
    cadena_minus= cadena.lower()
    for i in cadena_minus:
        if i in "aeiou":
            vocal+=1
        elif i in "áéíóú":
            vocal_tilde+=1
        elif ord (i) >= 65 and ord (i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
            consonante+=1
        elif ord (i) >= 48 and ord (i) <= 57 :
            numero+=1
        else:
            carac_espe+=1
    print(cadena, "tiene: ")
    print(vocal, "vocales")
    print(vocal_tilde, "vocales con tilde")       
    print(consonante, "Consonantes")     
    print (carac_espe, "caracteres especiales")
    print(numero, "numeros")       
            
#cont_caracter(cadena)