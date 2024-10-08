import json

# Charger le contenu du fichier JSON
with open('fichier1.json', 'r') as f:
    contenu = json.load(f)

# Demander l'email et le mot de passe
pw = input("pass: ")
eml = input("email : ")

# Initialiser un indicateur pour vérifier si l'utilisateur existe
user_exists = False

# Parcourir toutes les entrées dans le JSON
for c in contenu:
    if pw == c['pass'] and eml == c['email']:
        user_exists = True
        break

# Afficher le résultat
if user_exists:
    print("exist")
else:
    print("your pass or email is incorrecte")
