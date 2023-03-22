'''Hacer un código que muestre los años bisiestos que tuvieron lugar dede 1970 hasta el presente año'''
import calendar

def año_bisiesto():
    año2=int(input('Ingrese el valor del rango maximo:' ))
    for i in range(1970, año2+1):
        if calendar.isleap(i)==True:
            print(i, 'es un año bisiesto')
        else:
            print(i, 'No es un año bisiesto')


año_bisiesto()
    

    

          
