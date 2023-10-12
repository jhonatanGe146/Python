def calcular_iva(i):#Definimos la funcion principal que tiene como parametro el valor de iva a ser incluido al producto 
    s = i/100
    # Definimos una función interna que toma un argumento `x` que  es el precio del producto y hace la operacion para calcular el iva
    def f_iva(x):
        iva = x * s
        valor_total = x + iva
        return f"Valor total del producto es ${valor_total} se le agrego un iva de {i}% al valor original"
    
    # Devolvemos la función interna como resultado
    return f_iva 

# Guardamos en la var calcular la funcion calcular_iva que pasa como argumento el valor del iva y se lo asigna al parametro i de la funcion que se almacena en calcular 
calcular = calcular_iva(15)

# Ahora podemos usar el valor del iva guardado en calcular, pasamos el valor del producto para que se almanece en x de la funcion interna (f_iva) de calcular__iva()
resultado = calcular(85000)  # Esto devuelve el return de f_iva() que ya a calculado el precio del producto incluyendo el iva

calcular = calcular_iva(16)
resultado1 = calcular(1000)  # Esto devuelve el return de f_iva() que ya a calculado el precio del producto incluyendo el iva



calcular = calcular_iva(17)
resultado2 = calcular(5500)  # Esto devuelve el return de f_iva() que ya a calculado el precio del producto incluyendo el iva
print(resultado)
print(resultado1)
print(resultado2)




def calcular_tercer_angulo(angulo1):#Definimos la funcion principal que como parametro el valor del primer angulo
    # Definimos una función interna que toma el segundo ángulo como argumento y calcula el tercer ángulo
    def calcular_tercer(angulo2):
        # Verificamos si los ángulos son válidos (la suma de los ángulos de un triángulo es 180 grados)
        suma_angulos = angulo1 + angulo2

        if suma_angulos >= 180:
            return "Los ángulos ingresados no forman un triángulo válido."

        # Calculamos el tercer ángulo restando la suma de los dos ángulos dados de 180 grados
        tercer_angulo = 180 - suma_angulos

        return f"El tercer ángulo es de {tercer_angulo} grados."

    # Devolvemos la función interna como resultado
    return calcular_tercer

# Pedimos al usuario que ingrese el primer ángulo
#angulo1 = float(input("Ingresa el valor del primer ángulo: "))

# Llamamos a la función principal para obtener la función interna
#calcular = calcular_tercer_angulo(angulo1)

# Pedimos al usuario que ingrese el segundo ángulo y llamamos a la función interna para calcular el tercer ángulo
# angulo2 = float(input("Ingresa el valor del segundo ángulo: "))
# resultado = calcular(angulo2)

# print(resultado) 








