"""Ejercicio 3.
Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.
Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""
def precio_frutas():
    # Crear un diccionario de precios de frutas
    frutasxprecios = {
        "manzana": 2000,
        "banana": 1700,
        "uva": 3000
    }

    while True:

        fruta = input("Ingrese el nombre de la fruta (o '*' para terminar): ").lower()
        
        if fruta == '*':
            break
        
        if fruta in frutasxprecios:
            cant = int(input("Ingrese la cantidad vendida: "))
            precio_total = frutasxprecios[fruta] * cant
            print(f"Precio total de {fruta}: ${precio_total}")
        else:
            print("Error")
            break

precio_frutas() 