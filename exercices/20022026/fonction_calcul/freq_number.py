def number_freq(compteur) :
	champion_number = None
	champion_count = 0 
	for key in compteur: 
		if compteur[key] > champion_count: 
			champion_number = key
			champion_count = compteur[key]
	
	return (champion_number, champion_count)
		
		