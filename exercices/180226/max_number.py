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