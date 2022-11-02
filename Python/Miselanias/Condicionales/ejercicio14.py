"""Solicite un Angulo al usuario en grados. Diga en que cuadrante está. Diga
además en que vuelta está sabiendo que cada 360 grados se completa una
vuelta a la circunferencia. Además diga el resultado en radianes"""

grados =float(input("Ingrese los grados para conocer su cuadrante, vuleta y radianes: "))
conta=0
grados1=grados-360
if grados1 <=90:
            print("Se encuentra en el primer cuadrante")
elif grados1<=180:
            print("Se encuentra en el segundo cuadrante")
elif grados1<=270:
            print("Se encuentra en el Tercer cuadrante")
elif grados1 <=360:
            print("Se encuentra en el cuarto cuadrante")

radianes= (grados*3.1416)/180
print("A dado",conta, "vueltas")
print("Su conversión a radianes es: ", radianes)