class tipoHabitacion:
    def __init__(self,id_tipo,tipo):
        self.id_tipo = id_tipo
        self.tipoHab = tipo         
    #? getters/setters numeroHab    
    def getidTipo(self):
        return self.id_tipo
    def setNumeroHab(self,id_tip):
        self.id_tipo = id_tip   
    #? getters/setters descripcionHab
    def gettipoHab(self):
        return self.tipoHab
    def setdescripcionHab(self,tip):
        self.tipoHab = tip
    
