from multipledispatch import dispatch

class Calcul:
    def __init__(self):
        pass
    @dispatch(int,int)
    def somme(self,x,y):
        return x+y

    @dispatch(int,int,int)
    def somme(self,x,y,z):
        return x+y+z

c=Calcul()
print(c.somme(8,2))