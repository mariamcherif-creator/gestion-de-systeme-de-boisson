# 1 Classe de base Commande
class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []
 
    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)
 
    def prix_total(self):
        return sum(b.cout() for b in self.boissons)
 
    def afficher(self):
        descriptions = ", ".join(b.description() for b in self.boissons)
        print(f"Commande de {self.client.nom} :")
        print(f"  Boissons : {descriptions}")
        print(f"  Prix total : {self.prix_total():.2f}€")
 
 
# 2 Types de commandes
class CommandeSurPlace(Commande):
    def afficher(self):
        print("[ Sur place ]")
        super().afficher()
 
 
class CommandeEmporter(Commande):
    def afficher(self):
        print("[ À emporter ]")
        super().afficher()
 
 
# 3 Programme de fidélité
class Fidelite:
    def ajouter_points(self, client, montant):
        points = int(montant)
        client.points_fidelite += points
        print(f"  +{points} points → total : {client.points_fidelite} pts")
 
 
# 4 Héritage multiple
class CommandeFidele(Commande, Fidelite):
    def valider(self):
        print(f"\nValidation de la commande de {self.client.nom} :")
        self.ajouter_points(self.client, self.prix_total())