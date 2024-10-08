import json

# Charger le premier fichier JSON qui contient les descriptions
try:
    with open('fichier1.json', 'r') as file1:
        comptes_desc = json.load(file1)
except json.JSONDecodeError as e:
    print(f"Erreur de lecture du fichier1.json : {e}")
    comptes_desc = []

# Charger le deuxième fichier JSON où nous voulons ajouter les descriptions
try:
    with open('fichier2.json', 'r') as file2:
        comptes = json.load(file2)
except json.JSONDecodeError as e:
    print(f"Erreur de lecture du fichier2.json : {e}")
    comptes = []

# Vérifier les contenus des fichiers chargés
print("Contenu du premier fichier (fichier1.json) :")
print(comptes_desc)

print("\nContenu du deuxième fichier (fichier2.json) :")
print(comptes)

# Créer un dictionnaire pour un accès rapide par numéro de compte
descriptions_dict = {compte['accountNumber']: compte.get('description', '') for compte in comptes_desc}

# Ajouter la description au deuxième fichier
for compte in comptes:
    numero_compte = compte.get('accountNumber')
    if numero_compte in descriptions_dict:
        compte['description'] = descriptions_dict[numero_compte]
    else:
        print(f"Aucune description trouvée pour le compte {numero_compte}")

# Sauvegarder le fichier JSON mis à jour
try:
    with open('fichier2_mis_a_jour.json', 'w') as file2_updated:
        json.dump(comptes, file2_updated, indent=4)
    print("\nDescriptions ajoutées avec succès.")
except IOError as e:
    print(f"Erreur lors de la sauvegarde du fichier mis à jour : {e}")
