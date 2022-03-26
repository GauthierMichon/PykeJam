from classes.attaque import Attaque


class AttaqueClimat(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, climatId):
        super().__init__(idAttaque, name, accuracy, Type, description, PP)
        self.climatId   = climatId
