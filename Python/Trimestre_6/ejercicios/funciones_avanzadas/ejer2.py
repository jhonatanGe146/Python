import random
def base (funcion):
    print ('Primera linea de la función')
    funcion()
    print('Linea final de la función')


def generar_lista():
    # Generar una lista de tamaño aleatorio entre 10 y 100 con números aleatorios entre 0 y 100.
    print ([random.randint(0, 100) for _ in range(random.randint(10, 100))])

base(generar_lista)