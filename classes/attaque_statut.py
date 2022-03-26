from classes.attaque import Attaque


class AttaqueStatut(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, statutId):
        super().__init__(idAttaque, name, accuracy, Type, description, PP)
        self.statutId   = statutId
