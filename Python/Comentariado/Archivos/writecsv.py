import csv #Importa el modulo csv
header=['Fruit','Price']#Crea una variable (header) que almacena un lista ['fruit','price']
rows=[['Apple',1200],#crea una variable (rows) que almacena un lista que a su vez tiene listas de con la fruta y el precio
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('archivos/example.csv','w') as csvfile:#Se abre el archivo con ruta relativa o el flujo el cual se renombra a csvfile y tiene como modo de apertura  write
    csvwriter=csv.writer(csvfile)#a la variable csvwrite se le almacena Metodo csv.writer
    csvwriter.writerow(header)
    csvwriter.writerows(rows)