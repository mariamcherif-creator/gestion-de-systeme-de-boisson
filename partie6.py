class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.7
 
    def description(self):
        return self._boisson.description() + ", Caramel"
 
 
class ChocolatChaud(Boisson):
    def cout(self):
        return 2.5
 
    def description(self):
        return "Chocolat chaud"
 
 
def afficher_commande(boisson):
    print(f"Commande : {boisson.description()}")
    print(f"Prix : {boisson.cout():.1f}€")