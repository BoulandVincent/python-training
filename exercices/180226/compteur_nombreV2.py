numbers = [4, 2, 7, 4, 3, 2, 4]
compteur = {}

for number in numbers:
    if number in compteur:
        compteur[number] += 1
    else: 
        compteur[number] = 1

for key in compteur:
   print(f"le nombre {key} a été retrouvée {compteur[key]} fois")

