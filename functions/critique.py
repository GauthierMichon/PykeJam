from random import randrange

# Fonction 
def isCrit(Attaque) :
    # Nombre random
    rand = randrange(0, 100)
    # Si l'attaque à un taux de critique élevé
    if Attaque.id == 58 or Attaque.id == 59 or Attaque.id == 117 :
        if rand > 12 :
            return True
        else :
            return False
    else :
        if rand > 6 :
            return False
        else :
            return True