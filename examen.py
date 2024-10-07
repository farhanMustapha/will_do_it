class Reponse:
    def __init__(self,journal,compte,montant):
        self.journal=journal
        self.compte=compte
        self.montant=montant

rep1=Reponse("achat",["4411","6111"],["6000","6000"])

class Examen:
    def __init__(self,question,reponse):
        self.question=question
        self.reponse=reponse


ex=Examen("achat de m/ses",rep1)

print(ex.reponse.journal)