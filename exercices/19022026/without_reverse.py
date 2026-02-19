numbers = [1, 2, 3, 4]

reversed_list = []
	
for i in range (len(numbers)-1,-1,-1):
	#print("indice :",i,"valeur:",numbers[i]) 
	reversed_list.append(numbers[i])
	print("reversed_list :",reversed_list)