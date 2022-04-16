from functions.fonctions_attaque_autre import Abri, AntiBrume, Balance, BallMeteo, BlablaDodo, BouleRoc, BouteFeu, CasseBrique, ChangeEclair, ChocPsy, Clairvoyance, Clonage, CloseCombat, Colere, Conversion, Damocles, DemiTour, DracoMeteore, EclairFou, Effort, Explosion, Facade, FrappeAtlas, GlasDeSoin, LanceSoleil, Malediction, Megaphone, NoeudHerbe, Picots, PicsToxik, PiedSaute, PiedVoltige, PiegeDeRoc, Projection, PuissanceCachee, Rapace, Repos, Requiem, Sabotage, Siphon, Souvenir, Stalactite, Surchauffe, Surpuissance, Synthese, TourDeMagie, TourRapide, VampiPoing, Vampigraine, Vampirisme, VentArriere, Voeu, VoleForce

# Fonction qui gère les attaques autres en appelant leur fonction correspondante
def Autres(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque, pokemonActuelNum) :
    if Attaque.id == 1 :
        pokemon_attaquant = Abri(pokemon_attaquant, Attaque)
    elif Attaque.id == 2 :
        terrain = AntiBrume(pokemon_attaquant, Attaque, terrain)
    elif Attaque.id == 8 :
        pokemon_attaquant, pokemon_defenseur = Balance(pokemon_attaquant, pokemon_defenseur, Attaque)
    elif Attaque.id == 9 :
        pokemon_defenseur = BallMeteo(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 12 :
        pokemon_attaquant, pokemon_defenseur, terrain = BlablaDodo(pokemon_attaquant, pokemon_defenseur, terrain)
    elif Attaque.id == 15 :
        pokemon_defenseur = BouleRoc(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 17 :
        pokemon_attaquant, pokemon_defenseur = BouteFeu(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 20 :
        pokemon_defenseur = CasseBrique(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 21 :
        pokemon_defenseur, pokemonActuelNum = ChangeEclair(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, pokemonActuelNum)
    elif Attaque.id == 22 :
        pokemon_defenseur = ChocPsy(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 23 :
        pokemon_attaquant = Clairvoyance(pokemon_attaquant, Attaque)
    elif Attaque.id == 24 :
        pokemon_attaquant = Clonage(pokemon_attaquant)
    elif Attaque.id == 25 :
        pokemon_attaquant, pokemon_defenseur = CloseCombat(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 26 :
        pokemon_attaquant, pokemon_defenseur, dresseurPokemonAttaquant = Colere(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque)
    elif Attaque.id == 27 :
        pokemon_attaquant = Conversion(pokemon_attaquant, Attaque)
    elif Attaque.id == 31 :
        pokemon_attaquant, pokemon_defenseur = Damocles(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 35 :
        pokemon_defenseur, pokemonActuelNum = DemiTour(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, pokemonActuelNum)
    elif Attaque.id == 36 :
        pokemon_attaquant, pokemon_defenseur = DracoMeteore(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 41 :
        pokemon_attaquant, pokemon_defenseur = EclairFou(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 43 :
        pokemon_defenseur = Effort(pokemon_attaquant, pokemon_defenseur, Attaque)
    elif Attaque.id == 46 :
        pokemon_attaquant, pokemon_defenseur = Explosion(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 48 :
        pokemon_defenseur = Facade(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 50 :
        pokemon_defenseur = FrappeAtlas(pokemon_attaquant, pokemon_defenseur, Attaque)
    elif Attaque.id == 51 :
        dresseurPokemonAttaquant = GlasDeSoin(dresseurPokemonAttaquant)
    elif Attaque.id == 61 :
        pokemon_defenseur, dresseurPokemonAttaquant = LanceSoleil(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant, numAttaque)
    elif Attaque.id == 67 :
        pokemon_attaquant, pokemon_defenseur = Malediction(pokemon_attaquant, pokemon_defenseur, Attaque)
    elif Attaque.id == 70 :
        pokemon_defenseur = Megaphone(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 71 :
        pokemon_defenseur = NoeudHerbe(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 75 :
        terrain = Picots(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque)
    elif Attaque.id == 76 :
        terrain = PicsToxik(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque)
    elif Attaque.id == 77 :
        pokemon_attaquant, pokemon_defenseur = PiedSaute(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 78 :
        pokemon_attaquant, pokemon_defenseur = PiedVoltige(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 80 :
        terrain = PiegeDeRoc(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque)
    elif Attaque.id == 91 :
        pokemonActuelNum = Projection(pokemon_defenseur, dresseurPokemonAttaquant, pokemonActuelNum)
    elif Attaque.id == 93 :
        pokemon_defenseur = PuissanceCachee(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 94 :
        pokemon_attaquant, pokemon_defenseur = Rapace(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 97 :
        pokemon_attaquant = Repos(pokemon_attaquant)
    elif Attaque.id == 98 :
        pokemon_attaquant, pokemon_defenseur = Requiem(pokemon_attaquant, pokemon_defenseur)
    elif Attaque.id == 100 :
        pokemon_attaquant = Sabotage(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 101 :
        pokemon_defenseur = Siphon(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 103 :
        pokemon_attaquant, pokemon_defenseur = Souvenir(pokemon_attaquant, pokemon_defenseur)
    elif Attaque.id == 105 :
        pokemon_defenseur = Stalactite(pokemon_attaquant, pokemon_defenseur, Attaque, terrain) 
    elif Attaque.id == 106 :
        pokemon_attaquant, pokemon_defenseur = Surchauffe(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 108 :
        pokemon_attaquant, pokemon_defenseur = Surpuissance(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 109 :
        pokemon_attaquant = Synthese(pokemon_attaquant, terrain)
    elif Attaque.id == 113 :
        pokemon_defenseur = TourDeMagie(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 114 :
        pokemon_attaquant, pokemon_defenseur, terrain = TourRapide(pokemon_attaquant, pokemon_defenseur, Attaque, terrain, dresseurPokemonAttaquant)
    elif Attaque.id == 118 :
        pokemon_attaquant, pokemon_defenseur = VampiPoing(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 119 :
        terrain = Vampigraine(dresseurPokemonAttaquant, terrain, pokemon_attaquant, Attaque)
    elif Attaque.id == 120 :
        pokemon_attaquant, pokemon_defenseur = Vampirisme(pokemon_attaquant, pokemon_defenseur, Attaque, terrain)
    elif Attaque.id == 121 :
        dresseurPokemonAttaquant = VentArriere(dresseurPokemonAttaquant, pokemon_attaquant, Attaque)
    elif Attaque.id == 127 :
        terrain = Voeu(pokemon_attaquant, Attaque, terrain, dresseurPokemonAttaquant)
    elif Attaque.id == 128 :
        pokemon_attaquant, pokemon_defenseur = VoleForce(pokemon_attaquant, Attaque, pokemon_defenseur)
    

    return pokemon_attaquant, pokemon_defenseur, terrain, dresseurPokemonAttaquant, pokemonActuelNum