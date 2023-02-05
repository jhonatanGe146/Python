d={
"horse":["herbívoro","dormir de die", "correr"],
"cow":["herbívoro", "rumiar","comer"],
"pig":["omnívoro", "revolcar", "dormir"],
"sheep":["herbívoro", "correr", "pastorear"],
"chicken":["herbívoro", "planear", "comer", "poner huevos"],
"goose":["herbívoro", "volar", "comer", "poner huevos"],
"turkey":["omnívoro", "sonidos", "comer", "caminar"],
"duck":["herbívoro", "volar", "nadar", "comer"],
"rabbiit":["herbívoro", "correr", "comer", "saltar"],
"lion":["carnívro", "cazar","comer","manada"],
"tiger":["carnívro","cazar", "comer", "trepar"],
"giraffe":["herbívoro", "comer", "correr", "manada"],
"hippo":["herbívoro", "nadar", "comer"],
"monkey":["omnívoro", "trepar", "comer", "saltar","columpiar"]
}

def accion_ing(dic):
    nombre=str(input("Escribe el nombre del animal en ingles: "))
    if nombre in dic:
        for i in dic.keys():
            if nombre == i:
                return(nombre, dic[i])
    else:
        return "El animal NO esta en la diccionario"
    
#print (accion_ing(d))