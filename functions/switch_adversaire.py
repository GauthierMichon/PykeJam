from functions.choose_random_num import rand

# Fonction qui gère le changement de pokemon de l'adversaire
def ChangeAdversaire(adversaire, pokemonActuelNum) :
    boolean = True
    while boolean :
        randNum = rand(0, 5)
        if adversaire.pokemons[randNum].PV > 0 and randNum != pokemonActuelNum :
            pokemonActuelNum = randNum
            boolean = False

    return pokemonActuelNum

