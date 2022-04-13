from functions.choose_random_num import rand


def ChangeAdversaire(adversaire, pokemonActuelNum) :
    boolean = True
    while boolean :
        randNum = rand(0, 5)
        if adversaire.pokemons[randNum].PV > 0 :
            pokemonActuelNum = randNum
            boolean = False

    return pokemonActuelNum

