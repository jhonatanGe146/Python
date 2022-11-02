"""Pedir números. imprimir con el opuesto, finaliza con cero
 y diga cuantos ingreso"""
  
num=int (input("Digite un número: "))
cont=0  
while num != 0:
    opu=num*-1
    print ("sU opuesto de es=",opu)
    num=int (input("Digite un número: "))
    cont+=1
print("Usted ingreso una cantidad de =",cont,"números")