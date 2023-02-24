try: # Define un bloque de codigo para probar, ya que puede ocurrir un error en él. 
    #print(1/1)) #Es un comentario  que presenta un error de SyntaxError, debido a que tiene un parentecis de mas.
    raise SyntaxError #Lanza el error de SyntaxError para manejarlo en el bloque de except.
except SyntaxError as e: #Define el bloque de codigo en que se se trataroa los errores (except) y renombra es error  de SyntaxError a 'e' con (as)
    print(e) # Imprime el error de SyntaxError
    print('Cierra el parentesis') # Imprime un mensaje personalizado en caso de que ocurra el error de SyntaxError.
    
try: # Define un bloque de codigo para probar, ya que puede ocurrir un error en él. 
    #raise ZeroDivisionError # #Es un comentario que lanza el error de ZeroDivionError para manejarlo en el bloque de except.
    print(1/0) # Imprime el resultado de la division (1/0), la cual causa un error que se maneja en el bloque de codigo except
#except (ZeroDivisionError) as e: #Define el bloque de codigo en que se se trataran los errores (except) y renombra es error ZeroDivisonError a 'e' con (as)
except ZeroDivisionError as zde: #Define el bloque de codigo en que se se trataran los errores (except) y renombra es error ZeroDivisonError a 'zde' con (as)
    print(zde)  # Imprime el error de ZeroDivisionError que fue renombrado a zde
    #print('prueba error') #Es un comentario que imprime un mensaje personalizado en caso de  ocurra el error de ZeroDivisionError