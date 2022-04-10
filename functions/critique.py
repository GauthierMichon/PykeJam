from random import randrange


def isCrit(Attaque) :
    rand = randrange(0, 100)
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