class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booléen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """Place l’élément v au sommet de la pile."""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


# Exos 2, sujet 8
"""
On considère la fonction insere ci-dessous qui prend en argument un entier a et un
tableau tab d'entiers triés par ordre croissant. Cette fonction insère la valeur a dans le
tableau et renvoie le nouveau tableau. Les tableaux seront représentés sous la forme de
listes python.
"""
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2 # le moins 2 est car : -1 cart le dernière element de la liste est len(l)-1, et -1 pour éviter de boucler sur l'element qu'on vient de rajouter
    while a < tab[i] and i >= 0: 
        l[i+1] = l[i]
        l[i] = a
        i = i -1
    return l



# Exercice 2, sujet 12
"""
On considère un tableau d'entiers tab (type list dont les éléments sont des 0 ou des
1). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri,
le tableau est constitué de trois zones consécutives, la première ne contenant que des 0,
la seconde n'étant pas triée et la dernière ne contenant que des 1.
Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
élément :
- si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant
que des 0 ;
- si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on
considère alors qu’il appartient à la zone ne contenant que des 1.
Dans tous les cas, la longueur de la zone non triée diminue de 1.
"""
def tri(tab):
    #i est le premier indice de la zone non triée, j le dernier indice. 
    #Au debut, la zone non triée est le tableau entier.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i] == 0:
            i= i+1
        else :
            valeur = tab[j] # Ici il y a un échange de valeur 
            tab[j] = tab[i]
            tab[i] = valeur
            j= j-1
    return tab



# Exercice 2, sujet 15
"""
Voici une fonction python basée sur la méthode des divisions successives permettant de
convertir un nombre entier positif en binaire
"""
def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a



# Triangle de pascal
def pascal(n):
    C= [[1]]
    for k in range(1,n):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

# Dichotomie
def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

# Dichotomie version récursive
def chercher(T,n,i,j):
     if i < 0 or  j > len(T):
         print("Erreur")
         return 19
     if i > j :
         return 20
     m = (i+j) // 2
     if T[m] < n:
         return chercher(T, n, m+1 , j )
     elif T[m] > n :
        return chercher(T, n,  i, m-1)
     else :
         return m


# Notation polonaise inversé, NPI
def npi(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == "+":
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()



def multiplication(n1:int,n2:int)->int:
    """
    Fonction qui multiplie 2 nombres ensembles sans utiliser de multiplication
    
    Paramètre:
    n1 (int) : Premier nombre à multiplier
    n2 (int) : Deuxième nombre à multiplier
    
    Retour :
    int: la multiplication de n1 x n2
    Sans effet de bord

    """
    r = 0 # Variable qui stocke le résultat
    
    # Vérification nécessaire dans le cas de nombre négatif
    nb_negatif = 0 # Variable qui stocke le nombre de nombre négatif, si ce nombre est pair, le résultat sera positif, sinon il sera négatif
    if n1 < 0:
        nb_negatif += 1
    if n2 < 0:
        nb_negatif += 1
    
    for i in range(abs(n1)):
        r += abs(n2)
    if nb_negatif % 2 == 0:
        return r
    return -r


## Exercice 2
"""
Je ne retrouve pas la consigne,
La fonction depouille, permet de faire un dictionnaire avec comme clé le nom de l'artiste 
et en valeur le nombre d’occurrence dans la liste
La fonction vainqueur permet a l'aide de la fonction depouille de trouver quels sont les personnes ayant obtenue le plus d’occurrence, 
renvoie une liste si plusieurs personnes ont le meme nombre d’occurrence.
"""
Urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales', 'Extra Vomit','Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
        liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale