def ColorAttaque(type) :
    color = None
    if type == "Normal" :
        color = (219, 220, 221)
    elif type == "Feu" :
        color = (250, 155, 83)
    elif type == "Eau" :
        color = (77,147,212)
    elif type == "Plante" :
        color = (102, 189, 94)
    elif type == "Electrik" :
        color = (243, 211, 61)
    elif type == "Glace" :
        color = (116, 205, 194)
    elif type == "Combat" :
        color = (205, 68, 112)
    elif type == "Poison" :
        color = (173, 110, 203)
    elif type == "Sol" :
        color = (219, 123, 69)
    elif type == "Vol" :
        color = (147, 172, 221)
    elif type == "Psy" :
        color = (249, 116, 123)
    elif type == "Insecte" :
        color = (147, 194, 47)
    elif type == "Roche" :
        color = (196, 185, 140)
    elif type == "Spectre" :
        color = (85, 108, 174)
    elif type == "Dragon" :
        color = (9, 111, 197)
    elif type == "Tenebre" :
        color = (71, 70, 79)
    elif type == "Acier" :
        color = (90, 140, 162)
    elif type == "Fee" :
        color = (236, 146, 228)

    if color == None :
        color = (255, 255, 255)
    return color

    
