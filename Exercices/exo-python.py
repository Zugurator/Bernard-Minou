try:
    age1 = int(input("Quel est l'âge de la première personne ?"))
    age2 = int(input("Quel est l'âge de la deuxième ?"))
    diffence_age = abs(age1 - age2)
    print(f"La différence d'âge entre les deux est de {diffence_age} an(s)")
except ValueError :
    print("Genre ton âge c'est des lettres, fait pas le malin Colin, je t'ai à l'oeil.")

from datetime import datetime
try :
    anneen = int(input("Quel est ton année de naissance bro ?"))
    anneea = datetime.now().year
    age3 = abs( anneea - anneen )
    print(f"T'es vla vieux wesh, t'a {age3} ans")
except ValueError :
    print("Gros mytho va")