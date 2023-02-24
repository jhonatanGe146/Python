def edad():#Define uan función llamada edad que no tiene ningún parametro.
    try:# Define un bloque de codigo para probar, ya que puede ocurrir un error en él. 
        tuedad=int(input("introduce tu edad"))#Define una variable entera que se debera ingresar por teclado y tiene un str de (introduce tu edad).
        print(f'tu edad es  {tuedad}')#Imprime la sintaxis en la que se combinan str (tu edad es) y variables ({tuedad}) y se debe iniciar con una f para utilizar esta foma de sintaxis.
        #print('Tu edad es ',tuedad)# Imprime de la forma convecional en la que se separan por ',' cada str ('Tu edad es) y variables (tuedad)
    except ValueError as e:#Define el bloque de codigo en que se se trataran los errores (except),hace uso de la excepción (ValueError) que es renombrada a 'e'
        print(e)#Imprime la excepción ValueError
        print("La edad debe ser un valor numerico...")# Imprime un mensaje personalizado que se mostrara si se ejecuta la excepción (ValueError).
        edad()#Se llama a la función edad() que no toma como argumentos ningun valor,se ejecutara siempre y cuando se ejecute la excepción ValueError.
    
edad()#Se llama a la función edad() que no toma como argumentos ningun valor.