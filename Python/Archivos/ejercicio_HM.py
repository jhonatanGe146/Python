import csv
from Ganador import *

ganadores=[]
with open ('c:\\Users\\APRENDIZ\\Documents\\Jhonatan\\Python\\Python\\Archivos\\oscar_H.csv') as hombres:
    winners_h = csv.reader(hombres)
    
    for i in winners_h:
        ob=Ganador(i[0],i[1],i[2],i[3],i[4])
        ganadores.append(ob)
     
    
    
with open ('c:\\Users\\APRENDIZ\\Documents\\Jhonatan\\Python\\Python\\Archivos\\oscar_M.csv') as mujer:
    winners_m = csv.reader(mujer)
    for i in winners_m:
        ob=Ganador(i[0],i[1],i[2],i[3],i[4])
        ganadores.append(ob)
        
cont=0     
# for i in ganadores:
#     print (i.getIndex(),i.getNombre(), i.getEdad(), i.getMovie(), i.getAño())
#     cont+=1
    


def buscarActor():
    act= (input('Actor a buscar: '))
    l=[]
    for i in ganadores:
        x=i.getNombre()
        l.append(x)
    if act in l:
        print ('esta')


    
buscarActor()

