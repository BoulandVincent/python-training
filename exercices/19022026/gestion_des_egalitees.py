numbers = [4, 2, 7, 4, 3, 2, 4]

occurrence = {}

max_count = 0
champion = []

#La première boucle vérifie si le nombre est déjà présente dans l'occurrence ou non
for number in numbers:
	if number in occurrence:
		occurrence[number] +=1 
	else: 
	     occurrence[number]=1
	 
for number,count in occurrence.items():
	if count > max_count:
		max_count = count
		champion = []
		champion.append(number) 
	elif count == max_count: 
		champion.append(number)
print("Le(s) nombre(s) le(s) plus fréquent(s) est/sont : ", champion, " avec ", max_count, " occurrences.")