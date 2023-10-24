import requests
url = "https://httpbin.org/get?salon=1&estudiante=Jenna"

respuesta = requests.get(url) 
# print (type(respuesta)) 
# print (respuesta.content.decode())
#print (respuesta.content) # * Imprime el contenido de la URL
#print (respuesta.status_code) # * Saber si el sitio esta activo (200) o no lo encuntra (404)


