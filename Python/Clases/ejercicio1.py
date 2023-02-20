class  primerclase:
    pass 
primer_objeto=primerclase()

#Crear pila con enfoque procedimental.

'''pila=[]

def push(valor):
    pila.append(valor)
    
def sacar ():
    val=pila[-1]
    del pila[-1]
    return val

push(3)
push(2)
push(1)
print(pila)
print(sacar())
print(sacar())
print(sacar())'''

#Crear pila con enfoque orientado a objetos.
class pila:
    def __init__(self):
        print('Se invoca de forma implícita')
        self.__lista=[]# encapsulamiento del mundo exterior, es como si no estuviera
        
        
pila1=pila()
pila2=pila()
print(len(pila1.lista))