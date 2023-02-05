from sys import path
path.append("c:/Users/famil/Documents/Python-1/Python/idioma/tracd/Esp_ing")

import mo2

def cont_esp_ing ():
    print(mo2.esp_ing(mo2.__dic))
    return(mo2.nom , "tiene" , len(mo2.nom), "letras y", mo2.y , len(mo2.y), "letras") 

    
def cont_ing_esp():
    print (mo2.ing_esp(mo2.__dic))
    return (mo2.n , "Tiene" , len(mo2.n) , "letras y" , mo2.x , len(mo2.x) ,"letras")

def contador2():
        while True:
            try:
                print("1- Contar las letras del idioma español a ingles")
                print("2- Contar las letras del idioma ingles a español")
                print("3- salir")
                print()
                g=int (input("Selecciona una opcion: "))
                match g:
                    case 1:
                        print (cont_esp_ing())
                        print()
                    case 2:
                        print (cont_ing_esp())
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
#contador2()