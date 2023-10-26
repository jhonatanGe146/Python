import requests
import sys
sys.path.append('Python/Trimestre_6')

from funciones import f_ejercicio1
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


# response =requests.get(url)
# respuesta= response.json()
# print(len (respuesta))


def obtenerCasosPorEntidad (Purl, Pentidad): #? Función Para Conocer La Cantidad De Casos Por Una Entidad Especifica Que Se Pasa Por Párametros (Dept,Munc)
    response =requests.get(Purl)
    respuesta= response.json()
    conteo= {}
    for dicci in respuesta:
        for claveM, valorM in dicci.items():
            if claveM == Pentidad:
                if valorM not in conteo: 
                    conteo[valorM] = 1
                else: 
                    conteo [valorM] +=1
    print ("Nombre | Cantidad  De Casos")
    for claveC, valorC in conteo.items():
        print (f"{claveC} = {valorC}")
      

def obtenerCasosPorGruposEdad(Purl): #? Función Para Conocer La Cantidad De Casos Por Grupos De Edad
    response =requests.get(Purl)
    respuesta= response.json()
    gruposEdad= {'Niños': 0, 'Adolescentes': 0, 'Adultos jóvenes': 0, 'Adultos de mediana edad':0, 'Adultos de tercera edad':0}
    for dicci in respuesta:
        for claveM, valorM in dicci.items():
            if claveM == "edad":
                valorM = int(valorM) #* Convierte el valor de la edad a entero
                if valorM >= 40 and valorM <= 64: 
                    gruposEdad['Adultos de mediana edad'] += 1
                    
                elif valorM >= 20 and valorM <= 39: 
                    gruposEdad['Adultos jóvenes'] += 1
                    
                elif valorM >= 13 and valorM <= 19: 
                    gruposEdad['Adolescentes'] += 1
                    
                elif valorM <= 12:
                    gruposEdad['Niños'] += 1
                    
                else:
                    gruposEdad['Adultos de tercera edad'] += 1
                    
    print ("Grupo De Edad | Cantidad De Casos")
    for claveC, valorC in gruposEdad.items():
        print (f"{claveC} = {valorC}")
    

def obtenerCasosPorSemana (Purl): #? Función Para Conocer La Cantidad De Casos Por Semanas
    response =requests.get(Purl)
    respuesta= response.json()
    conteo= {}
    for dicci in respuesta:
        for claveM, valorM in dicci.items():
            if claveM == 'semana':
                if valorM not in conteo: 
                    conteo[valorM] = 1
                else: 
                    conteo [valorM] +=1
    #* Ordena el diccionario por las claves (semanas) en orden ascendente
    conteo_ordenado = dict(sorted(conteo.items()))
    
    print ("Semana | Cantidad  De Casos")
    for claveC, valorC in conteo_ordenado.items():
        print (f"{claveC} = {valorC}")


def obtenerCasosPorGenero (Purl, Pgenero): #? Función Para Conocer La Cantidad De Casos Por Un Genero Especifico
    response =requests.get(Purl)
    respuesta= response.json()
    genero= {'Femenino':0,'Masculino':0}
    for dicci in respuesta:
        for claveM, valorM in dicci.items():
            if claveM == 'sexo':
                if valorM == 'F': 
                    genero['Femenino'] +=1
                else: 
                    genero ['Masculino'] +=1
    print ("Genero | Cantidad  De Casos")
    for claveC, valorC in genero.items():
        if Pgenero == 'M':
            if claveC == 'Masculino':
                print (f'{claveC} = {valorC}')
        else:
            if claveC == 'Femenino':
                print (f'{claveC} = {valorC}')

def obtenerCasosPorEstrato(Purl): #? Función Para Conocer La Cantidad De Casos Por Estrato
    response =requests.get(Purl)
    respuesta= response.json()
    gruposEdad= {'1': 0, '2': 0, '3': 0, '4':0, '5':0, '6':0,'Sin Estrato':0}
    for dicci in respuesta:
        for claveM, valorM in dicci.items():
            if claveM == "estrato":
                if valorM == "1": 
                    gruposEdad['1'] += 1
                
                elif valorM == "2": 
                    gruposEdad['2'] += 1
                
                elif valorM == "3": 
                    gruposEdad['3'] += 1
                
                elif valorM == "4": 
                    gruposEdad['4'] += 1

                elif valorM == "5": 
                    gruposEdad['5'] += 1
                    
                elif valorM == "6": 
                    gruposEdad['6'] += 1
                    
                else:
                    gruposEdad['Sin Estrato'] += 1
                    
    print ("Estrato| Cantidad De Casos")
    for claveC, valorC in gruposEdad.items():
        print (f"{claveC} = {valorC}")
