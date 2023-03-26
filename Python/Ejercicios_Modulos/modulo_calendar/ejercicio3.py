"""Ingresar una fecha y que devuelva el dia de la semana(lunes,martes)"""
import calendar
def dia_semana():
    año= int(input('Ingrese el año: '))
    mes= int(input('Ingrese el mes:  '))
    dia= int(input('Ingrese el dia:  '))
    if mes<=12 and dia <=31:
        v=calendar.weekday(año, mes, dia)
        if v == 0:
            print('El dia es Lunes')
        elif v == 1:
            print('El dia es Martes')
        elif v == 2:
            print('El dia es Miercoles')
        elif v == 3:
            print('El dia es Jueves')
        elif v == 4:
            print('El dia es Viernes')
        elif v == 5:
            print('El dia es Sabado')
        elif v == 6:
            print('El dia es Domingo')
    else:
        print('ERROR:Solo hay 12 meses y máximo 31 dias en algunos meses')
        dia_semana()
    

dia_semana()