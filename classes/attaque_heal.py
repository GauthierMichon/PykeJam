from classes.attaque import Attaque

# Objet des attaques permettant au pokemon de se soigner
class AttaqueHeal(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel, PVHeal):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
        self.PVHeal   = PVHeal
