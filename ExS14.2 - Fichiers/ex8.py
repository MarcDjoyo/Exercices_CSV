def ecrire_lignes():
    """
    Demander le texte à écrire dans le fichier
    :return: La liste dans laquelle est inscrit le texte
    """
    list = []

    while True:
        texte = input("Entrez le texte à ajouter dans le fichier (tapez 'EOF' pour terminer) : ")

        if texte == "EOF":
            break

        list.append(texte)

    # Écrire dans le fichier
    with open(nom_fichier, "a") as fichier:
        for e in list:
            fichier.write(e + "\n")

def lire_fichier():
    """
    Lire le contenu du fichier et l'afficher
    :return: Le texte provenant du fichier
    """
    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
        print(f"Le contenu actuel du fichier {nom_fichier} est :\n{contenu}")

if __name__ == "__main__":
    # Demander le nom du fichier à utiliser
    caracteres_non_acceptes = "<, >, :, “, /, \, |, ?, *"

    while True:
        nom_fichier = input("Entrez le nom du fichier : ")

        if any(c in caracteres_non_acceptes for c in nom_fichier):
            print("Veuillez entrer un nom de fichier valide... \n"
                  "Caractères non acceptés: <, >, :, “, /, \, |, ?, *")
            continue
        else:
            # Appeler la fonction pour écrire dans le fichier
            ecrire_lignes()

            # Appeler la fonction pour lire et afficher le contenu du fichier
            lire_fichier()
            break