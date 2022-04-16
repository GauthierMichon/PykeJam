# Objet qui contient les informations d'un dresseur
class Dresseur():
    def __init__(self, name, pokemons, person, inventaire):
        self.name               = name
        self.pokemons           = pokemons
        self.inventaire         = inventaire
        self.actionOblig        = None
        self.actionObligNbTour  = None
        self.person             = person



