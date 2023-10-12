"""Escriba un programa en python que genere una cantidad indeterminada de listas numericas. Máximo 10 listas de tamaño variable entre mínimo 10 y máximo 100 elementos. Cada elemento debe ser un número aleatorio entre 0 y 100.

Escriba una función que reciba las listas como parametros posicionales (*args) y diga cual lista tiene la suma mayor, el número mayor y cual el número menor"""   



import random

def generar_lista():
    # Generar una lista de tamaño aleatorio entre 10 y 100 con números aleatorios entre 0 y 100.
    lista=[]
    for j in range (random.randint(10,100)):
        lista.append(random.randint(0,100)) 
    return lista
       

def encontrar_max_min_suma(*listas):
    if not listas:
        return "No se proporcionaron listas."

    max_suma = float('-inf')
    max_lista = None
    max_numero = float('-inf')
    min_numero = float('inf')

    for lista in listas:
        suma_actual = sum(lista)
        numero_max_actual = max(lista)
        numero_min_actual = min(lista)

        if suma_actual > max_suma:
            max_suma = suma_actual
            max_lista = lista
        if numero_max_actual > max_numero:
            max_numero = numero_max_actual
        if numero_min_actual < min_numero:
            min_numero = numero_min_actual

    return f"La lista con la suma mayor es {max_lista}, su suma es {max_suma}, el número mayor es {max_numero} y el número menor es {min_numero}."

# Generar entre 1 y 10 listas aleatorias.
num_listas = random.randint(1, 10)
listas = [generar_lista() for _ in range(num_listas)]

print("Listas generadas:")
for i, lista in enumerate(listas):
    print(f"Lista {i + 1}: {lista}")

resultado = encontrar_max_min_suma(*listas)
print(resultado)