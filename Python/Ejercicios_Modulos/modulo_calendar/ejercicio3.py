"""Ingresar una fecha y que devuelva el dia de la semana(lunes,martes)"""
import calendar
def dia_semana():
    año= int(input('Ingrese el año:'))
    mes= int(input('Ingrese el mes: '))
    dia= int(input('Ingrese el dia: '))
    v=calendar.weekday(año, mes, dia)
    if v == 0:
        print('Lunes')
    elif v == 1:
        print('Martes')
    elif v == 2:
        print('Miercoles')
    elif v == 3:
        print('Jueves')
    elif v == 4:
        print('Viernes')
    elif v == 5:
        print('Sabado')
    elif v == 6:
        print('Domingo')
    

dia_semana()