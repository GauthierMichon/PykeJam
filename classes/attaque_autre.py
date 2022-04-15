from classes.attaque import Attaque

# Objet des attaques ne rentrant dans aucune autre catégories ou dans plusieurs
class AttaqueAutre(Attaque):
    def __init__(self, idAttaque, name, accuracy, Type, description, PP, priorityLevel):
        super().__init__(idAttaque, name, accuracy, Type, description, PP, priorityLevel)
