import requests

url= 'https://api.covidtracking.com/v2/states.json'
response =requests.get(url)
respuesta= response.json()
# print(type(respuesta))
lista_name= []
for lista, y in respuesta.items():
    if lista == "data":
        for subclaves in y: 
            #print(subclaves)   
            for i,m in subclaves.items(): 
                if i== "name":
                    lista_name.append(m)

#print(response.content.decode())
#print(lista_name)

def obtenerInfo (Purl, Pcampo, Pdato):
    url= Purl
    response =requests.get(url)
    respuesta= response.json()
    # print(type(respuesta))
    lista_name= []
    for lista, y in respuesta.items():
        if lista == Pcampo:
            for subclaves in y: 
                #print(subclaves)   
                for i,m in subclaves.items(): 
                    if i== Pdato:
                        lista_name.append(m)
    return lista_name


#print(obtenerInfo(url,"data", "name"))

def obtenerInfo2 (Purl, Pcampo, Pdato):
    url= Purl
    response =requests.get(url)
    respuesta= response.json()
    # print(type(respuesta))
    lista_name= [m for lista, y in respuesta.items() if lista == Pcampo for subclaves in y for i,m in subclaves.items() if i== Pdato]
    return lista_name
#print(obtenerInfo2(url,"data", "fips"))