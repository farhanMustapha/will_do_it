import livre as lv
import bibliotheque as bb


livre1 = lv.Livre("1984", "George Orwell", 1949, "Dystopie")
livre2 = lv.Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "Fiction")
livre3 = lv.Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997, "Fantaisie")

biblio=bb.Bibliotheque()
biblio.ajouter_livre(livre1) #livre = livre1
biblio.ajouter_livre(livre2) #livre = livre2
biblio.ajouter_livre(livre3) #livre = livre3

print("afficher tout les livres :")
biblio.afficher_livres()
print("-" * 30)

print("Recherche du livre '1984' :")
livre_recherche=biblio.rechercher_livre_par_titre("1984")
if livre_recherche:
    livre_recherche.afficher_details()

print("Suppression du livre '1984' :")
biblio.supprimer_livre_par_titre("1984")

print("Tous les livres après suppression :")
biblio.afficher_livres()




