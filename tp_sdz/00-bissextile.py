# Invite utilisateur à saisir une année
annee = input("Saisir une année : ");

# TODO prévoir test de saisie

# La valeur récupérée est une String -> transforme en int
annee = int(annee);

# L'année est bissextile si elle est multiple de 4 sans etre 
# multiple de 100 sauf dans le cas où elle est multiple de 400
if (annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)):
    print("Année bissextile")
else:
    print("Année non bissextile")
