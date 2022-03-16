from classes.attaque import Attaque


class AttaqueStatut(Attaque):
    def __init__(self, idAttaque, name, accuracy, typeId, description, PP, statutId):
        super().__init__(self, idAttaque, name, accuracy, typeId, description, PP)
        self.statutId   = statutId
