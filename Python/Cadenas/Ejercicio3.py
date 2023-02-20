cadena=str (input("Ingrese el texto: "))

#!3- Cuantas veces se repite un caracter dado.
def cont_caracter(cadena):
    for o in cadena:
        m=cadena.count(o)
        print(o, "Se repite", m, "veces")
    return None

#print(cont_caracter(cadena))