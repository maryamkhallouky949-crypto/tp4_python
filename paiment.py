
from abc import ABC, abstractmethod



class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if not self.verifier_luhn(numero):
            raise ValueError("Numéro de carte invalide.")

        if not (cvv.isdigit() and len(cvv) == 3):
            raise ValueError("CVV invalide.")

        self._numero = numero
        self._cvv = cvv

    @staticmethod
    def verifier_luhn(numero):
        if not numero.isdigit():
            return False

        chiffres = [int(c) for c in numero]
        somme = 0

        for i, chiffre in enumerate(reversed(chiffres)):
            if i % 2 == 1:
                chiffre *= 2
                if chiffre > 9:
                    chiffre -= 9

            somme += chiffre

        return somme % 10 == 0

    def payer(self):
        return (
            f"Paiement par Carte Bancaire réussi : "
            f"{self._montant} €"
        )

class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)

        if "@" not in email or "." not in email:
            raise ValueError("Adresse email invalide.")

        if not token:
            raise ValueError("Token API obligatoire.")

        self._email = email
        self._token = token

    def payer(self):
        return (
            f"Paiement par PayPal réussi : "
            f"{self._montant} €"
        )

class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)

        if not wallet_id:
            raise ValueError("Identifiant wallet obligatoire.")

        reseaux_valides = ["BTC", "ETH", "BNB"]

        if reseau not in reseaux_valides:
            raise ValueError("Réseau crypto non reconnu.")

        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        return (
            f"Paiement par Crypto ({self._reseau}) réussi : "
            f"{self._montant} €"
        )



def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())

if __name__ == "__main__":

    paiements = [

        CarteBancaire(200, "4532016112830366", "123"),
        CarteBancaire(350, "601107799013924", "456"),

        PayPal(150, "maryam@gmail.com", "TOKEN113"),
        PayPal(250, "dounya@gmail.com", "TOKEN466"),

        Crypto(300, "WALLET001", "BTC"),
        Crypto(500, "WALLET002", "ETH")
    ]

    traiter_paiements(paiements)
