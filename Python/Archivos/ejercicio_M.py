from Ganador import *
import csv


obs_muj=[]
ganadores_muj=[]
with open ('c:\\Users\\APRENDIZ\\Documents\\Jhonatan\\Python\\Python\\Archivos\\oscar_M.csv') as mujer:
    winners = csv.reader(mujer)
    
    for i in winners:
        ganadores_muj.append(winners)
        # print('index: ', i[0])
        # print('Año: ', i[1])
        # print('Edad: ', i[2])
        # print('Nombre: ', i[3])
        # print('movies: ', i[4])
        ob=Ganador(i[0],i[1],i[2],i[3],i[4])
        obs_muj.append(ob)
    

#print(ganadores_hom)for row in csvReader:
for i in obs_muj:
    print(i.getNombre(),i.getMovie())
        