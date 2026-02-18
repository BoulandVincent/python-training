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