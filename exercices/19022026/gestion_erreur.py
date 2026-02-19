while True :
    user_input = input ("Entrez un chiffre: ")

    try:
        number = int(user_input)
        if number >= 0:
            print (f"Le chiffre que vous avez entré est : {number} ce qui est positif")
            break
        else :
            print(f"Le chiffre que vous avez entrée est : {number} ce qui est négatif")

    except ValueError:

        print("Verifiez que vous avez bien entrée un chiffre au lieux d'une lettre ou d'un symbole")
