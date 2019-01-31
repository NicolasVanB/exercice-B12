import random


fichier = open("B12_liste1.txt","r")  ##Lecture des fichiers txt
receveurs = []
donneurs = fichier.read().splitlines()  ##conversion du contenu des fichiers en une liste
receveurs.extend(donneurs)

while len(donneurs) != 0:
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
                
    if donneur in receveurs == False and receveur in donneurs == False:
        # Evite l'échange mutuel de cadeaux
        save = receveur
        receveurs.remove(receveur)
        receveur = random.choice(receveurs)
        receveurs.append(save)
    print(donneur + " doit offrir un cadeau à " + receveur) ##Affiche le résultat du tirage au sort
    donneurs.remove(donneur)  ##Supprime les deux noms tirés au sort de la liste
    receveurs.remove(receveur)
    
