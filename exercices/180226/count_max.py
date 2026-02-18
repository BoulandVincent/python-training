numbers = [4, 2, 7, 4, 3, 2, 4]
champion_number =None 
champion_count = 0
compteur = {}

for number in numbers:
    if number in compteur:
        compteur[number] += 1
    else:
        compteur[number] = 1
    if compteur[number] > champion_count:
        champion_number = number
        champion_count = compteur[number]


for key in compteur:
   print(f"le nombre {key} a été retrouvée {compteur[key]} fois")
print(f"le nombre {champion_number} est le plus fréquent avec {champion_count} occurrences")