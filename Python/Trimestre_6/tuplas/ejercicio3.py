"""Ejercicio 3.
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor."""

def notas_alum ():
    try: 
        notas = ()
        for i in range(5):
            nota = float(input("Ingrese una nota (entre 0 y 10): "))
            while nota < 0 or nota > 10:
                print("Nota fuera del rango valido (0-10). Intente de nuevo.")
                nota = float(input("Ingrese una nota (entre 0 y 10): "))
            notas += (nota,)

        # Mostrar todas las notas
        print("Todas las notas del alumno:")
        for nota in notas:
            print(nota)

        # Calcular la nota media
        nota_media = sum(notas) / len(notas)
        print("Nota media:", nota_media)

        # Encontrar la nota más alta y la menor
        nota_mas_alta = max(notas)
        nota_menor = min(notas)
        print("Nota más alta:", nota_mas_alta)
        print("Nota menor:", nota_menor)
    except ValueError or TypeError:
        print("Valor no soportado por el sistema ")
        notas_alum()

notas_alum()