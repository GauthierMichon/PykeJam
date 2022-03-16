from BDD.conn import conn
from classes.attaque_autre import AttaqueAutre
from classes.attaque_buff import AttaqueBuff
from classes.attaque_climat import AttaqueClimat
from classes.attaque_heal import AttaqueHeal
from classes.attaque_offensive import AttaqueOffensive
from classes.attaque_statut import AttaqueStatut

def init() :
    select_attaque_cursor = conn.cursor()
    select_attaque_query = ("SELECT * FROM attaques")
    select_attaque_cursor.execute(select_attaque_query)
    data_attaque = select_attaque_cursor.fetchall()

    attaqueList = []

    for i in data_attaque :
        if i[6] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueoffensive WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueOffensive(i[0], i[1], i[2], i[3], i[4], i[5], data_oneattaque[2], data_oneattaque[3], data_oneattaque[4], data_oneattaque[5], data_oneattaque[6], data_oneattaque[7]))
        elif i[7] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueclimat WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueClimat(i[0], i[1], i[2], i[3], i[4], i[5], data_oneattaque[2]))
        elif i[8] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueheal WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueHeal(i[0], i[1], i[2], i[3], i[4], i[5], data_oneattaque[2]))
        elif i[9] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaquebuff WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueBuff(i[0], i[1], i[2], i[3], i[4], i[5], data_oneattaque[2], data_oneattaque[3]))
        elif i[10] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaquestatut WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueStatut(i[0], i[1], i[2], i[3], i[4], i[5], data_oneattaque[2]))
        elif i[11] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueautres WHERE attaqueId = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueAutre(i[0], i[1], i[2], i[3], i[4], i[5]))

    print(attaqueList[52])
