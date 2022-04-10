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
        self.PVMax      = PV
        self.Att        = Att
        self.AttInit    = Att
        self.AttBuff    = 0
        self.Def        = Def
        self.DefInit    = Def
        self.DefBuff    = 0
        self.AttSpe     = AttSpe
        self.AttSpeInit = AttSpe
        self.AttSpeBuff = 0
        self.DefSpe     = DefSpe
        self.DefSpeInit = DefSpe
        self.DefSpeBuff = 0
        self.Speed      = Speed
        self.SpeedInit  = Speed
        self.SpeedBuff  = 0
        self.accuracy   = accuracy
        self.Attaques   = Attaques
        self.Poids      = Poids
        self.statut     = None
        self.confusion  = False
        self.confusionNum  = None
        self.afraid     = False
        self.abri       = False
        self.clone      = False
        self.clonePV    = None
        self.maudit     = False
        self.requiem    = False
        self.requiemNum = None
        self.siphon     = False
        self.siphonNum  = None



