class Terrain():
    def __init__(self, climat, Picots, PicsToxik, PiegeDeRoc, Vampigraine, PicotsAdverse, PicsToxikAdverse, PiegeDeRocAdverse, VampigraineAdverse):
        self.climat                 = climat
        self.Picots                 = Picots
        self.PicsToxik              = PicsToxik
        self.PiegeDeRoc             = PiegeDeRoc
        self.Vampigraine            = Vampigraine
        self.VoeuNbTour             = None
        self.VoeuPVHeal             = None
        self.PicotsAdverse          = PicotsAdverse
        self.PicsToxikAdverse       = PicsToxikAdverse
        self.PiegeDeRocAdverse      = PiegeDeRocAdverse
        self.VampigraineAdverse     = VampigraineAdverse
        self.VoeuAdverseNbTour      = None
        self.VoeuAdversePVHeal      = None

