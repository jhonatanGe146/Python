import requests
import json

url ='https://httpbin.org/post'

argumentos = {"animal":"perro"}
#respuesta= requests.post(url, params=argumentos)
#respuesta= requests.post(url, data=argumentos)
#respuesta= requests.post(url, json=argumentos) #* Se serializa en el servidor
respuesta= requests.post(url, data=json.dumps(argumentos)) #* Se serializa en el cliente
rta = respuesta.content.decode()

print(rta)

