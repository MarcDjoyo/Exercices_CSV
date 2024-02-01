"""
Exercice 7:
Modifiez le programme de l'exercice 6 afin de permettre d'écrire plusieurs lignes.
Pour se faire, vous devrez demander des lignes jusqu'à ce que le texte soit égal à EOF.
Vous devez également utiliser une liste pour stocker chaque ligne de texte.
Finalement, affichez le contenu du fichier à l'utilisateur clairement.
"""
import os

def entrer_texte(nom_fichier):
    """
    Entrer le texte qui sera écrit dans le fichier
    :param nom_fichier: Nom du fichier
    :return: Liste des lignes de texte
    """
    lignes = []
    print("Entrez les lignes de texte. Tapez 'EOF' sur une ligne vide pour terminer.")

    while True:
        ligne = input("Entrez votre texte: ")
        if ligne.lower() == 'eof':
            break
        lignes.append(ligne)

    # Écrire dans le fichier
    with open(nom_fichier, "w") as fichier:
        for ligne in lignes:
            fichier.write(ligne + '\n')  # Ajouter un retour à la ligne entre chaque ligne

    return lignes


def afficher_contenu(nom_fichier):
    """
    Affiche le contenu du fichier s'il existe
    :param nom_fichier: Nom du fichier
    :return: None
    """
    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
        print(f"Le texte provenant du fichier {nom_fichier} est :\n{contenu}")



# Demander le nom du fichier à utiliser
caract_non_acceptes = [",", ">", ":", '"', "/", "\\", "|", "?", "*"]
try:
    while True:
        nom_fichier = input("Entrez le nom du fichier : ")
        if any(c in caract_non_acceptes for c in nom_fichier):
            print(f"Veuillez entrer un nom de fichier valide...\nCaractères non acceptés: , >, :, \", /, \\, |, ?, *")
        else:
            break
except OSError:
    print("Le nom de fichier entré n'est pas valide...")

# Appeler la fonction pour entrer le texte
lignes_enregistrees = entrer_texte(nom_fichier)

# Appeler la fonction pour afficher le contenu du fichier
afficher_contenu(nom_fichier)

