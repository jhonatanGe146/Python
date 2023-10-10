"""Ejercicio 6.
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4)
y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes.Debes usar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días."""

def mesxdia():
    try:  
        meses = [
            ("Enero", 31),
            ("Febrero", 28),
            ("Marzo", 31),
            ("Abril", 30),
            ("Mayo", 31),
            ("Junio", 30),
            ("Julio", 31),
            ("Agosto", 31),
            ("Septiembre", 30),
            ("Octubre", 31),
            ("Noviembre", 30),
            ("Diciembre", 31)
        ]


        numero_mes = int(input("Ingrese un número de mes (1-12): "))

        if numero_mes >= 1 and numero_mes <= 12:
            nombre_mes, dias = meses[numero_mes - 1]
            print(f"El mes {numero_mes} es {nombre_mes} y tiene {dias} días.")
        else:
            print("Número de mes no válido. Debe estar entre 1 y 12.")
            mesxdia()
    except ValueError:
        print("ERROR!!Ingreso un valor no soportado")
        print()
        mesxdia()
mesxdia()