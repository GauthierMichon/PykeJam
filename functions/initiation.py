from BDD.conn import conn
from classes.attaque_offensive import AttaqueOffensive

def init() :
    select_attaque_cursor = conn.cursor()
    select_attaque_query = ("SELECT * FROM attaques")
    select_attaque_cursor.execute(select_attaque_query)
    data_attaque = select_attaque_cursor.fetchall()

    attaqueList = []

    for i in data_attaque :
        if i[6] == 1 :
            select_oneattaque_cursor = conn.cursor()
            select_oneattaque_query = ("SELECT * FROM attaqueoffensive WHERE idAttaque = {0}".format(i[0]))
            select_oneattaque_cursor.execute(select_oneattaque_query)
            data_oneattaque = select_oneattaque_cursor.fetchone()
            attaqueList.append(AttaqueOffensive(i[0], i[1], i[2], i[3], i[4], i[5], data_oneattaque[2], data_oneattaque[3], data_oneattaque[4], data_oneattaque[5], data_oneattaque[6], data_oneattaque[7]))
        elif i[7] == 1 :
            print("climat")
        elif i[8] == 1 :
            print("heal")
        elif i[9] == 1 :
            print("buff")
        elif i[10] == 1 :
            print("statut")
        elif i[11] == 1 :
            print("autres")

    print(attaqueList)
