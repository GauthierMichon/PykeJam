from functions.boost_value import boost
from functions.choose_random_num import rand

def useEffect(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if Attaque.id == 3 :
        if pokemon_defenseur.DefBuff > -6 :
            pokemon_defenseur.DefBuff -= 1
            pokemon_defenseur.Def = pokemon_defenseur.DefInit * boost(pokemon_defenseur.DefBuff)
        
    if Attaque.id == 10 :
        if pokemon_defenseur.DefSpeBuff > -6 :
            pokemon_defenseur.DefSpeBuff -= 1
            pokemon_defenseur.DefSpe = pokemon_defenseur.DefSpeInit * boost(pokemon_defenseur.DefSpeBuff)
    
    if Attaque.id == 14 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Empoisonnement"
    
    if Attaque.id == 16 :
        if pokemon_defenseur.DefSpeBuff > -6 :
            pokemon_defenseur.DefSpeBuff -= 1
            pokemon_defenseur.DefSpe = pokemon_defenseur.DefSpeInit * boost(pokemon_defenseur.DefSpeBuff)
    
    if Attaque.id == 18 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Brûlure"
    
    if Attaque.id == 19 :
        pokemon_defenseur.afraid = True

    if Attaque.id == 29 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Paralysie"
    if Attaque.id == 30 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Empoisonnement"

    if Attaque.id == 37 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Brûlure"

    if Attaque.id == 38 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Empoisonnement"

    if Attaque.id == 40 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Brûlure"

    if Attaque.id == 45 :
        if pokemon_defenseur.DefSpeBuff > -6 :
            pokemon_defenseur.DefSpeBuff -= 1
            pokemon_defenseur.DefSpe = pokemon_defenseur.DefSpeInit * boost(pokemon_defenseur.DefSpeBuff)

    if Attaque.id == 57 :
        pokemon_defenseur.afraid = True

    if Attaque.id == 60 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Brûlure"

    if Attaque.id == 62 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Gel"

    if Attaque.id == 63 :
        if pokemon_defenseur.DefSpeBuff > -6 :
            pokemon_defenseur.DefSpeBuff -= 1
            pokemon_defenseur.DefSpe = pokemon_defenseur.DefSpeInit * boost(pokemon_defenseur.DefSpeBuff)

    if Attaque.id == 64 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Gel"

    if Attaque.id == 68 :
        if pokemon_defenseur.DefBuff > -6 :
            pokemon_defenseur.DefBuff -= 1
            pokemon_defenseur.Def = pokemon_defenseur.DefInit * boost(pokemon_defenseur.DefBuff)

    if Attaque.id == 82 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Paralysie"

    if Attaque.id == 84 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Gel"

    if Attaque.id == 85 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Brûlure"

    if Attaque.id == 86 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Paralysie"
    
    if Attaque.id == 90 :
        if pokemon_defenseur.AttSpeBuff > -6 :
            pokemon_defenseur.AttSpeBuff -= 1
            pokemon_defenseur.AttSpe = pokemon_defenseur.AttSpeInit * boost(pokemon_defenseur.AttSpeBuff)

    if Attaque.id == 92 :
        if pokemon_defenseur.DefSpeBuff > -6 :
            pokemon_defenseur.DefSpeBuff -= 1
            pokemon_defenseur.DefSpe = pokemon_defenseur.DefSpeInit * boost(pokemon_defenseur.DefSpeBuff)

    if Attaque.id == 95 :
        if pokemon_defenseur.confusion == False :
            pokemon_defenseur.confusion = True
            pokemon_defenseur.confusionNum = rand(1, 4)

    if Attaque.id == 111 :
        if pokemon_defenseur.DefSpeBuff > -6 :
            pokemon_defenseur.DefSpeBuff -= 1
            pokemon_defenseur.DefSpe = pokemon_defenseur.DefSpeInit * boost(pokemon_defenseur.DefSpeBuff)

    if Attaque.id == 112 :
        if pokemon_defenseur.statut == None :
            pokemon_defenseur.statut = "Paralysie"

    if Attaque.id == 122 :
        if pokemon_defenseur.confusion == False :
            pokemon_defenseur.confusion = True
            pokemon_defenseur.confusionNum = rand(1, 4)

    if Attaque.id == 123 :
        if pokemon_defenseur.confusion == False :
            pokemon_defenseur.confusionNum = rand(1, 4)

    if Attaque.id == 124 :
        pokemon_defenseur.afraid = True


    return pokemon_attaquant, pokemon_defenseur