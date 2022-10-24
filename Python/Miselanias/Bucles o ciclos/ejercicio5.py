"""¿Cuáles y cuántos son los números primos comprendidos
entre 1 y 1000?"""
numero = 1
cantidad=0
while numero <= 1000:
    contador = 1
    divisores = 0
    while contador <= numero:
        if numero % contador == 0:
            divisores+=1
        contador+=1
    if divisores==2:
        print ("El número,", numero, "es primo")
        cantidad+=1
    numero+=1
print("La cantidad de números primos entre 1 y 1000 son:",cantidad )