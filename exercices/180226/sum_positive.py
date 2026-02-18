# Calculer la somme des valeurs positives dans une liste
numbers = [4, -2, 7, 0, -5, 3]

somme = 0

for number in numbers:
    if number > 0:
        somme += number

print("Somme des valeurs positives :", somme)
