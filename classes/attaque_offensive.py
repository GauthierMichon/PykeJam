from classes.attaque import Attaque


class AttaqueOffensive(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, puissance, physique, special, priorityLevel, effect, probaEffect):
        super().__init__(idAttaque, name, accuracy, Type, description, PP)
        self.puissance   = puissance
        self.physique   = physique
        self.special   = special
        self.priorityLevel    = priorityLevel
        self.effect    = effect
        self.probaEffect    = probaEffect
