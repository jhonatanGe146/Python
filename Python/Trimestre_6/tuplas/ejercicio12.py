"""
Ejercicio 12.
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x15 y nombre marco.
Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.

  111111111111111
  100000000000001
  100000000000001
  100000000000001
  111111111111111
Visualiza el contenido de la matriz en pantalla."""


def marco5x15():
    fila_borde = (1,) * 15
    fila_interior = (1,) + (0,) * 13 + (1,)
    marco = (fila_borde,) + (fila_interior,) * 3 + (fila_borde,)
    
    for i in marco:
        for j in i:
            print(j, end="")
        print()
marco5x15()