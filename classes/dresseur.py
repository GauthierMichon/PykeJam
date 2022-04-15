# Objet qui contient les informations d'un dresseur
class Dresseur():
    def __init__(self, name, pokemons, person):
        self.name               = name
        self.pokemons           = pokemons
        self.inventaire         = None
        self.actionOblig        = None
        self.actionObligNbTour  = None
        self.person             = person



