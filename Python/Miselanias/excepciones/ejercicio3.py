

while True:
    print("Opcion 1 para resolver la ecuacion de forma porsitiva:")
    print("Opcion 2 para resolver la ecuacion de forma negativa:")
    print("Opcion 3 para salir:")
    control=int(input("seleccione la opcion:\n"))
    match(control):
        
        case 1:
            while True:
                    try:
                        a=float (input ("ingresar a: "))
                        b=float (input ("ingresar  b: "))
                        c=float (input ("ingresar c: "))
                        x= ((-(b)+((b ** 2 - 4*a*c) ** 0.5) ))
                        if x >= 0:
                            x= x / (2 * a)
                            print (" El resultado de la función cuadratica positiva es: ", x)
                        else:
                            print ("resultado incorrecto")
                    except ZeroDivisionError:
                        print("indeterminacion ")
                    except:
                        print("datos no soportados")
                    break
        case 2:
            while True:
                    try:
                        a=float (input ("ingresar a: "))
                        b=float (input ("ingresar  b: "))
                        c=float (input ("ingresar c: "))
                        x= ((-(b)-((b ** 2 - 4*a*c) ** 0.5) ))
                        
                        x= x / (2 * a)
                        print (" El resultado de la función cuadratica positiva es: ", x)
                        
                        
                    except ZeroDivisionError:
                        print("indeterminacion ")
                    except:
                        print("datos no soportados")
                    break
        case 3:
            print("saliste")
            break
        case _:
            print("esta opcion no existe")