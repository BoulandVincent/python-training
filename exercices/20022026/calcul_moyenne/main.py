from max_score import find_max_score
from mean_score import calculate_mean

notes = [12, 15, 9, 17]

mean = calculate_mean(notes)
max_score = find_max_score(notes)
print(f"La moyenne des notes est : {mean}")
print(f"Le score maximum est : {max_score}")
