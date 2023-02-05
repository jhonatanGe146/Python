d={
"cavalo":["herbívoro","dormir de die", "correr"],
"vaca":["herbívoro", "rumiar","comer"],
"porco":["omnívoro", "revolcar", "dormir"],
"ovelha":["herbívoro", "correr", "pastorear"],
"frango":["herbívoro", "planear", "comer", "poner huevos"],
"ganso":["herbívoro", "volar", "comer", "poner huevos"],
"turkey":["omnívoro", "sonidos", "comer", "caminar"],
"peru":["herbívoro", "volar", "nadar", "comer"],
"coelho":["herbívoro", "correr", "comer", "saltar"],
"leão":["carnívro", "cazar","comer","manada"],
"tigre":["carnívro","cazar", "comer", "trepar"],
"girafa":["herbívoro", "comer", "correr", "manada"],
"hipopótamo":["herbívoro", "nadar", "comer"],
"macaco":["omnívoro", "trepar", "comer", "saltar","columpiar"]
}


def accion_port(dic):
    nombre=str(input("Escribe el nombre del animal en portugues: "))
    if nombre in dic:
        for i in dic.keys():
            if nombre == i:
                return(nombre, dic[i])
    else:
        return "El animal NO esta en la diccionario"
    
#print (accion_port(d))