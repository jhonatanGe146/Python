from sys import path
path.append("c:/Users/famil/Documents/Python-1/Python/idioma/tracd/Esp_fran")

import mo1

def cont_esp_fran ():
    print(mo1.esp_fran(mo1.d))
    return(mo1.n , "tiene" , len(mo1.n), "letras y", mo1.x , len(mo1.x), "letras") 

    
def cont_fran_esp():
    print (mo1.fran_esp(mo1.d))
    return (mo1.nom, "Tiene" , len(mo1.nom) , "letras y" , mo1.y , len(mo1.y) ,"letras")

def contador():
        while True:
            try:
                print("1- Contar las letras del idioma español a frances")
                print("2- Contar las letras del idioma frances a español")
                print("3- salir")
                print()
                g=int (input("Selecciona una opcion: "))
                match g:
                    case 1:
                        print (cont_esp_fran())
                        print()
                    case 2:
                        print (cont_fran_esp())
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
#contador()