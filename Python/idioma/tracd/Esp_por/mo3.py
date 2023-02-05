dic_port={
"gato":"gato",
"cao":"perro",
"hamster":"hamster",
"galinha":"gallina",
"ganso":"ganso",
"cabra":"cabra",
"touro":"toro",
"vaca":"vaca",
"ovelha":"oveja",
"galo":"gallo",
"cavalo":"caballo",
"leao":"leon",
"esquilo":"ardilla",
"morcego":"murcielago",
"girafa":"jirafa",
"coelho":"conejo",
"golfinho":"delfin",
"aranha":"araña",
"formiga":"hormiga",
"pinguim":"pinguino",
"rato":"raton",
"furao":"huron",
"urso":"oso",
"macaco":"mono",
"falcao":"halcon"
}
def port_esp(_dr):
    global a,j
    a=str(input("Ingrese un animal para traducir: "))
    if a in _dr:
        for i in _dr.keys():
            if i == a:
                j=_dr[i]
                return (a,"es:",_dr[i])
    else:
        return "El animal NO esta en la lista"

def esp_port(x):
    global palabra, ind
    palabra=(input("Ingrese animal para traducir: "))
    claves=list(x.keys())
    valores=list(x.values())
    if palabra in valores:
        for i in range(len(valores)):
            if palabra == valores[i]:
                ind=claves[i]
                return (palabra,"es:",ind)
    else:
        return "El animal no esta en el diccionario"
            

def traducir ():
    while True:
        try:
            print()
            print("1- traduce de portugues a español")
            print("2- traduce de español a portugues")
            print("3-salir")
            xcz=int(input("Selecciona las opciones que desees: "))
            match xcz:
                case 1:
                    print (port_esp(dic_port))
                    print()
                case 2:
                    print(esp_port(dic_port))
                case 3:
                    return "Saliste"
                    break
                case _:
                    print("Esta opcion no existe")
        except:
            print("Ingreso un valor no soportado por el sistema")
            
#print(traducir())