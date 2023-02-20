cadena=str (input("Ingrese el texto: "))

#!1- Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez.
def cont_letra (cad):
    l=[]
    cont=0
    cadena=cad.lower()
    for i in cadena:
        ver= i.isalpha()
        if ver != False:
            if i not in l:
                l.append(i)
                cont+=1
    return cont

#print(cont_letra(cadena))


#!2- Pida una cadena por teclado y diga cual es su valor al sumar sus codigos.
def cont_cod (cadena):
    cont=0
    for i in cadena:
        codigo=ord(i)
        cont+=codigo
    return cont
    
# print(cont_cod(cadena))


#!3- Cuantas veces se repite un caracter dado.
def cont_caracter(cadena):
    for o in cadena:
        m=cadena.count(o)
        print(o, "Se repite", m, "veces")
    return None

#print(cont_caracter(cadena))


#!4- Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas
def cadena_forma(cadena):
    print(cadena.capitalize())#Cambia todas las letras de la cadena a mayúsculas.    
    print(cadena.lower())#Convierte todas las letras de la cadena en minúsculas.       
    print(cadena.swapcase())#Intercambia las mayúsculas y minúsculas de las letras      
    print(cadena.title())#Hace que la primeras letra de cada palabra sea mayúscula.    
    print(cadena.upper())#Convierte todas las letras de la cadena en letras mayúsculas.    
    return ""

#print( cadena_maymis (cadena))


#!5- Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
def tipo_palabra():
    palabra=[]
    silaba="1"
    tilde="""bábébíbóbúcácécícócúdádédídódúfáféfífófúgágégígógúháhéhíhóhújájéjíjójúkákékíkókúlálélílólúmámémímómúnánénínónúñáñéñíñóñúpápépípópúqáqéqí
    qóqúrárérírórúsásésísósútátétítótúvávévívóvúwáwéwíwówúxáxéxíxóxúyáyéyíyóyúzázézízózúbrábrébríbróbrúcrácrécrícrócrúdrádrédrídródrúfráfréfrífrófrúgrá
    grégrígrógrúkrákrékríkrókrúlrálrélrílrólrúprápréprípróprúrrárrérrírrórrútrátrétrítrótrúnéczón"""
    while silaba != "0":
        silaba=str (input("Ingrese las silabas de la palabra: "))
        palabra.append(silaba)
    del palabra[-1]
    print("".join(palabra), "es una")
    if palabra[-1] in tilde:
        print("Palabra Aguda")
    elif palabra[-2] in tilde:
        print("Palabra Grave")
    elif palabra[-3] in tilde:
        print("Palabra Esdrújula")
    elif palabra[-4] in tilde:
        print("Palabra Sobreesdrújula")
            
#tipo_palabra()
    

#!6- Determinar en que tiempo esta conjugado un verbo.
def verb_tiempo(verbo):
    seg_verb=(verbo[-1:])
    seg_verb2=(verbo[-2:-1])
    if seg_verb2 == chr(82) or seg_verb2 == chr (114):
        return ("Verbo en futuro")
    elif seg_verb == chr(225) or seg_verb == chr(193) or seg_verb == chr(233) or seg_verb == chr(201) or seg_verb == chr(237) or seg_verb == chr(205) or seg_verb == chr(243) or seg_verb == chr(211) or seg_verb == chr (250) or seg_verb == chr (218):
        return ("Verbo en Pasado")
    elif seg_verb == chr(97) or seg_verb == chr(65) or seg_verb == chr(101) or seg_verb == chr(69) or seg_verb == chr(105) or seg_verb == chr(73) or seg_verb == chr(111) or seg_verb == chr(79) or seg_verb == chr (117) or seg_verb == chr (85):
        return ("Verbo en presente")

#print (verb_tiempo(cadena))


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


#!8- Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def cifrado (cadena):
    for i in cadena:
        if ord(i) >= 33  and ord (i) <= 62:
            print ((chr(ord(i)-4)), end="")
        elif ord(i) >= 63  and ord (i) <= 93:
            print ((chr(ord(i)-4)), end="")
        elif ord(i) >= 94  and ord (i) <= 126:
            print ((chr(ord(i)+4)), end="")
            
#(cifrado(cadena))    

      
def descifrado(cadena):
        for i in cadena:
            if ord(i) >= 33  and ord (i) <= 62:
                print ((chr(ord(i)+4)), end="")
            elif ord(i) >= 63  and ord (i) <= 93:
                print ((chr(ord(i)+4)), end="")
            elif ord(i) >= 94  and ord (i) <= 126:
                print ((chr(ord(i)-4)), end="")    
            
#(descifrado(cadena))


#!9- Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última.
def sub_cadena (cadena):
    lon=len(cadena)
    for i in range (1,lon):
        print(cadena[0:i+1])

#sub_cadena(cadena)

