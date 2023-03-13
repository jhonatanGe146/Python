from Ganador import *
import csv


obs_hombre=[]
ganadores_hom=[]
with open ('c:\\Users\\APRENDIZ\\Documents\\Jhonatan\\Python\\Python\\Archivos\\oscar_H.csv') as hombres:
    winners = csv.reader(hombres)
    
    for i in winners:
        ganadores_hom.append(winners)
        # print('index: ', i[0])
        # print('Año: ', i[1])
        # print('Edad: ', i[2])
        # print('Nombre: ', i[3])
        # print('movies: ', i[4])
        ob=Ganador(i[0],i[1],i[2],i[3],i[4])
        obs_hombre.append(ob)
    

#print(ganadores_hom)for row in csvReader:
for i in obs_hombre:
    print(i.getNombre(),i.getMovie())
        