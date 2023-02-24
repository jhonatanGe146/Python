def sumlist():
    try:
        lista=[]
        num=-1
        while num != 0:
            num=int(input("Ingresa un numeros: "))
            lista.append(num)
        del lista[-1]
        acu=0
        for i in lista:
            acu+=i
        print (acu)
    except ValueError:
        print("Debes ingresar un número")
        sumlist()
        
sumlist()