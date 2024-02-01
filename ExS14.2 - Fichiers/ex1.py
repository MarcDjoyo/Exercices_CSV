"""
Exercice 1:
Dans cet exercice, vous devez expliquer les différences entre
les différentes fonctions de lecture de texte à partir d'un fichier.
ATTENTION! Ne pas exécuter toutes les lignes d'un coup. Enlever un commentaire à la fois.
"""
with open("zen.txt") as f:
    print(f.read())
    print(f.read(12))
    print(f.readline())
    print(f.readlines())
    print(f.read().splitlines())


"""
Écrire une brève description de chaque fonction ici
f.read():               <Retourne une chaîne contenant tous les 
                         caractères du fichier.>
f.readline():           <Retourne une chaîne de tous les 
                         caractères jusqu’au prochain retour de ligne (\n).>
f.readlines():          <Retourne une liste contenant chacune des lignes du
                         fichier (incluant /n) comme éléments de la liste.>
f.read(12):             <Retourne une chaîne contenant les n prochains 
                         caractères.>
f.read().splitlines():  <Retourne une liste contenant chacune des lignes
                         du fichier (excluant /n) comme éléments de la liste.
>
"""