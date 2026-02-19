numbers = [4, 2, 4, 3, 2, 1]

unique_numbers= []
for number in numbers: 
    if number not in unique_numbers:
        unique_numbers.append(number)
        print(f"Le nombre {number} à été ajouté a la liste unique_numbers")
print(unique_numbers)
        