totale = 0 

while True: 
    user_input = input ("Entrez un chiffre:").strip()
    if user_input == ("stop").strip().upper():
        print(f"le totale est de : {totale}")
        break 
    try:
        number = int(user_input)
        totale+= number
    except ValueError:
        print("Vérifiez que la valeur que vous avez entrée est un chiffre au lieu d'un caractère ou d'un symbole")
