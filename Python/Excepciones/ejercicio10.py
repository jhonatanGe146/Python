#KeyboardInterrupt: Se produce cuando el usuario interrumpe la ejecución del programa mediante la combinación de las teclas CTRL+C.
def interrupción():
    try:
        for i in  range(200000):
            print(i)
    except KeyboardInterrupt:
        print('KeyboardInterrupt: Se ha detenido la ejecución del programa con el comando CTRL+C')