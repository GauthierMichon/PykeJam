from classes.attaque import Attaque


class AttaqueClimat(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, climat):
        super().__init__(idAttaque, name, accuracy, Type, description, PP)
        self.climat   = climat
