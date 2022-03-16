class Pokemon():
    def __init__(self, id, name, sprite, spriteDos, typeId, typeId2, natureId, PV, Att, Def, AttSpe, DefSpe, Speed, accuracy, Attaques, Poids):
        self.id         = id
        self.name       = name
        self.sprite     = sprite
        self.spriteDos  = spriteDos
        self.typeId     = typeId
        self.typeId2    = typeId2
        self.natureId   = natureId
        self.PV         = PV
        self.PVInit     = PV
        self.Att        = Att
        self.AttInit    = Att
        self.Def        = Def
        self.DefInit    = Def
        self.AttSpe     = AttSpe
        self.AttSpeInit = AttSpe
        self.DefSpe     = DefSpe
        self.DefSpeInit = DefSpe
        self.Speed      = Speed
        self.SpeedInit  = Speed
        self.accuracy   = accuracy
        self.Attaques   = Attaques
        self.Poids      = Poids
        self.statut     = None
        self.confusion  = False



