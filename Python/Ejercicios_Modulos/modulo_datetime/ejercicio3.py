'''Escriba un programa que solicite al usuario que introduzca una fecha en formato
dd/mm/aaaa, la convierta a un objeto de la clase date del módulo datetimey muestre
por pantalla el dia de la semana correspondiente'''

import datetime as d
 
def dia ():
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    dia=int(input('Ingree el dia: '))
    mes=int(input('Ingrese el mes:'))
    año=int(input('Ingrese el año: '))
    formato=(d.date(año,mes,dia))
    dia=dias_semana[formato.weekday()]
    print(dia)

dia()