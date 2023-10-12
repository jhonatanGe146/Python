def decoradora(funcion):
    print("Inicia la decoracion")
    def interna (*args, **kwargs):
        print (funcion (*args, **kwargs))
    return interna

# @decoradora
# def suma(n1,n2):
#     return n1+n2
# suma(10,5)

# @decoradora
# def suma3(n1,n2,n3):
#     return n1+n2+n3
# suma3(1,2,3)
#? función Para Sumar Valores Indeterminados
@decoradora
def sumar(*args, **kwargs):
    total_sum =0
    for num in args:
        total_sum+=num
    return total_sum
sumar(5,6,2)

#? función Para Restar Valores Indeterminados
@decoradora
def restar(*args, **kwargs):
    total_res=args[0]
    for num in range (1,len(args)):
        total_res-=args[num]
    return total_res

restar(10,20,5)

#? función Para Multiplicar Valores Indeterminados
@decoradora
def Multiplicar(*args, **kwargs):
    total_mul=args[0]
    for num in range (1,len(args)):
        total_mul*=args[num]
    return total_mul
Multiplicar(3,3,2)
