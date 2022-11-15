"""Determinar cuales son los múltiplos de 5 comprendidos entre
1 y N."""


def multiplo(N):
    n=N+1
    print("Los primeros",N, "números múltiplos de 5 son:")
    for i in range(1,n,1):
        multiplos= i*5
        print (multiplos)
N=int (input ("¿Cuántos multiplos de 5 quieres conocer? "))
multiplo(N)