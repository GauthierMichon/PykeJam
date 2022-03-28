from BDD.conn import conn
from classes.attaque_autre import AttaqueAutre
from classes.attaque_buff import AttaqueBuff
from classes.attaque_climat import AttaqueClimat
from classes.attaque_heal import AttaqueHeal
from classes.attaque_offensive import AttaqueOffensive
from classes.attaque_statut import AttaqueStatut
from classes.pokemon import Pokemon

def init() :
    attaqueList = initAttaque()
    pokemonList = initPokemon(attaqueList)

    return pokemonList




def initAttaque() :
    select_attaque_cursor = conn.cursor()
    select_attaque_query = ("SELECT * FROM attaques")
    select_attaque_cursor.execute(select_attaque_query)
    data_attaque = select_attaque_cursor.fetchall()

    select_type_cursor = conn.cursor()
    select_type_query = ("SELECT * FROM types")
    select_type_cursor.execute(select_type_query)
    data_type = select_type_cursor.fetchall()

    attaqueList = []

    for i in data_attaque :
        if i[6] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueoffensive WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueOffensive(i[0], i[1], i[2], data_type[i[3]-1][1], i[4], i[5], data_oneattaque[2], data_oneattaque[3], data_oneattaque[4], data_oneattaque[5], data_oneattaque[6], data_oneattaque[7]))
        elif i[7] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueclimat WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()

            select_climat_cursor = conn.cursor()
            select_climat_query = ("SELECT * FROM climat WHERE id = {0}".format(data_oneattaque[2]))
            select_climat_cursor.execute(select_climat_query)
            data_climat = select_climat_cursor.fetchone()

            attaqueList.append(AttaqueClimat(i[0], i[1], i[2], data_type[i[3]-1][1], i[4], i[5], data_climat[1]))
        elif i[8] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueheal WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueHeal(i[0], i[1], i[2], data_type[i[3]-1][1], i[4], i[5], data_oneattaque[2]))
        elif i[9] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaquebuff WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchall()
            statsBuff = []
            nombresBuff = []
            if len(data_oneattaque) > 1 :
                for j in range(len(data_oneattaque)) :
                    statsBuff.append(data_oneattaque[j][2])
                    nombresBuff.append(data_oneattaque[j][3])
            else :
                statsBuff.append(data_oneattaque[0][2])
                nombresBuff.append(data_oneattaque[0][3])
            attaqueList.append(AttaqueBuff(i[0], i[1], i[2], data_type[i[3]-1][1], i[4], i[5], statsBuff, nombresBuff))
        elif i[10] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaquestatut WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueStatut(i[0], i[1], i[2], data_type[i[3]-1][1], i[4], i[5], data_oneattaque[2]))
        elif i[11] == 1 and i[0] != 93 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueautres WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueAutre(i[0], i[1], i[2], data_type[i[3]-1][1], i[4], i[5]))
        elif i[11] == 1 and i[0] == 93 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueautres WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueAutre(i[0], i[1], i[2], None, i[4], i[5]))

    return attaqueList

def initPokemon(attaqueList) :
    select_pokemon_cursor = conn.cursor()
    select_pokemon_query = ("SELECT * FROM pokemon")
    select_pokemon_cursor.execute(select_pokemon_query)
    data_pokemon = select_pokemon_cursor.fetchall()

    select_type_cursor = conn.cursor()
    select_type_query = ("SELECT * FROM types")
    select_type_cursor.execute(select_type_query)
    data_type = select_type_cursor.fetchall()

    select_nature_cursor = conn.cursor()
    select_nature_query = ("SELECT * FROM nature")
    select_nature_cursor.execute(select_nature_query)
    data_nature = select_nature_cursor.fetchall()

    pokemonList = []

    for i in data_pokemon :
        id = i[0]
        name = i[1]
        sprite = i[2]
        spriteDos = i[3]
        Type = data_type[i[4]-1][1]
        Type2 = None
        if i[5] == None :
            Type2 = None
        else :
            Type2 = data_type[i[5]-1][1]

        nature = data_nature[i[6]-1][1]
        PV = ((2 * i[7] + 31) * 100) / 100 + 110
        Att = ((2 * i[8] + 31) * 100) / 100 + 5
        Def = ((2 * i[9] + 31) * 100) / 100 + 5
        AttSpe = ((2 * i[10] + 31) * 100) / 100 + 5
        DefSpe = ((2 * i[11] + 31) * 100) / 100 + 5
        Speed = ((2 * i[12] + 31) * 100) / 100 + 5
        accuracy = i[13]
        Attaques = [attaqueList[i[14]-1], attaqueList[i[15]-1], attaqueList[i[16]-1], attaqueList[i[17]-1]]
        Poids = i[18]
    
        if data_nature[i[6]-1][2] == 'Att' :
            Att *= 1.10
        elif data_nature[i[6]-1][2] == 'AttSpe' :
            AttSpe *= 1.10
        elif data_nature[i[6]-1][2] == 'Def' :
            Def *= 1.10
        elif data_nature[i[6]-1][2] == 'DefSpe' :
            DefSpe *= 1.10
        elif data_nature[i[6]-1][2] == 'Speed' :
            Speed *= 1.10

        if data_nature[i[6]-1][3] == 'Att' :
            Att *= 0.90
        elif data_nature[i[6]-1][3] == 'AttSpe' :
            AttSpe *= 0.90
        elif data_nature[i[6]-1][3] == 'Def' :
            Def *= 0.90
        elif data_nature[i[6]-1][3] == 'DefSpe' :
            DefSpe *= 0.90
        elif data_nature[i[6]-1][3] == 'Speed' :
            Speed *= 0.90

        pokemonList.append(Pokemon(id, name, sprite, spriteDos, Type, Type2, nature, PV, Att, Def, AttSpe, DefSpe, Speed, accuracy, Attaques, Poids))

    return pokemonList