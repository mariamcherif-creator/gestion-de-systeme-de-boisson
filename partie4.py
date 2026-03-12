class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self._b1 = b1
        self._b2 = b2
 
    def cout(self):
        return self._b1.cout() + self._b2.cout()
 
    def description(self):
        return self._b1.description() + " + " + self._b2.description()
 
 
Boisson.__add__ = lambda self, other: BoissonCombinee(self, other)