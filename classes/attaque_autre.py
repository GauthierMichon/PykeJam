from classes.attaque import Attaque


class AttaqueAutre(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
