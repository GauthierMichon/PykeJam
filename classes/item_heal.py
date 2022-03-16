from classes.item import Item


class ItemHeal(Item):
    def __init__(self, idItem, name, PVHeal):
        super().__init__(self, idItem, name)
        self.PVHeal   = PVHeal
