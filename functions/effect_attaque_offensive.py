from functions.choose_random_num import rand
from functions.use_effect import useEffect

# Fonction qui gère l'effet d'attaque offensive
def Effect(pokemon_attaquant, pokemon_defenseur, Attaque) :
    # Si l'attaque possède un effet
    if Attaque.effect == 1 :
        randNum = rand(0,100)
        # Si l'effet est inligé
        if randNum <= Attaque.probaEffect :
            pokemon_attaquant, pokemon_defenseur = useEffect(pokemon_attaquant, pokemon_defenseur, Attaque)

    return pokemon_attaquant, pokemon_defenseur