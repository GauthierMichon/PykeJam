from functions.table_types import TableType

def AttaquePhy(pokemon_attaquant, pokemon_defenseur, Attaque) :

    degats = (100 * 0.4 + 2) * pokemon_attaquant.Att * Attaque.puissance
    degats = degats / (pokemon_defenseur.Def * 50) + 2
    
    #STAB
    if Attaque.Type == pokemon_attaquant.Type or Attaque.Type == pokemon_attaquant.Type2 :
        degats *= 1.5

    #Efficacité type
    TableType(Attaque.Type, pokemon_defenseur.Type, pokemon_defenseur.Type2)

    #Crit

    #Climat

    #Random num entre 0.85 et 1

    return "oui"