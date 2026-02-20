def compteur_occurences(numbers):
	compteur = {}

	for number in numbers: 
		if number not in compteur:
			compteur[number] = 1
		else:
			compteur[number] +=1

	return(compteur)



