def calculate_mean(notes):
    if len(notes) == 0:
        raise ValueError("Impossible de calculer une moyenne : la liste de notes est vide.")

    total = 0 

    for note in notes:
        total += note 
    mean = total /len(notes)
    return mean  