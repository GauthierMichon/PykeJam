from classes.attaque import Attaque


class AttaqueClimat(Attaque):
    def __init__(self, idAttaque, name, accuracy, typeId, description, PP, climatId):
        super().__init__(idAttaque, name, accuracy, typeId, description, PP)
        self.climatId   = climatId
