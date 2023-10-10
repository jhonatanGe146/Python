"""Ejercicio 1.
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla
(suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =
"""

def EscribirCentrado(texto):
    long_tex = len(texto)
    espacios = 40 - long_tex // 2
    print(" "*espacios+texto)
    print("=" * 80)

# texto = str(input("Digite el texto a centrar: "))
# EscribirCentrado(texto)
