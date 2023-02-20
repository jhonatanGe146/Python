cadena=str (input("Ingrese el texto: "))

#!2- Pida una cadena por teclado y diga cual es su valor al sumar sus codigos.
def cont_cod (cadena):
    cont=0
    for i in cadena:
        codigo=ord(i)
        cont+=codigo
    return cont
    
# print(cont_cod(cadena))
