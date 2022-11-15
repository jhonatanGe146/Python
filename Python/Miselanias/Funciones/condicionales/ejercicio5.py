"""Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la
hora que será dentro de 1 segundo"""

def formt_hours(horas,minutos,segundos):  
    if segundos > 58:
        minutos+=1
        segundos=00
        if minutos > 58:
            horas+=1
            minutos= 00
            if horas>23:
                horas = 0
    else: 
        segundos +=1
    return horas,minutos,segundos
horas = int(input ("Ingresar la hora: "))
minutos = int(input ("Ingresar los minutos: ")) 
segundos = int(input ("Ingresar los segundos: "))
print ( formt_hours(horas,minutos,segundos))