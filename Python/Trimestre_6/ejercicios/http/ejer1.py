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


respuesta= requests.post(url, params=argumentos) #* Los datos quedan guardados en en args
#respuesta= requests.post(url, data=argumentos) #* Los datos quedan guardados en form
#respuesta= requests.post(url, json=argumentos) #* Se serializa en el servidor y los datos quedan guardados en data y json
#respuesta= requests.post(url, data=json.dumps(argumentos)) #* Se serializa en el cliente y los datos quedan guardados en data y json 

# rta = respuesta.content.decode()
# print(rta)

#!  Uso del verbo DELETE 


url = 'https://httpbin.org/delete'
argumentos = {"Nombre": "Andres", "Apellido": "Rodriguez", "Edad": 18}
# respuesta = requests.delete(url, json=argumentos)
# rta = respuesta.content.decode()
# print(rta)
# print(respuesta.status_code)  #* Imprime el código de estado de la respuesta


#! Uso del verbo PUT


url = 'https://httpbin.org/put'
argumentos = {"Nombre": "Andres", "Apellido": "Rodriguez", "Edad": 18}
respuesta = requests.put(url, json=argumentos)
rta = respuesta.content.decode()
# print(rta)
# print(respuesta.status_code)  #* Imprime el código de estado de la respuesta
# if respuesta.status_code == 200:
#     print("Solicitud PUT exitosa")
# else:
#     print(f"Error en la solicitud PUT. Código de estado: {respuesta.status_code}")

#! Uso del verbo PATCH

url = 'https://httpbin.org/patch'
argumentos = {"Nombre": "Andres", "Apellido": "Rodriguez", "Edad": 18}
rta = respuesta.content.decode()
print(rta)
print(respuesta.status_code)  #* Imprime el código de estado de la respuesta
respuesta = requests.patch(url, json=argumentos)

if respuesta.status_code == 200:
     print("Solicitud PATCH exitosa")
else:
     print(f"Error en la solicitud PATCH. Código de estado: {respuesta.status_code}")