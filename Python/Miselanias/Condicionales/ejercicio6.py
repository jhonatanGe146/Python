"""Pida un numero al usuario que representa días del año. Diga a que mes del año
corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días."""

dias=int(input("Digita días del año: "))
if dias <=365:
    if  dias <= 31:
        print("Enero")
    elif dias <=59:
        print("Febrero")
    elif dias <= 90:
        print("Marzo")
    elif dias <= 120:
        print("Abril")
    elif dias <= 151:
        print("Mayo")
    elif dias <= 181:
        print("Junio")
    elif dias <= 212:
        print("Julio")
    elif dias <=243:
        print("Agosto")
    elif dias <= 273:
        print("Septiembre")
    elif dias <= 304:
        print("Octubre")
    elif dias <= 334:
        print("Noviembre")
    elif dias <=365:
        print("Diciembre")
else:
    print("!Error¡ un año tiene 365 dias")