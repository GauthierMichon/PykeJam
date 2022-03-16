from classes.attaque import Attaque


class AttaqueHeal(Attaque):
    def __init__(self, idAttaque, name, accuracy, typeId, description, PP, PVHeal):
        super().__init__(self, idAttaque, name, accuracy, typeId, description, PP)
        self.PVHeal   = PVHeal
