def afficher_flottant(n):
    n = str(n).split(".")
    n = ",".join([n[0], n[1][:3]])
    print(n)
    
afficher_flottant(3.123456789)
afficher_flottant(1.5)
afficher_flottant("2.43")
afficher_flottant("3.2.3")
afficher_flottant("A.BCD")
