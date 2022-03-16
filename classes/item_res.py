from classes.item import Item


class ItemRes(Item):
    def __init__(self, idItem, name, PV):
        super().__init__(idItem, name)
        self.PV   = PV
