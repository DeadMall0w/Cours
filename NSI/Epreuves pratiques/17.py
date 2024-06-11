# Sujet 17 - 2022

# Exercice 1
def nombre_de_mots(phrase:str)->int:
    """
    Trouve le nombre de mots dans une phrase
    
    Paramètre:
    phrase - str: la phrase où on compte les mots

    Retour:
    int: nombre de mots présent dans la phrase
    Sans effet de bord
    """
    return len(phrase.split(" "))-1

# Test
print("Exercice 1:")
print(nombre_de_mots('Le point d exclamation est sépare !'))
print(nombre_de_mots('Il y a un seul espace entre les mots !'))
# Exercice 2
    