from classes.item import Item

# Objet des object de resurection
class ItemRes(Item):
    def __init__(self, idItem, name, PV):
        super().__init__(idItem, name)
        self.PV   = PV
