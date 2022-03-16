class Pokemon():
    def __init__(self, id, name, sprite, spriteDos, Type, Type2, nature, PV, Att, Def, AttSpe, DefSpe, Speed, accuracy, Attaques, Poids):
        self.id         = id
        self.name       = name
        self.sprite     = sprite
        self.spriteDos  = spriteDos
        self.Type       = Type
        self.Type2      = Type2
        self.nature     = nature
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



