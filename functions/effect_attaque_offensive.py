from functions.choose_random_num import rand
from functions.use_effect import useEffect

def Effect(pokemon_attaquant, pokemon_defenseur, Attaque) :
    if Attaque.effect == 1 :
        randNum = rand(0,100)
        if randNum <= Attaque.probaEffect :
            pokemon_attaquant, pokemon_defenseur = useEffect(pokemon_attaquant, pokemon_defenseur, Attaque)

    return pokemon_attaquant, pokemon_defenseur