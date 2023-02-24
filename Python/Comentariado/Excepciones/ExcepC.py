def try_syntax(numerator, denominator):#Definie un función llamda (try_syntax) que tiene dos parametros (numerator, denominator)
    try:# Define un bloque de codigo para probar, ya que puede ocurrir un error en él. 
        #print(f'In the try block: {numerator}/{denominator}')#Imprime utilizando la sintaxis de combinar str (In the try block:) con variables ( {numerator}/{denominator}), tiene que iniciar con una f para este modo de sintaxis.
        #!quiero ver el resultado de la operacion en el print
        print('In the try block:', numerator/denominator)#Para ver el resultado de la operacion en el print hay que usar la forma de sintaxis en la que se reparar por comas cada str y variable.
        result = numerator / denominator #Define una variable llamda result que almacena el resultado de la operacion numerator\denominator.
    except ZeroDivisionError as zde:#Define el bloque de codigo en que se se trataran los errores (except),hace uso de la excepción(ZeroDivisionError) que se renombradas a 'zde'.
        print(zde)#Imprime la excepcion ZeroDivisionError que fue remobrada a zde.
    else:#Este codigo se ejecuta siempre y cuando no se se active la excepcion (ZeroDivisionError).
        print('The result is:', result)# Imprime un str('The result is:) y la variable result, con la forma de sintaxis convencional.
        return result# Devuelve o retonar la variable result.
    finally:#Bloque de codigo para escribir la sentencias de finalización del programa, siempre se ejecuta.
        print('Exiting')#Imprime un mensaje personalizado cuando se remine el programa.
        #return "Fallo por zero" #Devuelve o retona un str (Fallo por zero).
#print(try_syntax(12, 4))# Comentario que imprime la funcion (try_syntax) la cual toma como argumentos (12 y 4) para su ejecucuión.
print(try_syntax(10, 'a'))# Imprime la funcion (try_syntax) la cual toma como argumentos (10 y 'a') para su ejecucuión.