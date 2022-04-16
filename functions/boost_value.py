# Fonction qui permet de récupérer la le coefficient multiplicateur de boost
def boost(num) :
    if num == 0 :
        return 1
    elif num == 1 :
        return 1.5
    elif num == 2 :
        return 2
    elif num == 3 :
        return 2.5
    elif num == 4 :
        return 3
    elif num == 5 :
        return 3.5
    elif num == 6 :
        return 4
    elif num == -1 :
        return 2/3
    elif num == -2 :
        return 1/2
    elif num == -3 :
        return 2/5
    elif num == -4 :
        return 1/3
    elif num == -5 :
        return 2/7
    elif num == -6 :
        return 1/4