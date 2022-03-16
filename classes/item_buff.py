from classes.item import Item


class ItemBuff(Item):
    def __init__(self, idItem, name, StatBuff):
        super().__init__(idItem, name)
        self.StatBuff   = StatBuff
