import random
fichier=open("B12_liste1.txt","r") ##Lecture des fichiers txt
liste_B12B=[]
liste_B12A=fichier.read().splitlines()##conversion du contenu des fichiers en une liste
liste_B12B.extend(liste_B12A)
indiceB=0
print(liste_B12A)
print(liste_B12B)
while len(liste_B12A) != 0:
    A=random.choice(liste_B12A)
    B=random.choice(liste_B12B)
    if A == B: ##Empêche que les deux mêmes noms soient sélectionnés en même temps
        liste_B12B.remove(A)
        B=random.choice(liste_B12B)
        liste_B12B.append(A)
    if len(liste_B12A)==2: ##Supprime la faible probabilité que les deux derniers noms de la liste soient les mêmes
        for nom in liste_B12A:
            if nom == liste_B12B[0]:
                A=nom
                B=liste_B12B[1]
            if nom == liste_B12B[1]: 
                A=nom
                B=liste_B12B[0]
    if A in liste_B12B == False and B in liste_B12A == False:
        save=B
        liste_B12B.remove(B)
        B=random.choice(liste_B12B)
        B=save
        liste_B12B.append(B)
    print(A+" dois offrir un cadeau à "+B) ##Affiche le résultat du tirage au sort
    liste_B12A.remove(A)##Supprime les deux noms tirés au sort de la liste
    liste_B12B.remove(B)
