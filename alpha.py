# -*- coding: utf-8 -*-

#import
from datetime import *

# fonctions
def nom_jour(numero):
    a = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
    return a[numero]

def nom_mois(numero):
    a = ["", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Decembre"]
    return a[numero]

# debut et fin
d = date.today()
print(d)

mois = d.month
an = d.year

debut = d.replace(an, mois, 1).toordinal()
print("Debut " + str(debut))

mois = mois + 3

if mois > 12:
    mois = mois % 12
    an += 1

fin = d.replace(an, mois, 1).toordinal() - 1
print("fin " + str(fin))

# variables
table = [[] for i in range(3)]
i, j = debut, -1
flag = False
bakMois = ""

# boucle principale
while i <= fin:
    d = date.fromordinal(i)
    print(d, end = " ")

    #semaine
    if flag:
        semaine = "Semaine " + str(d.isocalendar()[1])
        print(semaine)
        table[j].append(semaine)
        flag = False

    #mois
    strMois = nom_mois(d.month)
    if strMois != bakMois:
        j += 1
        print(strMois)
        print()
        table[j].append(strMois)
        table[j].append("-")
    bakMois = strMois

    #jour
    strJour = nom_jour(d.weekday())
    strJour = strJour + " " + str(d.day)
    print(strJour)
    table[j].append(strJour)

    #weekend
    if d.weekday() == 6:
        print()
        table[j].append("-")
        flag = True



    i += 1

# 3 colonnes
une, deux, trois = len(table[0]), len(table[1]), len(table[2])
i = 0
while True:
    cpt = 0
    if i < une:
        print("{:10} ".format(table[0][i]), end = "")
    else:
        print(" " * 11)
        cpt += 1
    
    if i < deux:
        print("{:10} ".format(table[1][i]), end = "")
    else:
        print(" " * 11)
        cpt += 1
    
    if i < trois:
        print("{:10} ".format(table[2][i]))
    else:
        print(" " * 11)
        cpt += 1

    if cpt == 3: break

    i += 1


print(table)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
