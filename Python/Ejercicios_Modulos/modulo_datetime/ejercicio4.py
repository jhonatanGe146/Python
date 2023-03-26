'''Escribe un programa con el módulo datetime que funcion como alarma y
escribe una operación matématica que haga que se ejecute después de 20 segundos'''
import datetime as d
import time as t

def alarma():
    fh_actual= d.datetime.now()
    alarma=fh_actual+ d.timedelta(seconds=20)
    while d.datetime.now() <alarma:
        t.sleep(1)
    gra= float (input("inserta los grados a convertir :"))
    fa = (gra * 9/5) + 32
    k = (gra + 273.15)
    R = (gra*(9/5)+491.67)
    print ("Los", gra , "grados" " celsius", "se convirtieron en:", "\n  Fahrenheit:", fa ,"\n Kelvin:", k , "\n rankine:", R )
        
alarma()