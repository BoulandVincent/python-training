# Compter le nombre de valeurs positives dans une liste
numbers = [4, -2, 7, 0, -5, 3]

compteur_chiffre = 0

for number in numbers:
    if number > 0:
        compteur_chiffre += 1
        print("On ajoute 1 au compteur :", compteur_chiffre)

print("Nombre total de valeurs positives :", compteur_chiffre)