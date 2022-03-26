from classes.attaque import Attaque


class AttaqueBuff(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, statBuff, nombreBuff):
        super().__init__(idAttaque, name, accuracy, Type, description, PP)
        self.statBuff   = statBuff
        self.nombreBuff   = nombreBuff
