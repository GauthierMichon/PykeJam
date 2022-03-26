from functions.critique import isCrit
from functions.table_types import TableType

def AttaquePhy(pokemon_attaquant, pokemon_defenseur, Attaque) :

    degats = (100 * 0.4 + 2) * pokemon_attaquant.Att * Attaque.puissance
    degats = degats / (pokemon_defenseur.Def * 50) + 2
    
    #STAB
    if Attaque.Type == pokemon_attaquant.Type or Attaque.Type == pokemon_attaquant.Type2 :
        degats *= 1.5

    #Efficacité type
    eff = TableType(Attaque.Type, pokemon_defenseur.Type, pokemon_defenseur.Type2)
    if eff == 0 :
        print("inefficace")
    elif eff == 0.5 :
        print("peu efficace")
    elif eff == 1 :
        print("efficace")
    elif eff >= 2 :
        print("super efficace")
    else : 
        print("problème efficacité")

    degats *= eff

    #Crit
    if isCrit() :
        print("Coup Critique")
        degats *= 2

    #Climat


    #Random num entre 0.85 et 1

    return "oui"