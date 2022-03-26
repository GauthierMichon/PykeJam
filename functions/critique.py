from random import randrange


def isCrit() :
    rand = randrange(0, 100)
    if rand > 6 :
        return False
    else :
        return True