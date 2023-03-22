"""Crear una función que muestre los años bisiestos de un determinado rango de años sin uasar la funcion isleapdays"""
import calendar
def año_bisiesto():
    año=int(input('Ingrese el valor del rango minimo: '))
    año2=int(input('Ingrese el valor del rango maximo:' ))
    for i in range(año, año2+1):
        if calendar.isleap(i)==True:
            print(i, 'es un año bisiesto')
        else:
            print(i, 'No es un año bisiesto')


año_bisiesto()
    









