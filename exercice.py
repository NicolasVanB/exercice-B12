import random

couples_acceptés = []

def get_donneurs_receveurs():
    fichier = open("B12_liste1.txt","r")  ##Lecture des fichiers txt
    receveurs = []
    donneurs = fichier.read().splitlines()  ##conversion du contenu des fichiers en une liste
    receveurs.extend(donneurs)
    return donneurs, receveurs

def candidats_donneurs_receveurs(donneurs, receveurs):
    donneur = random.choice(donneurs)
    receveur = random.choice(receveurs)
    if donneur == receveur: ##Empêche que les deux mêmes noms soient sélectionnés en même temps
        receveurs.remove(donneur)
        receveur = random.choice(receveurs)
        receveurs.append(donneur)
    if len(donneurs) == 2: ##Supprime la faible probabilité que les deux derniers noms de la liste soient les mêmes
        for nom in donneurs:
            if nom == receveurs[0]:
                donneur = nom
                receveur = receveurs[1]
            if nom == receveurs[1]: 
                donneur = nom
                receveur = receveurs[0]     
    if (receveur, donneur) in couples_acceptés:#empêche l'échange mutuel
        print("Itération déclenchée")
        sauvegarde = receveur
        receveurs.remove(receveur)
        receveur = random.choice(receveurs)
        receveurs.append(sauvegarde)
        print("Echange mutuel corrigé")
    donneurs.remove(donneur)  ##Supprime les deux noms tirés au sort de la liste
    receveurs.remove(receveur)
    couples_acceptés.append((donneur,receveur))
    return donneur, receveur


def trouve_tous_les_donneurs_receveurs(donneurs, receveurs):
    print()
    compteur=0
    couples = []
    while len(donneurs) != 0:
        compteur += 1
        couple = candidats_donneurs_receveurs(donneurs, receveurs)
        couples.append(couple)
        donneur, receveur = couple
        print(donneur + " doit offrir un cadeau à " + receveur) ##Affiche le résultat du tirage au sort
        if compteur == 100:
            break
    return couples

def verifie_regles_couples(couples):
    liste_echanges_mutuels=[]
    liste_echanges_solo=[]
    liste_echanges_doubles=[]
    echange_solo = False
    echange_mutuel = False
    echange_double = False
    for couple in couples:
        for candidats in couples:
            if candidats[0] == couple[1] and candidats[1] == couple[0]:
                echange_mutuel = True
                liste_echanges_mutuels.append(candidats)
            if candidats[0] == candidats[1]:
                echange_solo = True
                liste_echanges_solo.append(candidats)
            if couples.count(candidats)<1:
                echange_double = True
                liste_echanges_doubles.append(candidats)
    print()
    if echange_mutuel == True:
        print("erreur: échange mutuel")
    if echange_solo == True:
        print("erreur: échange à soi-même")
    if echange_double == True:
        print ("erreur: échange double")
    print("liste des problèmes d'échanges mutuels: ",liste_echanges_mutuels)
    print("liste des problèmes d'échanges à soi-même: ",liste_echanges_solo)
    print("liste des problèmes d'échanges doubles: ",liste_echanges_doubles)
    if liste_echanges_mutuels == [] and liste_echanges_solo == [] and liste_echanges_doubles == []:
        print("Aucune erreur détectée")
def cas_reel():
    donneurs, receveurs = get_donneurs_receveurs()        
    couples = trouve_tous_les_donneurs_receveurs(donneurs, receveurs)
    verifie_regles_couples(couples)

def cas_trivial():
    donneurs = [
        "A",
        "B"
        ]
    receveurs = [
        "A",
        "B"
        ]
    couples = trouve_tous_les_donneurs_receveurs(donneurs, receveurs)
    verifie_regles_couples(couples)
    
def simple_cas():
    donneurs = [
        "A",
        "B",
        "C"
        ]
    receveurs = [
        "A",
        "B",
        "C"
        ]
    couples = trouve_tous_les_donneurs_receveurs(donneurs, receveurs)
    verifie_regles_couples(couples)
while compteur < 1000
    simple_cas()
    cas_reel()
