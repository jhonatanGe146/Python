#OverflowError: Se produce cuando un cálculo númerico produce un resultado que es demsiado grande para ser representado.
def overflowerror(a,b):
    try:
        resultado=a**b
    except OverflowError:
        print("OverflowError: no se puede realizar la operacion")


overflowerror(25.6,214503)