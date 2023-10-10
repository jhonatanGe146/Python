"""Ejercicio 5.
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""

import random

# numeros= []
# for i  in range(10):
#     numeros.append(round(random.random()*100))
# print (numeros)

def calcularMaxMin (lista):
    maximo=max(lista)
    minimo=min(lista)
    return f"El número mayor es: {maximo}  y el menor: {minimo}"
   

def pedirNumeros():
    try:
        listaNum = []
        cont = 0
        print("Ingrese los números para comparar o '0' si quieres salir: ")
        while True:
            num = float(input("Ingrese número: "))
            if num != 0.0:
                listaNum.append(num)
                cont+=1 
          
            else:
                if cont==0:
                    print ("Debes Ingresar por lo menos un número")
                    print()                  
                else:    
                    print(calcularMaxMin(listaNum))
                    break  
    except ValueError:
        print("Por favor, ingrese solo números.")
        print()
        pedirNumeros()

    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")


pedirNumeros()
        
