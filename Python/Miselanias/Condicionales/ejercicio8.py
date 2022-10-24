"""Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
permita calcular el costo de una llamada dados los minutos de duración."""

min_duracion = int (input ("Ingresar los minutos de duración dela llamada: "))
if  (min_duracion <= 3):
    costo = 200
    print ("El costo de la llamada es: ", costo)
else:
    min_adicional = (min_duracion - 3)
    costo = (200) + (min_adicional *50)
    print ("El costo de la llamada es: ", costo)