from classes.attaque import Attaque

# Objet des attaques changeant le climat
class AttaqueClimat(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel, climat):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
        self.climat   = climat
