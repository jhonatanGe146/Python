"""generar dissionario canciones diccionario duración
artita
Genero 
duracion

buscar por artista 
cancion
anexar cancion 
eliminar artista
buscar canciones 
anexar artista
ordenar alfabeticamente 
el que tiene mas  canciones 
el que tiene  las cancion mas larga 
el que tiene la cancion mas corta """


listareproduccion={}
                   
              

# funcion buscar
def artista (playlist):
    artis=input("Nombre del cantante que quieres buscar: ")
    if artis in playlist:
        print(playlist[artis])
        
    else:
        print("El artista no se encuenta")

#funcion agregar artitas
def agregarArtista(playlist):
        y=input("Escribe el nombre del artista que quieres agregar\n")
        playlist[y]={}
        print(playlist)
        return 1
    
#Agregar cancion
def agregarCancion (playlist):
    artiscan=input("Nombre del artista al que le quieres agregar una cancion:\n")
    if artiscan in playlist:
        c=input("Nombre de la cancion que quieres agregar:\n")
        g=input("genero de la cancion:\n")
        d=int (input("minutos y segundos de  duracion de la cancion:\n"))
        playlist[artiscan].update({'cancion':c,'genero':g,'duracion':d})
        print(playlist)
    else:
        print("Agrega al artista primero")
#Eliminar artista
def eliminarArtista(playlist):
    eliminar=input("Nombre del artista que quieres eliminar\n")
    del playlist[eliminar]
    print(playlist)
#organizar playlist
def ordenarLista(playlist):
    sorted(playlist.keys())
    print(playlist)
#buscar cancion
def buscar_cancion(playlist):
    x=input("Nombre de la cancion que quieres buscar:\n")
    for y in playlist.keys():
        if x in playlist[y]["cancion"]:
            print("Si esta")
        else:
            print("no esta")
def mas_canciones(playlist):
    for y  in playlist.keys(): 
        cont=0
        for x in playlist.values():
            if x in playlist[y]["cancion"]:
                cont+=1
                if cont >= cont:
                    print(playlist[y])
                



while True:
    print("1-Buscar artista")
    print("2-Agregar artista")
    print("3-Agregar cancion")
    print("4-Agregar eliminar artista")
    print("5-organizar playlist")
    print("6-Buscar cancion")
    print("7-Salir")
    ctrl=int(input("Selecciona la opcion: "))
    match ctrl:
        case 1:
            print("selecciono la opcion 1")
            artista(listareproduccion)
            print()
        case 2:
            print("selecciono la opcion 2")
            agregarArtista(listareproduccion)
            print()
            
        case 3:
            print("selecciono la opcion 3")
            agregarCancion(listareproduccion)
            print()
        case 4:
            print("selecciono la opcion 4")
            eliminarArtista(listareproduccion)
            print()
        case 5:
            ordenarLista(listareproduccion)
            print()
        case 6:
            buscar_cancion(listareproduccion)
            print()
        case 7:
                print("saliste")
                break
        case _:
            print("opcion no disponible")
            print()
mas_canciones(listareproduccion)