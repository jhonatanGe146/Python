"""Algoritmo para hallar el m.c.d de dos números m y n por
el algoritmo de Euclides."""
from tkinter import N


m=int(input("digite el primer numero: "))
n=int(input("digite el segundo numero: "))
while m!=0:
    a=n
    b=m
    if n<0:
        n-=a
        m-=b
    if m<0:
        n=a
        m-=b
    else:
        n=b
        m=a%b
print("El minimo comúm multiplo es:",n)