from classes.attaque import Attaque


class AttaqueHeal(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, PVHeal):
        super().__init__(idAttaque, name, accuracy, Type, description, PP)
        self.PVHeal   = PVHeal
