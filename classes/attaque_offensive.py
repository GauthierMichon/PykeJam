from classes.attaque import Attaque


class AttaqueOffensive(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel, puissance, physique, special, effect, probaEffect):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
        self.puissance   = puissance
        self.physique   = physique
        self.special   = special
        self.effect    = effect
        self.probaEffect    = probaEffect
