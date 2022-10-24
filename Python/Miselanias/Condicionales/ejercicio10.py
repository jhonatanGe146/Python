"""Solicite al usuario la hora en formato hh:mm:ss (hora militar, 24 horas). El
programa debe responder que hora será un segundo después. Ej: ingreso
11:59:59, el programa responde 12:00:00."""

hh = int(input ("Ingresar la hora: "))
mm = int(input ("Ingresar los minutos: ")) 
ss = int(input ("Ingresar los segundos: "))  
if ss > 58:
    mm+=1
    ss=00
    if mm > 58:
        hh+=1
        mm= 00
        if hh>23:
            hh = 0
else: 
    ss +=1
print ( "la hora un segundo despues es",hh, mm, ss, sep = ":")