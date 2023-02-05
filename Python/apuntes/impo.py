from sys import path

#path.append("c:/Users/famil/Documents/Python-1/Python/idioma/tracd/Esp_fran")
#path.append("Python-1/Python/Modulos")
path.append("c:/Users/famil/Documents/Python-1/Python")
#import jhonatan as j

#li=[]  
#print(j.fill(li))
#print(j.sumlist(li))

#from idioma.tracd.Esp_fran import traducir
#! Traducir animales
import idioma.tracd.Esp_fran.mo1
import idioma.tracd.Esp_ing.mo2
import idioma.tracd.Esp_por.mo3
#! Traducir y contaar letras de los animales
import idioma.cont.cont_Esp_Fran.cont_fran
import idioma.cont.cont_Esp_Ing.cont_ing
import idioma.cont.cont_Esp_Port.cont_port
#! Animales y sus acciones
import idioma.acci.acci_fran.ani_fran
import idioma.acci.acci_ing.ani_ing
import idioma.acci.acci_port.ani_port




#! Traducir animales
#print(idioma.tracd.Esp_fran.mo1.traducir())
#print(idioma.tracd.Esp_ing.mo2.traducir())
#print(idioma.tracd.Esp_por.mo3.traducir())
#! Traducir y contaar letras de los animales
#print(idioma.cont.cont_Esp_Fran.cont_fran.contador())
#print(idioma.cont.cont_Esp_Ing.cont_ing.contador2())
#print(idioma.cont.cont_Esp_Port.cont_port.contador3())
#! Animales y sus acciones
x= (idioma.acci.acci_fran.ani_fran.d)
y= (idioma.acci.acci_ing.ani_ing.d)
z= (idioma.acci.acci_port.ani_port.d)

print(idioma.acci.acci_fran.ani_fran.accion_fran(x))
print(idioma.acci.acci_ing.ani_ing.accion_ing(y))
print(idioma.acci.acci_port.ani_port.accion_port(z))