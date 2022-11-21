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
                            "cancion " "perdedor ", 
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
def artista (artis, playlist):
    if artis in playlist:
        print(playlist[artis])
        return 1
    else:
        print("El artista no se encuenta")
        return 2

#funcion agregar artitas
def agregarArtista(veri, playlist):
    if veri ==2:
        y=input("Escribe el nombre del artista que quieres agregar\n")
        playlist[y]=()
        print(playlist)
        return 1
#Agregar cancion
def agregarCancion (artis,playlist):
    if x ==1:
        c=input("Nombre de la cancion que quieres agregar:\n")
        g=input("genero de la cancion:\n")
        d=input("duracion de la cancion:\n")
        dici=("cancion", c,"duracion", d,"genero", g)
        playlist[artis]+=dici
        print(playlist)
    else:
        print("Debes agregar el artista primero")

cantante=input ("Escribe el nombre del artita que quieres buscar:\n")

x= artista(cantante,listareproduccion)


#funciones
agregarArtista(x, listareproduccion)
x= artista(cantante,listareproduccion)
artiscan=input("Nombre del artista al que le quieres agregar una cancion:\n")
agregarCancion(artiscan, listareproduccion)
















"""

x=str(input("ingrese el artista:"))
artista(x,listareproduccion)

"""