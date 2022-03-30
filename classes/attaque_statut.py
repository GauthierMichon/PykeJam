from classes.attaque import Attaque


class AttaqueStatut(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel, statut):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
        self.statut   = statut
