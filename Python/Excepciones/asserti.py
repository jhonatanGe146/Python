def aserti (num):
    try:
        lon=len(num)
        assert lon == 10
        print('Su número de teléfono es:',num)
    except AssertionError:
        print('Parámetro no válido')
        
n=input('Ingrese el número de teléfono: ')
aserti(n)
