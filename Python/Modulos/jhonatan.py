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


try:
      
      c=1+1
      
except AssertionError:
    print('AssertionError: No se cumplio la condición')
except TypeError:
    print('TypeError:Representa un error cuando una operación no puede ser completada, cuando un valor no es del tipo esperado.')
except AttributeError:
    print('AtributeError:Se genera cuando falla una asignación o una referencia de atributo.')
except SyntaxError:
    print('SyntaxError:Represta un error cuando se trata de interpretar código que resulta ser inválido sintácticamente.')
except IndexError:
    print('Índice de lista fuera de rango.')
except NameError:
    print("NameError: Llamar a algo no definido")
except KeyError:
    print("KeyError: Llave no encontrada ")       
except ModuleNotFoundError:
    print("ModuleNotFoundError: Módulo no encontrado")
except ValueError:
        print('Se levanta cuando a una función se le ingresa un argumento que tiene el tipo que se solicita, pero tiene un valor inapropiado.')
except MemoryError:
        print("MemoryError:Se produce cuando el sistema no tiene suficiente memoria para en este caso crear la lista.")
except OverflowError:
        print('OverflowError:Se produce cuando un cálculo númerico produce un resultado que es demsiado grande para ser representado.')
except KeyboardInterrupt:
        print('KeyboardInterrupt: Se ha detenido la ejecución del programa con el comando CTRL+C')
except ZeroDivisionError:
    print('ZeroDivisionError: se produce cuando se intenta dividir un número por cero.')
