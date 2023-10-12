def sumar (n1,n2):
    return n1+n2

def posicionales (*args):
    #print(type(args))
    s=0
    for i in args:
        s+=i
    return s

#print(posicionales(1,2,3,5,67,4,43,2,54,657,67))



def clave (**kwargs):
    #print(type(kwargs))
    for key, values in kwargs.items():
        print(f"{key}:{values}")

# x = input("Ingrese el numero")
# clave(num = x ,numw=3)



def myfunction (*args, **kwargs):
    pass

myfunction(12,232,3, nombre="pedro",edad=28)