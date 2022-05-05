from functions.attaque_miss_or_work import MissWork
from functions.boost_value import boost
from graph.write_info import WriteInfo

# Fonction qui gère les attaques de buff
def Buff(pokemon_attaquant, Attaque) :
    # Si l'attaque réussit
    if MissWork(pokemon_attaquant, Attaque) :
        for i in range(len(Attaque.statBuff)) :

            
            
            if Attaque.statBuff[i] != "accuracy" :
                # On récupère la statistique de base
                initStat = getattr(pokemon_attaquant, (Attaque.statBuff[i] + "Init"))

                # On récupère le nombre de buff actuel de la statistique
                buff = getattr(pokemon_attaquant, (Attaque.statBuff[i] + "Buff"))
                # On ajoute le nombre de buff qu'apporte l'attaque
                buff += Attaque.nombreBuff[i]
                # On vérifie si le nombre de buff ne dépasse pas 6 ou n'est pas inférieur à -6
                if buff > 6 :
                    buff = 6
                elif buff < -6 :
                    buff = -6
                
                # On recalcul la statistique
                newStat = initStat * boost(buff)
                # On set les nouvelles valeurs
                setattr(pokemon_attaquant, Attaque.statBuff[i], newStat)
                setattr(pokemon_attaquant, (Attaque.statBuff[i] + "Buff"), buff)
            else :
                # On récupère le nombre de buff actuel de la statistique
                buff = getattr(pokemon_attaquant, (Attaque.statBuff[i]))
                
                buff += Attaque.nombreBuff[i]
                # On vérifie si le nombre de buff ne dépasse pas 6 ou n'est pas inférieur à -6
                if buff > 6 :
                    buff = 6
                elif buff < -6 :
                    buff = -6

                setattr(pokemon_attaquant, Attaque.statBuff[i], buff)

            statText, buffText = TextBuff(i, Attaque)
            WriteInfo(statText + pokemon_attaquant.name + buffText)
            

    return pokemon_attaquant



def TextBuff(i, Attaque) :
    statText = ""
    buffText = ""

    if Attaque.statBuff[i] == "Att" :
        statText = "L'Attaque de "
    elif Attaque.statBuff[i] == "Def" :
        statText = "La Défense de "
    elif Attaque.statBuff[i] == "AttSpe" :
        statText = "L'Attaque Spéciale de "
    elif Attaque.statBuff[i] == "DefSpe" :
        statText = "La Défense Spéciale de "
    elif Attaque.statBuff[i] == "Speed" :
        statText = "La Vitesse de "
    else :
        statText = "La Précision de "

    if Attaque.nombreBuff[i] == 1 :
        buffText = " augmente !"
    elif Attaque.nombreBuff[i] == -1 :
        buffText = " baisse !"
    elif Attaque.nombreBuff[i] == 2 :
        buffText = " augmente beaucoup !"
    elif Attaque.nombreBuff[i] == -2 :
        buffText = " baisse beaucoup !"

    return statText, buffText