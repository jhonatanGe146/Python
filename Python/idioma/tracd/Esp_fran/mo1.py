d={
"caballo":"cheval",
"vaca":"vache",
"cerdo":"cochon",
"cabra":"chévre",
"burro":"âne",
"oveja":"mouton",
"pollo":"poulet",
"pato":"canard",
"pavo":"dinde",
"ganso":"oie",
"conejo":"lapin",
"león":"lion",
"tigre":"tigre",
"elefante":"élépha",
"jirafa":"girafe",
"hipopótamo":"hippopotame",
"rinoceronte":"rhinocéros",
"cebra":"zébre",
"mono":"singe",
"cocodrilo":"crocodile",
"canguro":"kangouro",
"oso":"ours",
"lobo":"loup",
"pájaro":"oiseau",
"pez":"poisson",
"delfin":"dauphin",
"ballena":"baleine",
"foca":"phoque",
"tiburón":"requin",
"pinguino":"pingouin",
"calamar":"calamar",
"medusa":"méduse",
"langosta":"homard",
"cangrejo":"crabe",
"nutria":"loutre"
}


def esp_fran (dic):
    global n,x
    n=str(input("Animal a traducir: "))
    if n in dic:
        for i in dic.keys():
            if n == i:
                x=dic[i]
                return n, "es", x
    else:
        return "El animal no esta en el diccionario"
        
        
def fran_esp (dic):
    global nom, y
    clave=list(dic.keys())
    valor=list(dic.values())
    nom=str(input("animal a traducir: "))
    if nom in valor:
        for i in range (len(valor)):
            if nom == valor[i]:
                y=clave[i]
                return nom, "es", y
    else:
        return "El animal no esta en el diccionario"
                  
        
def traducir ():        
    while True:
        try:
            print()
            print("1- traduce de español a frances")
            print("2- traduce de frances a español")
            print("3-salir")
            x=int(input("Selecciona a cual idioma quieres traducir: "))
            match x:
                case 1:
                    print (esp_fran(d))
                    print()
                case 2:
                    print(fran_esp(d))
                    print()
                case 3:
                    return("Saliste")
                    break
                case _:
                    print("Esta opcion no existe")
        except:
            print("Ingreso un valor no soportado por el sistema")
#print(traducir())