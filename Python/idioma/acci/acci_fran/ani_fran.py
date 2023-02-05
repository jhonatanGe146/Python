global d

d={
"cheval":["herbívoro","dormir de die", "correr"],
"vache":["herbívoro", "rumiar","comer"],
"cochon":["omnívoro", "revolcar", "dormir"],
"mouton":["herbívoro", "correr", "pastorear"],
"poulet":["herbívoro", "planear", "comer", "poner huevos"],
"canard":["herbívoro", "volar", "comer", "poner huevos"],
"dinde":["omnívoro", "sonidos", "comer", "caminar"],
"oie":["herbívoro", "volar", "nadar", "comer"],
"lapin":["herbívoro", "correr", "comer", "saltar"],
"lion":["carnívro", "cazar","comer","manada"],
"tigre":["carnívro","cazar", "comer", "trepar"],
"girafe":["herbívoro", "comer", "correr", "manada"],
"hippopotame":["herbívoro", "nadar", "comer"],
"singe":["omnívoro", "trepar", "comer", "saltar","columpiar"]
}

def accion_fran(dic):
    nombre=str(input("Escribe el nombre del animal en frances: "))
    if nombre in dic:
        for i in dic.keys():
            if nombre == i:
                return(nombre, dic[i])
    else:
        return "El animal NO esta en la diccionario"
    
#print (accion_fran(d))