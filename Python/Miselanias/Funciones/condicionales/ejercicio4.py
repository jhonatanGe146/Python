"""Pida un numero al usuario que representa días del año. Diga a que mes del año
corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días."""


def months (dias):
    if dias <=365:
        if  dias <= 31:
            return("Enero")
        elif dias <=59:
            return("Febrero")
        elif dias <= 90:
            return("Marzo")
        elif dias <= 120:
            return("Abril")
        elif dias <= 151:
            return("Mayo")
        elif dias <= 181:
            return("Junio")
        elif dias <= 212:
            return("Julio")
        elif dias <=243:
            return("Agosto")
        elif dias <= 273:
            return("Septiembre")
        elif dias <= 304:
            return("Octubre")
        elif dias <= 334:
            return("Noviembre")
        elif dias <=365:
            return("Diciembre")
    else:
        return("!Error¡ un año tiene 365 dias")
dias=int(input("Digita días del año: "))
print (months(dias))