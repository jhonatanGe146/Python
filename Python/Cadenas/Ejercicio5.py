#!5- Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
def tipo_palabra():
    palabra=[]
    silaba="1"
    tilde="áéíóúÁÉÍÓÚ"
    while silaba != "0":
        silaba=str (input("Ingrese las silabas de la palabra: "))
        palabra.append(silaba)
    del palabra[-1]
    print("".join(palabra), "es una")
    for i in palabra:
        for j in i:
            if  j in tilde and j in palabra[-1]:
                print("palabra Aguda")
            elif  j in tilde and j in palabra[-2]:
                print("palabra Grave")
            elif j in tilde and j in palabra[-3]:
                print("palabra Esdrújula")
            elif j in tilde and j in palabra[-4]:
                print("palabra Sobreesdrújula")
            
#tipo_palabra()