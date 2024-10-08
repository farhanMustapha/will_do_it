

class Surface:

    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculerSurface(self):
        s=self.longueur*self.largeur
        return s

c=Surface(10,30)
print(c.calculerSurface())
