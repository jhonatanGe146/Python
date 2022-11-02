"""Valores enteros para los lados de un triángulo rectangulo se conoce como terna pitágorica.
Estos 3 lados deben satisfacer la relación que la suma de los cuadrados de los dos lados es igual al cuadrado de la hipotenusa.
Encuentre todas las termas pitagóricas para el lado 1, lado 2 y la hipotenusa, todos ellos no mayores que 500. ejemplo: c=3 c=4 h=5"""
suma=0
for i in range (1,501):
    for j in range(1,501):
        for k in range (1,501):
                lado1=i**2
                lado2=j**2
                lado3=k**2
                suma=lado1+lado2
                if suma==lado3:
                    print (i,j,k," es una terma pitágorica",suma,lado3)
                