n= int(input("Igrese número: "))
fact=1


bac=int(input("ingrese poblacion inicial: "))
bac1=bac*2
p=float(input("ingresar porcentaje de crecimiento"))
while bac<bac1:
    print(bac)
    bac=bac+(bac*p)
    print ("Bacterias= ", bac)
