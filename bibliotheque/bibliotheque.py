       
class Bibliotheque:
    def __init__(self):
        self.livres=[]

    def ajouter_livre(self,livre):
        self.livres.append(livre)

    
    def supprimer_livre_par_titre(self,titre):
        livre_a_supprimer=self.rechercher_livre_par_titre(titre)
        if livre_a_supprimer:
            self.livres.remove(livre_a_supprimer)

#afficher les livres qui existe dans la bibliotheque 
    def afficher_livres(self):
        for livre in self.livres:
            livre.afficher_details()

#rechercher un livre dans la bibliotheque par son titre 
    def rechercher_livre_par_titre(self,titre):
        for livre in self.livres:
            if livre.titre==titre:
                return livre
        return None
    
