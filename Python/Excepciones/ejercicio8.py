## MemoryError:Se produce cuando el sistema no tiene suficiente memoria para en este caso crear la lista.

def ErrordeMemoria():
    try:
        v=[1]*100000000000
        print(v)
    except MemoryError:
        print("MemoryError:Se produce cuando el sistema no tiene suficiente memoria para en este caso crear la lista.")
        
ErrordeMemoria()