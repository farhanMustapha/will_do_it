class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age



class Student(Personne):
    def __init__(self,nom,age,filiere):
        super().__init__(nom, age)
        self.filiere=filiere

stud=Student("ahmed",30,"math")
print(stud.filiere)
print(stud.age)
print(stud.nom)

