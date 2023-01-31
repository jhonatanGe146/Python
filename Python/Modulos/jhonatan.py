def fill (lista):
    import random
    try:
        rang=(round(random.randint(1,50)))
        for i in range (rang):
            x=(round(random.randint(1,200)))
            lista.append(x)
        return lista
    except AttributeError:
        return("Debes dar como argumento una lista")


def fill_specify(lista,inf,max,cant):
    import random
    try:
        for i in range (cant):
            num=(round(random.randint(inf,max)))
            lista.append(num)
        return lista
    except AttributeError:
        return ("Debes dar como argumento una lista")


def sumlist (lista):
    try:
        acum=0
        for i in lista:
            acum+=i
        return acum
    except AttributeError:
        return ("Debes dar como argumento una lista")


def promlist(lista):
    try:
        p=sumlist(lista)
        prom=p/len(lista)
        return prom
    except AttributeError:
        return ("Debes dar comoa rgumento una lista")
    except ZeroDivisionError:
        return("La lista debe tener como minimo un dato")


def par (lista,a,c):
    import random
    try:
        z=0
        while z < c:
            num=round(random.randint(1,600))
            if a ==2:
                if num % 2 ==0:
                    lista.append(num)
                    z+=1
            elif a ==1:     
                if num%2 !=0:
                    lista.append(num)
                    z+=1
        return(lista)
    except AttributeError:
        return ("Debes dar como argumento una lista")
