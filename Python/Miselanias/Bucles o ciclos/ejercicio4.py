"""Determinar ¿cuales y cuantos números perfectos hay entre 1 y
1000?"""

cuantos=0
for num in range (1,1001):
    perfe=0
    for i in range (1,num):
        resul= num%i
        if resul == 0:
            perfe+=i
            if perfe==num:
                cuantos+=1
                print (num, "Es un número perfecto")
print("En total son", cuantos,"números perfectos")