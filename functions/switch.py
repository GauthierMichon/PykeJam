# Fonction qui réinitialise des propriétés du pokemon qui est changé
def Switch(dresseur, currentPokemonNum) :
    dresseur.pokemons[currentPokemonNum].confusion      = False
    dresseur.pokemons[currentPokemonNum].confusionNum   = None
    dresseur.pokemons[currentPokemonNum].afraid         = False
    dresseur.pokemons[currentPokemonNum].abri           = False
    dresseur.pokemons[currentPokemonNum].clone          = False
    dresseur.pokemons[currentPokemonNum].clonePV        = None
    dresseur.pokemons[currentPokemonNum].maudit         = False
    dresseur.pokemons[currentPokemonNum].requiem        = False
    dresseur.pokemons[currentPokemonNum].requiemNum     = None
    dresseur.pokemons[currentPokemonNum].siphon         = False
    dresseur.pokemons[currentPokemonNum].siphonNum      = None
    dresseur.pokemons[currentPokemonNum].AttBuff        = 0
    dresseur.pokemons[currentPokemonNum].Att            = dresseur.pokemons[currentPokemonNum].AttInit
    dresseur.pokemons[currentPokemonNum].DefBuff        = 0
    dresseur.pokemons[currentPokemonNum].Def            = dresseur.pokemons[currentPokemonNum].DefInit
    dresseur.pokemons[currentPokemonNum].AttSpeBuff     = 0
    dresseur.pokemons[currentPokemonNum].AttSpe         = dresseur.pokemons[currentPokemonNum].AttSpeInit
    dresseur.pokemons[currentPokemonNum].DefSpeBuff     = 0
    dresseur.pokemons[currentPokemonNum].DefSpe         = dresseur.pokemons[currentPokemonNum].DefSpeInit
    dresseur.pokemons[currentPokemonNum].SpeedBuff      = 0
    dresseur.pokemons[currentPokemonNum].Speed          = dresseur.pokemons[currentPokemonNum].SpeedInit
    dresseur.pokemons[currentPokemonNum].accuracy       = dresseur.pokemons[currentPokemonNum].accuracy

    return dresseur
