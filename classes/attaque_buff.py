from classes.attaque import Attaque

# Objet des attaques changeant les statistiques du pokemon
class AttaqueBuff(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel, statBuff, nombreBuff):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
        self.statBuff   = statBuff
        self.nombreBuff   = nombreBuff
