cadena=str (input("Ingrese el texto: "))

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
