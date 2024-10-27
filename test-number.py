#On définie une foncion test_number
def test_number(a):
    try:
        #code qui ne fonctionne que si la variable a est un nombre
        float(a)
        #On retourne une réponse positive, a est bien un nombre
        return True
    #Si l'erreur ValueError apparait (et donc que a n'est pas un nombre), on execute le code suivant
    except ValueError:
        #On affiche que a n'est pas un nombre
        print'f"{a} isn't a number")
        #On arrète le programme
        exit()
