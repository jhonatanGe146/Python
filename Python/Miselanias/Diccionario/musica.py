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


listareproduccion={"maluma" :(
                            "perdedor ", 
                            "duracion " "3:27", 
                            "genero " "reggaeton"
                            ),
                   "morat": (
                            "cancion ""besos en guerra", 
                            "duracion " "3:51" , 
                            "genero " "romance"
                            ),
                    "INTERWORLD": (
                                "cancion ""metamorfosis",
                                "duracion " "2:22",
                                "genero " "phonk"                                                                 
                            ),
                    "metallica": (
                                "cancion " "enter sandmman",
                                "duracion "  "5:31",
                                "genero " "rock"
                                ),
                    "sebastian yatra": (
                                "canciones ""ojos marrones",
                                "duracion " "3:18",
                                "genero ""urbano"
                                ),
                    "luis miguel": (
                                "cancion ""ahora te puedes marchar",
                                "duracion " "3:11",
                                "genero ""pop"
                    )
                    
                    }
              

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
        playlist[y]=()
        print(playlist)
        return 1
    
#Agregar cancion
def agregarCancion (playlist):
    artiscan=input("Nombre del artista al que le quieres agregar una cancion:\n")
    c=input("Nombre de la cancion que quieres agregar:\n")
    g=input("genero de la cancion:\n")
    d=input("duracion de la cancion:\n")
    dici=("cancion", c,"duracion", d,"genero", g)
    playlist[artiscan]+=dici
    print(playlist)
#Eliminar artista
def eliminarArtista(playlist):
    eliminar=input("Nombre del artista que quieres eliminar\n")
    del playlist[eliminar]
    print(playlist)
#organizar playlist
def ordenarLista(playlist):
    sorted((playlist.keys()))
    print(playlist)

while True:
    print("1-Buscar artista")
    print("2-Agregar artista")
    print("3-Agregar cancion")
    print("4-Agregar eliminar artista")
    print("5-organizar playlist")
    print("6-Salir")
    ctrl=int(input("Selecciona la opcion: "))
    match ctrl:
        case 1:
            print("selecciono la opcion 1")
            x= artista(listareproduccion)

            print()
        case 2:
            print("selecciono la opcion 2")
            agregarArtista(listareproduccion)
            
        case 3:
            print("selecciono la opcion 3")
            agregarCancion(listareproduccion)
        case 4:
            print("selecciono la opcion 4")
            eliminarArtista(listareproduccion)
        case 5:
            ordenarLista(listareproduccion)
        case 6:
                print("saliste")
                break
