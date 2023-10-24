import requests
"""{'semana': '19',
    'a_o': '2023',
    'cod_dpto_n': '05',
    'cod_mun_n': '05001',
    'nom_dep_not': 'ANTIOQUIA',
    'nom_mun_not': 'MEDELLIN',
    'fec_not': '2023-05-11',
    'fec_diagnostico': '2023-06-13',
    'sexo': 'M',
    'edad': '37',
    'unid_med': '1',
    'ini_sin': '2023-05-10',
    'fecha_exantema': '2023-05-10',
    'hospitalizacion': '2',
    'con_fin': '1',
    'vinculo_epi': '2',
    'viajo': '2',
    'fuente_infeccion': 'FUENTE DESCONOCIDA',
    'fec_fin_seguimiento': '2023-05-31',
    'pert_etn': '6',
    'tip_ss': 'C', 
    'estrato': '3'},"""

url= 'https://www.datos.gov.co/resource/tmet-yeek.json'

#print(respuesta)

def obtenerCasosPorMunicipio (Purl):
    url= Purl
    response =requests.get(url)
    respuesta= response.json()
    
    conteo= {}
    for dicci in respuesta:
        cont=1
        for clave, valor in dicci.items():
                #for i in conteo.values():
                if clave == 'nom_mun_not': 
                    if clave not in conteo:
                        conteo[valor] = cont
                    else: 
                        conteo [valor] = "pero"
                    
    return conteo
print(obtenerCasosPorMunicipio(url))