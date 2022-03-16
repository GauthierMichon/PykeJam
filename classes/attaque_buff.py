from classes.attaque import Attaque


class AttaqueBuff(Attaque):
    def __init__(self, idAttaque, name, accuracy, typeId, description, PP, statBuff, nombreBuff):
        super().__init__(self, idAttaque, name, accuracy, typeId, description, PP)
        self.statBuff   = statBuff
        self.nombreBuff   = nombreBuff
