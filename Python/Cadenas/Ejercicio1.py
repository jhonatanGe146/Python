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

print(cont_letra(cadena))
