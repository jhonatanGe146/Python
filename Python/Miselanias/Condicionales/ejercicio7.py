"""Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig.
manera:
Si trabaja 40 horas o menos se le paga $2600 por hora
Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40
horas y $5000 por cada hora extra"""

horas_laboral = int (input ("horas trabajas semanalmente: "))
if horas_laboral <= 40 :
    salario = (horas_laboral * 2600)
else:
    horas_extra= (horas_laboral-40)
    salario = (40 * 2600 ) + (horas_extra * 5000)

print ("Su salario semanal es de: ", salario)