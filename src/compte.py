import uuid
from abc import ABC


class Compte(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, nomProprietaire: str,numero_compte, **kwargs):
        self.nom_proprietaire = nomProprietaire
        self.solde : int = 0
        self.numero_compte = numero_compte
        self.autorisation_decouvert = 0

    def retrait(self, montant=0, **kwargs):
        if montant <= 0:
            raise Exception("Ca n'est pas possible....")
        else:
            self.solde -= montant  # self.solde = self.solde - montant
        return self.solde

    def versement(self, montant=0, **kwargs) -> int:
        if montant <= 0:
            raise MontantNegatifError("Le montant doit etre positif !")
        self.solde += montant
        return self.solde

    def afficherSolde(self):  # pragma: no cover
        return f"CompteCourant - Solde : {self.solde}"

    def __repr__(self):
        return self.afficherSolde()


class CompteCourant(Compte):
    def __init__(self, nomProprietaire, numero_compte, **kwargs):
        self.pourcentage_agios = 10
        super().__init__(nomProprietaire,numero_compte, **kwargs)
        self.autorisation_decouvert = -1000


    def retrait(self, montant=0, autorisation_decouvert=0, **kwargs):
        self.autorisation_decouvert = autorisation_decouvert
        if self.solde > 0:
            super().retrait(montant)
        elif (self.solde + (self.solde * (self.pourcentage_agios / 100))) > self.autorisation_decouvert:
            raise AutorisationDeDecouvertDepasse
        elif (self.solde <= 0):
            super().retrait(montant)
            self.appliquer_agios(self.solde, self.pourcentage_agios)
        return self.solde

    def versement(self, montant=0, **kwargs) -> int:
        if self.solde >= 0:
            super().versement(montant)
        elif self.solde < 0:
            super().versement(montant)
            self.appliquer_agios(self.solde, self.pourcentage_agios)
        return self.solde

    def appliquer_agios(self, montant, pourcentage_agios):
        # self.solde += montant
        self.solde += (self.solde * (pourcentage_agios / 100))
        return self.solde


class CompteEpargne(Compte):
    def __init__(self, nomProprietaire, numero_compte, **kwargs):
        self.pourcentage_interet = 1.1
        self.autorisation_decouvert = 0
        super().__init__(nomProprietaire, numero_compte, **kwargs)

    def appliquer_interet(self, montant):
        self.solde *= self.pourcentage_interet
        return self.solde

    def versement(self, montant=0, **kwargs) -> int:
        super().versement(montant)
        self.appliquer_interet(montant)
        return self.solde

    def retrait(self, montant=0, **kwargs):
        if (self.solde - montant) < 0:
            raise AutorisationDeDecouvertDepasse("Ce compte ne peux pas etre en négatif")
        else:
            self.solde -= montant
            self.appliquer_interet(montant)
        return self.solde
    def afficherSolde(self):  # pragma: no cover
        super().afficherSolde()
        return f"CompteEpargne - Solde : {self.solde}"
    def __repr__(self):
        super().__repr__()
        return self.afficherSolde()


class MontantNegatifError(Exception):
    pass


class MontantTropEleveError(Exception):
    pass


class AutorisationDeDecouvertDepasse(Exception):
    pass
