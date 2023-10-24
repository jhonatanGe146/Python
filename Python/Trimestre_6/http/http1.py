import requests
url = "https://hotelskiline.000webhostapp.com/index.html"

respuesta = requests.get(url) 
print (type(respuesta)) 
#print (respuesta.content) # * Imprime el contenido de la URL
#print (respuesta.status_code) # * Saber si el sitio esta activo (200) o no lo encuntra (404)


if respuesta.status_code == 200:
    flujo = open("index.html", 'wb')
    flujo.write(respuesta.content)

# * r+ hace update y lee
# * a+ hace update pero no lee
# * w+ escribe
# * wb