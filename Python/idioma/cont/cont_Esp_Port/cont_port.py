from sys import path
path.append("c:/Users/famil/Documents/Python-1/Python/idioma/tracd/Esp_por")

import mo3

def cont_esp_por():
    print(mo3.esp_port(mo3.dic_port))
    return(mo3.palabra , "tiene" , len(mo3.palabra), "letras y", mo3.ind , len(mo3.ind), "letras") 

    
def cont_por_esp():
    print (mo3.port_esp(mo3.dic_port))
    return (mo3.a , "Tiene" , len(mo3.a) , "letras y" , mo3.j , len(mo3.j) ,"letras")

def contador3():
        while True:
            try:
                print("1- Contar las letras del idioma español a portugues")
                print("2- Contar las letras del idioma portugues a español")
                print("3- salir")
                print()
                g=int (input("Selecciona una opcion: "))
                match g:
                    case 1:
                        print (cont_esp_por())
                        print()
                    case 2:
                        print (cont_por_esp())
                        print()
                    case 3:
                        return("saliste")
                        break
                    case _:
                        print("No existe esta opcion")
                        print()
            except:
                print("Ingreso un valor no soportado por el sistema")
                print()
#contador3()