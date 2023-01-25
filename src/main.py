from src.compte import CompteCourant, CompteEpargne

nomutilisateur : str
numerodecompte : str
solde : int = 0
choixcompte : str
autreoperation : str = "1"
choixoperation : str
saisimontant: str
montant : int
affichersolde : int
solde : int

print("Bonjour \nVeuillez rentrer votre nom :")
nomutilisateur = input()
print("Entrez votre numéros de compte :")
numerodecompte = input()
print("Voulez vous gérer votre compte épargne ou compte courant?\nTapez 1 pour courant 0 pour épargne ")
choixcompte = input()
while choixcompte != "1" and choixcompte != "0":
    print("Valeur invalide, rentrez en une compris entre 1 pour une compte courant\n et 0 pour un compte épargne")
    choixcompte = input()

if choixcompte == "1":
    comptecourant = CompteCourant(nomutilisateur,numerodecompte)
    print(comptecourant.__repr__(), "\n")
    while autreoperation == "1":
        #print(comptecourant.__repr__(),"\n")
        print("Tapez 1 pour un versement où 0 pour un retrait :\n")
        choixoperation = input()
        while choixoperation != "1" and choixoperation !="0":
            print("Valeur invalide,Tapez 1 pour un versement où 0 pour un retrait :\n")
            choixoperation = input()
        if choixoperation == "1":
            print("Entrez le montant du versement:\n")
            saisimontant = input()
            montant = int(saisimontant)
            comptecourant.solde = comptecourant.versement(montant)
        elif choixoperation =="0":
            print("Entrez le montant du retrait:\n")
            saisimontant = input()
            montant = int(saisimontant)
            comptecourant.solde = comptecourant.retrait(montant)
        print(comptecourant.__repr__(), "\n")
        print("Souhaitez vous faire une autre opération?\nTapez sur 1 pour effectuer une autre opération et 0 pour arreter\n")
        autreoperation = input()
        while autreoperation !="0" and autreoperation != "1":
            print("Valeur invalide,Tapez sur 1 pour effectuer une autre opération sur ce compte et 0 pour arreter\n")
            autreoperation = input()
else:
    compteepargne = CompteEpargne(nomutilisateur,numerodecompte)
    print(compteepargne.__repr__(), "\n")
    while autreoperation =="1":
        print("Tapez 1 pour un versement où 0 pour un retrait :\n")
        choixoperation = input()
        while choixoperation != "1" and choixoperation != "0":
            print("Valeur invalide,Tapez 1 pour un versement où 0 pour un retrait :\n")
            choixoperation = input()
        if choixoperation == "1":
            print("Entrez le montant du versement:\n")
            saisimontant = input()
            montant = int(saisimontant)
            compteepargne.solde = compteepargne.versement(montant)
        elif choixoperation == "0":
            print("Entrez le montant du retrait:\n")
            saisimontant = input()
            montant = int(saisimontant)
            compteepargne.solde = compteepargne.retrait(montant)
        print(compteepargne.__repr__(), "\n")
        print("Souhaitez vous faire une autre opération?\nTapez sur 1 pour effectuer une autre opération et 0 pour arreter\n")
        autreoperation = input()
        while autreoperation != "0" and autreoperation != "1":
            print("Valeur invalide,Tapez sur 1 pour effectuer une autre opération sur ce compte et 0 pour arreter\n")
            autreoperation = input()
print("Au revoir\n", nomutilisateur)







