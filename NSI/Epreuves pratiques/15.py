# Sujet 15 - 2022

# Exercice 1
def moyenne(tab:list):
    """
    Calcul la moyenne d'une liste
    
    Paramètre:
    tab - list: List dont on va calculer la moyenne

    Retour:
    float: La moyenne de la liste, string "erreur" dans le cas d'une liste vide
    Sans effet de bord
    """
    if len(tab) == 0:
        return "erreur"
    
    somme = 0.0
    for elt in tab:
        somme += elt
    return somme / len(tab)

# Test
print("Exercice 1:")
print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
print(moyenne([]))

# Exercice 2
def tri(tab):
    #i est le premier indice de la zone non triée, j le dernier indice. 
    #Au debut, la zone non triée est le tableau entier.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j-1
    return tab

# Test

print("Exercice 2:")
print(tri([0,1,0,1,0,1,0,1,0]))
# Rajouter
print(tri([0,1,1,1,1,1,0,0,0]))
print(tri([0,0,1,1,0,0,0,0,0]))