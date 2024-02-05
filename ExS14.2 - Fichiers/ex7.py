"""
Exercice 7:
Modifiez le programme de l'exercice 6 afin de permettre d'écrire plusieurs lignes.
Pour se faire, vous devrez demander des lignes jusqu'à ce que le texte soit égal à EOF.
Vous devez également utiliser une liste pour stocker chaque ligne de texte.
Finalement, affichez le contenu du fichier à l'utilisateur clairement.
"""

def ecrire_lignes():
    """
    Demander le texte à écrire dans le fichier
    :return: La liste dans laquelle est inscrit le texte
    """
    list = []
    while True:
        texte = input("Entrez le texte à écrire dans le fichier : ")
        while True:
            list.append(texte)
            break
        # Écrire dans le fichier
        with open(nom_fichier, "w") as fichier:
            for e in list:
                fichier.write(e + "\n")
        if texte == "EOF":
            break
def lire_fichier():
    """
    Lire le contenu du fichier et l'afficher
    :return: Le texte provenant du fichier
    """
    with open(nom_fichier, "r") as fichier:
        ecrire_lignes()
        contenu = fichier.read()
        print(f"Le texte provenant du fichier {nom_fichier} est :\n{contenu}")


if __name__ == "__main__":
    # Demander le nom du fichier à utiliser
    caracteres = "<, >, :, “, /, \, |, ?, *"
    while True:
        nom_fichier = input("Entrez le nom du fichier : ")
        if any(c in caracteres for c in nom_fichier):
            print("Veuillez entrer un nom de fichier valide... \n"
                  "Caractères non_acceptés: <, >, :, “, /, \, |, ?, *")
            continue
        else:
            lire_fichier()
            break