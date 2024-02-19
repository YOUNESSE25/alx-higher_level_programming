#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb



if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], datab=sys.argv[3], port=3306)
    curseur = datab.cursor()
    curseur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    linges = curseur.fetchall()
    for linge in linges:
        print(linge)
    curseur.close()
    datab.close()
