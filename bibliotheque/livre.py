class Livre:
    
    def __init__(self,titre,auteur,annee_publication,genre):
        self.titre=titre
        self.auteur=auteur
        self.annee_publication=annee_publication
        self.genre=genre
        

    def afficher_details(self):
        print("-" * 30)
        print(f"titre :{self.titre}")
        print(f"auteur :{self.auteur}")
        print(f"anne publication :{self.annee_publication}")
        print(f"genre :{self.genre}")
        

 
