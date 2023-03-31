class habitacion:
    def __init__(self,nh,d,s):
        self.numeroHab = nh
        self.descripcionHab = d
        self.estado=s        
    #? getters/setters numeroHab    
    def getNumeroHab(self):
        return self.numeroHab
    def setNumeroHab(self,numeroHab):
        self.numeroHab = numeroHab
        
    #? getters/setters descripcionHab
    def getdescripcionHab(self):
        return self.descripcionHab
    def setdescripcionHab(self,descr):
        self.descripcionHab = descr
    
    #? getters/setters
    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estado=estado
        
        


# h1=habitacion()
# lis=[]
# for i in range(2):
#     h1.insertHab()
#     lis.append(h1)
# print(len(lis))
# print(type(h1))
# #print(h1.getNumeroHab())
# #print(h1.getdescripcionHab())
# #h1.setNumeroHab(205)
# # h1.setdescripcionHab('era mentira')
# # print(h1.getNumeroHab())
# # print(h1.getdescripcionHab())