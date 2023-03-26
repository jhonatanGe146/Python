'''ingrese un año y un mes con inputs, para que muestre el calendario de ese mes'''
import calendar
def saber_mes():
    año=int(input('Ingrese el año: '))
    mes=int(input('Ingrese el mes: '))
    if mes<=12:
        print(calendar.month(año, mes))
    else:
        print('ERROR:Solo hay 12 meses')
        saber_mes()
saber_mes()