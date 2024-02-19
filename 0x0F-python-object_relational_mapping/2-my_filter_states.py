#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], datab=sys.argv[3], port=3306)
    curseur = datab.cursor()
    curseur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    linges = curseur.fetchall()
    for linge in linges:
        print(linge)
    curseur.close()
    datab.close()
