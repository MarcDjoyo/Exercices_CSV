"""
Exercice 6:
Écrivez un programme pour écrire dans un fichier. Votre programme doit demander
le nom du fichier à utiliser et demander le texte à écrire. Une fois terminé,
votre programme doit afficher un message montrant clairement le texte provenant du fichier.
"""
# Demander le nom du fichier à utiliser
nom_fichier = input("Entrez le nom du fichier : ")

# Demander le texte à écrire dans le fichier
texte = input("Entrez le texte à écrire dans le fichier : ")

# Écrire dans le fichier
with open(nom_fichier, "w") as fichier:
    fichier.write(texte)

# Lire le contenu du fichier et l'afficher
with open(nom_fichier, "r") as fichier:
    contenu = fichier.read()
    print(f"Le texte provenant du fichier {nom_fichier} est :\n{contenu}")



