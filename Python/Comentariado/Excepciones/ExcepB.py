values = (1, 0)# Crea una variable llamada values y le asigna el valor de una tupla (1,0)
#x,y=10,12# crea dos variables una llamada 'x' y otra llamada 'y' y le asigna el valor de 10 , 12 respectivamente
#print(divmod(10,3)) #Es un comentario que imprime el resultado de la función divmod que toma como argumentos (10,34) en cual es primero es el dividendo y el segundo el divisor
try:# Define un bloque de codigo para probar, ya que puede ocurrir un error en él. 
    q, r = divmod(*values) #Define dos variables q y r y a cada una se le asigana el valor resultante de la función.
    #print('valor de q=',q) #Imprime un str (valor de q=) y el valor almacenado en q anteriormente
    print(f'q={q}')# Imprime uuna forma de sintaxis para combinar str con variales, donde (q=) es el str y ({q}) y el la variable,tiene que iniciar con una f para este modo de sintaxis.
    print(f'r={r}')# Imprime uuna forma de sintaxis para combinar str con variales, donde (r=) es el str y ({r}) y el la variable,tiene que iniciar con una f para este modo de sintaxis. .
except (ZeroDivisionError, TypeError) as e: #Define el bloque de codigo en que se se trataran los errores (except),hace uso de dos excepciones (ZeroDivisionError y TypeError) que son renombradas a 'e'
    print(type(e), e)# Imprime el tipo de tipo de la excepcion y su descripción