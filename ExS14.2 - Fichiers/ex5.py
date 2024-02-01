"""
Exercice 5:
Réparez les problèmes vus dans les exercices précédents.
"""

# EX3
with open("sortie_ex5_3.txt", "w") as f:
    f.write("Ligne 1")
    f.write("Ligne 2")
    f.write("Ligne 3")
    f.write("Ligne 4")


# EX4
lst_lignes = [
    'Ligne 1',
    'Ligne 2',
    'Ligne 3',
    'Ligne 4'
]
with open("sortie_ex5_4.txt", "w") as f:
    f.writelines(lst_lignes)
