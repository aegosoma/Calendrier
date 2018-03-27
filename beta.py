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

    def intervale(date_jour, dico):
        for i in dico:
            #print(i)
            #print(dico[i])
            #print(str(type(dico[i])))
            fin = dico[i] if str(type(dico[i])) == "<class 'int'>" else dico[i][0]
            if i <= date_jour < fin:
                return dico[i]
        return None

# variables
    flag_semaine, flag_samedi, flag_ferie = True, False, False
    i = nbre_ordinal


# mois
    d = date.fromordinal(nbre_ordinal)
    str_mois = nomMois(d.month)
    print('<div class="mois{}">{}'.format(numero_mois, str_mois))
# noms des agents
    print('  <div class="noms"><div class="guy_1">Daniel</div>\
    <div class="guy_2">Pascal</div><div class="guy_3">Nicolas</div></div>')

# boucle
    while True:
        jour_numero, jour_of_semaine, suivant = d.day, d.weekday(), date.fromordinal(i + 1).day
        str_week_ferie, str_contenu, str_scol, str_cong = "", "", "", ""
        str_event = ""

  # ligne semaine
        if jour_of_semaine == 0 or flag_semaine:
            str_astr_cable = astreintes[i][2] if i in astreintes else "?"
            print('  <div class="sem"><div class="sem_astr">{}</div><div class="sem_txt">Semaine {}</div></div>'
              .format(str_astr_cable, d.isocalendar()[1]))
            flag_semaine = False
            table_des_mois[numero_mois - 1].nbr_sem += 1

  # ligne jours
    # numero
        str_jour = str(jour_numero)
        if jour_of_semaine == 5: # samedi
            str_jour = "Sam"
            str_week_ferie = " j_week"
            flag_samedi = True
        if jour_of_semaine == 6: # dimanche
            if flag_samedi: str_jour, str_week_ferie = "Week", " j_week"
            else:           str_jour, str_week_ferie = "Dim", " j_week"

    # contenu
  # fériés
        if d in jours_feries:
            str_week_ferie = " j_fer" # remplace j_week
            str_contenu = '<div class="guy_all">' + jours_feries[d] + '</div>'

  # astreintes
        retourAstreinte = intervale(i, astreintes)
        if retourAstreinte == None: str_astreinte = ""
             # for next days
        else: str_astreinte = '<div class="guy_' + retourAstreinte[1] + ' astr"></div>' 

  # vacances scolaires
        if intervale(i, scolaire) == None: str_scol = ""
        else: str_scol = '<div class="scol"></div>'

  # évenements
        if i in evenements:
            str_event = '<div class="guy_{}">{}</div>'.format(evenements[i][0], evenements[i][1])

  # congés
        if i in conge and conge[i] == "RTT":
            str_cong = '<div class="guy_{} cong">RTT</div>'
           # intervale(i, conge, True):
            

# affichage / creation
        if jour_of_semaine != 5 or (jour_of_semaine == 5 and suivant == 1):
            print('    <div class="jour{}{}"><div class="num">{}</div>{}{}</div>'
            .format(numero_mois, str_week_ferie, str_jour, str_contenu + str_astreinte + str_cong + str_event, str_scol))
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
d = date.today()
#d = d.replace(2016, 3, 12) avr
mois, an = d.month + 0, d.year
debut = d.replace(an, mois, 1).toordinal()

# variables
table = []
table_des_mois = [statMois(), statMois(),statMois()] 
i = 1
nbre_mois = 3
jours_feries = {}
astreintes = {}
scolaire = {}
conge = {}
evenements = {}

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
        astreintes[date(f_annee, f_mois, f_jour).toordinal()] =\
          (date(f_annee, f_mois, f_jour).toordinal() + 7 , f_agent, f_cable)

# récupération des vacances scolaires
with open("./scolaire.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        f = line.strip("\n").split(" ")
        f_annee, f_mois, f_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        g_annee, g_mois, g_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        scolaire[date(f_annee, f_mois, f_jour).toordinal()] =\
          date(g_annee, g_mois, g_jour).toordinal()

# récupération des congés
with open("./conge.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        f = line.strip("\n").split(" ")
        f_annee, f_mois, f_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        item = f.pop(0)
        if item != "RTT":
            g_annee, g_mois, g_jour = int(item), int(f.pop(0)), int(f.pop(0))
            item = date(g_annee, g_mois, g_jour).toordinal()
        conge[date(f_annee, f_mois, f_jour).toordinal()] = item
        print("conge : {} - {}".format(date(f_annee, f_mois, f_jour).toordinal(), item))

# récupération des évenements
with open("./work.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        f = line.strip("\n").split(" ")
        f_annee, f_mois, f_jour = int(f.pop(0)), int(f.pop(0)), int(f.pop(0))
        f_agent, f_texte = f.pop(0), f.pop(0)
        evenements[date(f_annee, f_mois, f_jour).toordinal()] =\
          (f_agent, f_texte)

#for i in evenements:
#    print("date {} agent {} : {}".format(i, evenements[i][0], evenements[i][1]))
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
