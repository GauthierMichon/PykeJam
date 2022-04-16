from classes.item_heal import ItemHeal
from classes.item_buff import ItemBuff
from classes.item_res import ItemRes
from functions.derouler_item_buff import ActionItemBuff
from functions.derouler_item_heal import ActionItemHeal
from functions.derouler_item_res import ActionItemRes

def ActionItem(dresseur, numItem, pokemonActualPlayerNumber) :
    if type(dresseur.inventaire[numItem]) is ItemHeal :
        print("Item Heal")
        dresseur = ActionItemHeal(dresseur, dresseur.inventaire[numItem])

    elif type(dresseur.inventaire[numItem]) is ItemBuff :
        print("Item Buff")
        dresseur = ActionItemBuff(dresseur, dresseur.inventaire[numItem], pokemonActualPlayerNumber)

    elif type(dresseur.inventaire[numItem]) is ItemRes :
        print("Item Res")
        dresseur = ActionItemRes(dresseur, dresseur.inventaire[numItem])


    dresseur.inventaire.pop(numItem)
    return dresseur