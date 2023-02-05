__dic= {
"bull":"toro",
"cow":"vaca",
"chicken":"pollo",
"hen":"gallina",
"rooster":"gallo",
"chick":"pollito",
"donkey":"burro",
"goat":"cabra",
"horse":"caballo",
"pig":"cerdo",
"rabbit":"conejo",
"sheep":"oveja",
"turkey":"pavo",
"goose":"ganso",
"llama":"llama",
"prawn":"langostino",
"shrimp":"gamba",
"crab":"cangrejo",
"dolphin":"delfín",
"shark":"tiburón",
"eel":"anguila",
"whale":"ballena",
"jellyfish":"medusa",
"lobster":"langosta",
"octopus":"pulpo",
"oyster":"ostra",
"almeja":"clam",
"seal":"foca",
"squid":"calamar",
"hake":"merluza",
"sardine":"sardina",
"tunafish":"atún",
"cod":"bacalao",
"bass":"lubina",
"trout":"trucha",
"salmon":"salmón",
"boar":"jabalí",
"deer":"ciervo", 
"mouse":"ratón",
"racoon":"mapache",
"squirrel":"ardilla",
"beaver":"castor",
"otter":"nutria",
"bear":"oso ",
"moose":"alce" ,
"falcon":"halcón",
"eagle":"águila",
"hummingbird":"colibrí",
"crow":"cuervo",
"owl":"búho",
"stork":"cigüeña",
"swan":"cisne",
"duck":"pato",
"pigeon":"paloma",
"monkey":"mono",
"cobra":"cobra",
"gorilla":"gorila",
"sloth":"perezoso",
"parrot":"loro",
"tiger":"tigre",
"python":"pitón",
"cat":"gato",
"leopard":"leopardo",
"elephant":"elefante",
"giraffe":"jirafa",
}

def ing_esp (dic):
    global n,x
    n=str(input("Animal a traducir: "))
    if  n in dic:
        for i in dic.keys():
            if n == i:
                x=dic[i]
                return n, "es", x
    else:
        return "El animal No esta en la diccionario "
def esp_ing (dic):
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
            print("1- traduce de ingles a español")
            print("2- traduce de español a ingles")
            print("3-salir")
            x=int(input("Selecciona a cual idioma quieres traducir: "))
            match x:
                case 1:
                    print (ing_esp(__dic))
                    print()
                case 2:
                    print(esp_ing(__dic))
                case 3:
                    return("Saliste")
                    break
                case _:
                    print("Esta opcion no existe")
        except:
            print("Ingreso un valor no soportado por el sistema")

#print (ing_esp(__dic))
#print(esp_ing(__dic))
#traducir()