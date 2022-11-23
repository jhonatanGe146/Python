def divisores(num):
    try:        
        for i in range(1,num+1):
            if num%i==0:
                print(i,' es divisor')      
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')
        
        
        
        
while True:
    try:
        var=int(input('ingrese numero: \n'))
        divisores(var)
        print('El programa continua en esta linea')
        break
    except:
        print("El dato ingresado no es soportado\n Por favor ingresalo de nuevo")
        