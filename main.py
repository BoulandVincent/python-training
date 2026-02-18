# Exercice 18/02/2026

# Trouver le plus grand nombre d'une liste
numbers = [4,7,2,9,1]

# Initialise champion avec la valeur 0 il pourras s'adapter a toutes les liste
champion = numbers[0]
 
# Permet de parcourir une liste et de trouvée le chiffre le plus grand à chaque passage 
# On ajoutant [1:] on passe directement à la deuxième valeur de la liste pour éviter de comparer le champion avec lui même
for number in numbers[1:]:
    if number > champion:
        champion = number
print ("afficher le nouveau champion :", champion)

# Compter le nombre de valeurs positives dans une liste
numbers = [4, -2, 7, 0, -5, 3]

compteur_chiffre = 0

for number in numbers:
    if number > 0:
        compteur_chiffre += 1
        print("On ajoute 1 au compteur :", compteur_chiffre)

print("Nombre total de valeurs positives :", compteur_chiffre)

# Calculer la somme des valeurs positives dans une liste
numbers = [4, -2, 7, 0, -5, 3]

somme = 0

for number in numbers:
    if number > 0:
        somme += number

print("Somme des valeurs positives :", somme)

# Trouver le plus grand nombre positif dans une liste
numbers = [4, -2, 7, 0, -5, 3]

champion = None

for number in numbers:
    if number > 0:
        if champion is None or number > champion:
            champion = number

if champion is not None:
    print("Le plus grand nombre positif est :", champion)
else:
    print("Aucun nombre positif trouvé.")
    
# Afficher les nombres pairs d'une liste
numbers = [3, 8, 5, 12, 7, 10]

for number in numbers:
    if number % 2 == 0:
        print("Nombre pair :", number)
    		