l = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista=[]


for i in range(len(l)):
    if l[i] not in lista[:]:
        lista.append(l[i])

print("La lista con elementos únicos:")
print(lista)
