"""Escribir un programa que visualice la siguiente figura,
utilizando ciclos. El usuario decide cuantas líneas quiere
imprimir
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
"""

def figure(linea):
    linea+=1
    for i in range (0,linea):
        visu=("* ")*i
        print (visu, sep="_")   
linea=int (input("Hasta que linea quiere visualizar la figura: "))
figure(linea)