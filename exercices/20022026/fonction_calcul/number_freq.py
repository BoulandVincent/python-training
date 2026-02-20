from compteur_occurrences import compteur_occurences
from freq_number import number_freq

numbers = [4, 2, 7, 4, 3, 2, 4]

compteur = compteur_occurences(numbers)

champion_number, champion_count = number_freq(compteur)

print(f"Le nombre le plus fréquent est {champion_number} avec {champion_count} occurrences")