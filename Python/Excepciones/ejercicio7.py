# ValueError: se produce cuando se llama a una función con un argumento que tiene un valor inapropiado.        
def ErrordeValor():
    try:
        n=int(input('ingresa tu edad'))
        if n>=18:
            print('mayor de edad ')
        elif n<=18:
            print('menor de edad')
    except ValueError:
        print('No has ingresado un numero')


ErrordeValor()