"""
ex1
nom=input("tapez votre nom : ")
print(f"welcoom Mr/Mme : {nom} you are the best")

ex2
a=int(input("a :")) #input return tjr str cad chaine de caractere
b=int(input("b :")) #input return tjr str cad chaine de caractere
print(f"la somme de a et b :{a+b}")

ex3


a=int(input("a :")) #input return tjr str cad chaine de caractere
b=int(input("b :")) #input return tjr str cad chaine de caractere
if a > b :
    print(f" a est le max")
else:
    print(f"b est le max")

    ex4

for i in range(1,101):
    print(i)


n=int(input("tapez un nombre :"))
if n%2==0:
    print(f"{n} est pair")
else:
    print(f"{n} est impair")



age=int(input("tapez ton age  :"))
if age>18:
    print("vous etes majeur")
else:
    print("vous etes mineur")


x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
    print("x est le mx")
elif y>x and y>z:
    print("y est le max")
elif z>x and z>y:
    print("z est le max")

    ex 7

x=int(input())
y=int(input())
z=int(input())
def maximum(x,y,z):
    max=0
    if x>y :
        max=x
    else:
        max=y
    if max<z:
         max=z
    print(f" le max est {max}")
maximum(x,y,z)



n=int(input("tapez n :"))
s=0
for i in range(1,n+1):
    s=s+i
print(s)



n=int(input("tapez n :"))
s=1
for i in range(1,n+1):
    s=s*i
print(s)


pi=3.14
r=float(input("tapez le reayon cercle  :"))
s=pi*(r**2)
print("la surface est :",s)
p=2*pi*r
print("le perimetre est ",p)


a=int(input("tapez un entier :"))
for i in range(1,a+1):
    if a%i==0:
        print(f"{i} : est un diviseur de a ")



a=int(input("tapez n : "))
for i in range(0,11):
    print(f" la multiplication de {a} par {i} est : {a*i}")

    

for n in range(1,10):
    for i in range(0,10):
        print(f"table multiplication de {n}")
        print(f"la multi de {n} par {i} est : {n*i}")
        print("-"*30)

        
a=int(input("taper a :"))
b=int(input("taper b :"))
c=int(a/b)
print(c)



a=int(input("tapez a : "))
b=int(input("tapez b : "))
rslt=a//b # int(a/b) le resultat de la division 
rest=a%b   # a-(rslt*b): le reste de la division
print(f"le resultat de a/b est {rslt} ,le rest est {rest}")


ex 14
n=int(input('verifier carre parfait : '))
for i in range(1,n+1):
    if i*i==n:
        print(f" {n} est un carre parfait de {i}")
        break
else:
    print(f" {n} n'est pas un carree parfait")



n=int(input('verifier carre parfait : '))
for i in range(1,n+1):
    if i**2==n:
        print(f" {n} est un carre parfait de {i}")
        break
else:
    print(f" {n} n'est pas un carree parfait")

ex 15

n=int(input('tapez un nbr : '))
counter=0
for i in range(1,n+1):
    if n%i==0:
        counter=counter+1
if counter==2:
    print("n est premier")
else:
    print(" n'est pas premier ")

    ex 16
txt=input("tapez un text")
for c in txt:
    print(c)

    ex 18
txt=input("tapez un text : ")
c="e"
for i in range(0,len(txt)):
    if txt[i]==c:
        print(f" {c} exist in position {i}")
        break
else:
    print("la lettre n'existe pas ")
    

     ex 19   
lst=["laptop","iphoggne","tabhhhhhhhlet"]
for x in lst:
    print(f"la langueur de < {x} > est : {len(x)}")

    
#dans block try nous avon met une condition si true generer une erreur automatiquement executer except 
#si la condition est false donc executer le code de else 
try:  
    age=int(input("saisir ton age : "))
    if age<18:    #si cette condition est true executer le code de except car il s'agit d'un erreur
        raise ValueError
    else:         # si la condition est false executer ce code 
        print("age is valide")
except:
    print('age non valide ')



name="mustapha"
x=len(name)-1
first_lettre=name[0]
last_lettre=name[x]

name1=name[1:x]
name2=last_lettre+name1+first_lettre
print(name2)

"""


""" 
import os 
user=os.getlogin()
print(user)
 """

""" 
import os 
from pathlib import Path

def creatFolder(folder_name):
    rep_act=os.getcwd() # permet de stocker le chemein du dossier actuel
    path=f"C:/Users/AdMin/Desktop/pythonProject/oop/{folder_name}"
    if not os.path.exists(path):
        try:  
            os.mkdir(path)
            print(f"folder created with name {folder_name}")
        except OSError as e:
            print(f"os err {e}") 
            
    
    else:
        print('folder exist')
        print(f"le chemin actuel est  : {rep_act}") 

xx=input("nom du dossier : ")
creatFolder(xx)  
"""
taches = []


# Fonction pour créer une tâche
def create_taches(titre, date_tache, quantite):
    # Créer un dictionnaire avec les informations de la tâche
    dic_taches = {
        "titre": titre,
        "detail": {
            "date": date_tache,
            "quantite": quantite
        }
    }
    return dic_taches

# Ajouter la tâche à la liste `taches`

for i in range(1,4):
    # Demande d'entrée de l'utilisateur pour le titre, la date et la quantité
    titre = input("Le titre de la tâche : ")
    date_tache = input("La date de la tâche : ")
    quantite = input("La quantité : ")
        
    # Créer une tâche en utilisant les informations fournies par l'utilisateur
    a = create_taches(titre, date_tache, quantite)
    taches.append(a)


# Afficher la liste des tâches
print(taches)


 




