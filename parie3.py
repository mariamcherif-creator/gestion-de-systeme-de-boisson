class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson
 
 
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
 
    def description(self):
        return self._boisson.description() + ", Lait"
 
 
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2
 
    def description(self):
        return self._boisson.description() + ", Sucre"
 