def InstitutoNacionalSalud():
    #? Variables Necesarias Para al ejecución del Pograma 
    urn= 'https://www.datos.gov.co/resource/tmet-yeek.json'
    entidad=''
    genero=''
    espacio = ''
    select ='Selecione una Opción: '
    option1 = 'Conocer La Cantidad Total De Casos Por Entidad'
    option2 = 'Conocer La Cantidad Total De Casos Por Grupo De Edad'
    option3 = 'Conocer La Cantidad Total De Casos Por Semana'
    option4 = 'Conocer La Cantidad Total De Casos Por Genero'
    option5 = 'Conocer La Cantidad Total De Casos Por Estrato'
    optionM = 'Salir Al Menu Principal'
    option_ = 'No Existe Esta Opción'
    #? --------------------------------------------
    try:
        while True:
            f_ejercicio1.EscribirCentrado("Instituto Nacional de Salud")  
            f_ejercicio1.EscribirCentrado("Casos positivos de Viruela símica en Colombia")
            print (espacio)
            print ("Funcionalidades del Sistema:")
            print (espacio)
            print (f"1-{option1}" )
            print (f"2-{option2}")
            print (f"3-{option3}")
            print (f"4-{option4}")
            print (f"5-{option5}")
            print (f"6-Finalizar Programa")
            ctrl=int (input (select))
            print (espacio)
            match ctrl:
                case 1:
                    while True:
                        print (option1)
                        print ('1-Cantidad De Casos Por Departamento')
                        print ('2-Cantidad De Casos Por Municipio')
                        print (f"3-{optionM}")
                        ctrl=int (input (select))
                        print (espacio)
                        match ctrl:
                            case 1:
                                entidad='nom_dep_not'
                                obtenerCasosPorEntidad(urn, entidad)
                                print (espacio)
                            case 2:
                                entidad='nom_mun_not'
                                obtenerCasosPorEntidad(urn, entidad)
                                print (espacio)
                            case 3:
                                break
                            
                            case _:
                                print(option_)
                case 2:
                    while True:
                        print (option2)
                        print ('1-Cantidad De Casos Por Grupos De Edad')
                        print (f"2-{optionM}")
                        ctrl=int (input (select))
                        print (espacio)
                        match ctrl:
                            case 1:
                                obtenerCasosPorGruposEdad(urn)
                                print (espacio)
                                            
                            case 2:
                                break
                            
                            case _:
                                print(option_)
                case 3:
                    while True:
                        print (option3)
                        print ('1-Cantidad De Casos Por Semana')
                        print (f"2-{optionM}")
                        ctrl=int (input (select))
                        print (espacio)
                        match ctrl:
                            case 1:
                                obtenerCasosPorSemana(urn)
                                print (espacio)
                                            
                            case 2:
                                break
                            
                            case _:
                                print(option_)
                case 4:
                    while True:
                        print (option4)
                        print ('1-Cantidad De Casos Masculinos')
                        print ('2-Cantidad De Casos Femeninos')
                        print (f"3-{optionM}")
                        ctrl=int (input (select))
                        print (espacio)
                        match ctrl:
                            case 1:
                                genero='M'
                                obtenerCasosPorGenero(urn, genero)
                                print (espacio)
                            case 2:
                                genero='F'
                                obtenerCasosPorGenero(urn, genero)
                                print (espacio)
                            case 3:
                                break
                            
                            case _:
                                print(option_)
                case 5:
                    while True:
                        print (option5)
                        print ('1-Cantidad De Casos Por Estrato')
                        print (f"2-{optionM}")
                        ctrl=int (input (select))
                        print (espacio)
                        match ctrl:
                            case 1:
                                obtenerCasosPorEstrato(urn)
                                print (espacio)
                                            
                            case 2:
                                break
                            
                            case _:
                                print(option_)
                case 6:
                    print ('Programa Finalizado')
                    break
                            
                case _:
                    print(option_)
    except ValueError:
        print ('Valor No Soportado Por El Sistema')
        print (espacio)
        InstitutoNacionalSalud()
        
InstitutoNacionalSalud()