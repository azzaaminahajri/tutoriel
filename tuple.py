import csv

# Chemin vers le fichier CSV
data = ('C:/Users/Hp/Desktop/nychousing.csv')
# Créer une liste pour stocker le contenu du fichier CSV sous forme de tuple
contenu_csv = []

# Parcourir le fichier CSV et lire son contenu
with open(data, newline='') as csvfile:
    lecteur_csv = csv.reader(csvfile)
    for index, ligne in enumerate(lecteur_csv):
        # Convertir chaque élément de la ligne en tuple
        tuple_ligne = tuple(ligne)
        # Ajouter le tuple de ligne à la liste avec son numéro d'index
        contenu_csv.append((index, tuple_ligne))

# Afficher le contenu du tuple avec la fonction enumerate
for index, ligne in contenu_csv:
    print(f"Index {index}: {ligne}")

