from classes.attaque import Attaque


class AttaqueAutre(Attaque):
    def __init__(self, idAttaque, name, accuracy, typeId, description, PP):
        super().__init__(idAttaque, name, accuracy, typeId, description, PP)
