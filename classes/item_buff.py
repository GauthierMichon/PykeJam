from classes.item import Item

# Objet des object de changement de stat
class ItemBuff(Item):
    def __init__(self, idItem, name, StatBuff):
        super().__init__(idItem, name)
        self.StatBuff   = StatBuff
