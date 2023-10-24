import requests
import json

"""Uso de los verbos HTPP"""

#! Uso del verbo GET
url ='https://httpbin.org/get'
argumentos = {"Nombre":"Andres", "Apellido": "Rodriguez", "Edad":18}
head= {'content-type': 'application/json', 'access-token': b'12332'}
#respuesta = requests.get(url , params=argumentos) 
#respuesta = requests.get(url , params=argumentos, headers=head) #*Puedes especificar encabezados HTTP personalizados como un diccionario para personalizar la solicitud.
#respuesta = requests.get(url, params=argumentos, auth=('Andres', 'Gelvis')) #* Puedes proporcionar información de autenticación, como un nombre de usuario y contraseña, en forma de tupla.
respuesta = requests.get(url, params=argumentos, timeout=5) #*  Puedes especificar un tiempo de espera para la solicitud. Esto indica cuánto tiempo debe esperar la solicitud antes de lanzar una excepción si no se recibe una respuesta. 

# rta = respuesta.content.decode()
# print(rta)

#! Uso del verbo POST
url ='https://httpbin.org/post'
argumentos = {"Nombre":"Andres", "Apellido": "Rodriguez", "Edad":18}


#respuesta= requests.post(url, params=argumentos)
#respuesta= requests.post(url, data=argumentos)
#respuesta= requests.post(url, json=argumentos) #* Se serializa en el servidor
#respuesta= requests.post(url, data=json.dumps(argumentos)) #* Se serializa en el cliente

# rta = respuesta.content.decode()
# print(rta)

#!  Uso del verbo DELETE 
