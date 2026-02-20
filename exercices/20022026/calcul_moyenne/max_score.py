def find_max_score(scores):
    if len(scores) == 0:
        raise ValueError("Le calcul du score maximum ne peut pas être effectué : la liste de scores est vide.")
    meilleur_score = scores[0]
    for score in scores[1:]:
        if score > meilleur_score:
            meilleur_score = score
    return meilleur_score
