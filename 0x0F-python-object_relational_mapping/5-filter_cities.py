#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state
"""
import sys
import MySQLdb


if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], datab=sys.argv[3], port=3306)
    curseur = datab.cursor()
    curseur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    linges = curseur.fetchall()
    tmp = list(linge[0] for linge in linges)
    print(*tmp, sep=", ")
    curseur.close()
    datab.close()
