# -*- coding: utf-8 -*-

#import
from datetime import *

# classe
class statMois(object):
    def __init__(self):
        self.nbr_jr = 0
        self.nbr_w_f = 0
        self.nbr_sem = 0
        self.h_f = 0
        self.h_j = 0
    def calcul():
        return (self.h_j, self.h_f)

# fonctions
def creationMois(numero_mois, nbre_ordinal, table):

    def nomMois(numero):
        a = ["zero", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Decembre"]
        return a[numero]

    def intervale(date_jour, dico, flag = False):
        for i in dico:
            fin = dico[i][0] if flag else dico[i]
            if i <= date_jour < fin: return True
        return False

    # variables
    flag_semaine, flag_ferie = False, False
    i = nbre_ordinal
    str_astreinte = ""

    # mois
    d = date.fromordinal(nbre_ordinal)
    str_mois = nomMois(d.month)
    print('<div class="mois{}">{}'.format(numero_mois, str_mois))

    # boucle
    while True:
        jour_numero, jour_of_semaine = d.day, d.weekday()
        str_week_ferie, str_contenu, str_txt_ferie, str_scol = "", "", "", ""

    # ligne semaine
        if jour_of_semaine == 9 or flag_semaine:
            str_astr_cable = astreintes[i][2] if i in astreintes else "?"
            gus_astreinte = astreintes[i][1] if i in astreintes else "?"
            print('  <div class="sem">Semaine {}<div class="astr_cable">{}</div></div>'
              .format(d.isocalendar()[1], str_astr_cable))
            flag_semaine = False
            table_des_mois[numero_mois - 1].nbr_sem += 1

    # ligne jours
# numero
        str_jour = str(jour_numero)
        if jour_of_semaine == 5: # samedi
            str_jour = "S" + str_jour
            str_week_ferie = " j_sam"
        if jour_of_semaine == 6: # dimanche
            str_jour = "D" + str_jour
            str_week_ferie = " j_dim"

        # contenu
# fériés
        if d in jours_feries:
            str_week_ferie = " j_fer" # remplace j_week
            str_txt_ferie = jours_feries[d] + '</br>'

# astreintes
        str_astreinte = '<div class="astr"></div>' if intervale(i, astreintes, True) else ""

# vacances scolaire
        str_scol = '<div class="scol"></div>' if intervale(i, scolaire) else ""

# contenu
        if jour_of_semaine in contenu:
            str_contenu = contenu[jour_of_semaine] + '</br>'
        if i in contenu:
            str_contenu += contenu[i]

        # affichage / creation
        print('    <div class="jour{}"><div class="num">{}</div><div class="texte">{}</div>{}{}</div>'
            .format(str_week_ferie, str_jour, str_txt_ferie + str_contenu, str_astreinte, str_scol))
        if str_week_ferie:
            table_des_mois[numero_mois - 1].nbr_w_f += 1
        else:
            table_des_mois[numero_mois - 1].nbr_jr += 1

        # fin de boucle
        
        i += 1
        d = date.fromordinal(i)
        if d.day == 1:
            print('</div>')
            return (i, table)# << todo - mois suivant


                # # # # # # # # # #
# date du debut
d = date.today().replace(2018, 3, 1)
mois, an = d.month, d.year
debut = d.replace(an, mois, 1).toordinal()

# variables
table = []
table_des_mois = [statMois(), statMois(),statMois()] 
i = 1
nbre_mois = 3
jours_feries = {}
astreintes = {}
scolaire = {}
contenu = {}

# récupération des jours fériés
with open("./ferie.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        f = line.strip("\n").split(" ")
        f_mois, f_jour = int(f.pop(0)), int(f.pop(0))
        f_texte = f.pop(0)
        while len(f):
            f_texte +=  " " + f.pop(0)
        jours_feries[date(an, f_mois, f_jour)] = f_texte
        jours_feries[date(an + 1, f_mois, f_jour)] = f_texte # ???? todo

# récupération des astreintes
with open("./astreinte.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        f = line.strip("\n").split(" ")
        f_annee, f_mois, f_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        f_agent, f_cable = f.pop(0), f.pop(0)  
        if f_agent == "2":
            astreintes[date(f_annee, f_mois, f_jour).toordinal()] =\
          (date(f_annee, f_mois, f_jour).toordinal() + 7 , f_agent, f_cable)
            #print("{}/{}".format(f_jour, f_mois))

# récupération des vacances scolaires
with open("./scolaire.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        f = line.strip("\n").split(" ")
        f_annee, f_mois, f_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        g_annee, g_mois, g_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        scolaire[date(f_annee, f_mois, f_jour).toordinal()] =\
          date(g_annee, g_mois, g_jour).toordinal()

# récupération des contenus
flag = False
with open("./home.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        if flag: f = line.strip("\n")
        else: f = line.strip("\n").split(" ")
        #print(f)

        if flag == False:
            f_str = f.pop(0)
            if f_str == "hebdo":
                f_jour = int(f.pop(0))
                flag = True
                continue
            else:
                f_annee, f_mois, f_jour = int(f_str), int(f.pop(0)), int(f.pop(0))
                flag = True
                continue

        if flag:
            clef = f_jour if f_str == "hebdo" else date(f_annee, f_mois, f_jour).toordinal()
            contenu[clef] = f
            flag = False
            print("{} : {}".format(clef, f))
            print()
#for i in astreintes:
#    print("debut {}, fin {}, agent {}, cable {}".format(i.fromordinal(), astreintes[i][0], astreintes[i][1], astreintes[i][2]))
#exit()
    

# boucle principale
for i in range(1, nbre_mois + 1):
    #print("mois N°{}".format(i))

    a = creationMois(i, debut, table)

    #print("retour: {}".format(a))

    debut = a[0]
 
# stat
for i in range(nbre_mois):
    print("mois {}\nJours : {}\nWeek/ferie :{}\nSemaines :{}"
    .format(i, table_des_mois[i].nbr_jr,
    table_des_mois[i].nbr_w_f,
    table_des_mois[i].nbr_sem))

  

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
