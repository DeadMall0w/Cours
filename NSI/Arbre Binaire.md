# Définition
Les arbres binaires sont des structures de données non linéaire, ils sont utilisé pour stocker des données sous forme d'arbre ayant entre **0 et 2 branches maximum**.

![[Pasted image 20231127172206.png]]
- Chaque élément de l'arbre est appelé noeud et est relié par une arrête (ex : A,B,C,...P,Q).
- Le noeud **racine** est le noeud initiale (ici c'est A).
- Chaque noeud possède **entre 0 et 2 fils/enfants** (H et I sont les enfants de E)
- Le noeud **parent/pere** est le noeud au au dessus (le parent/pere de G est C)
- Un noeud n'ayant aucun enfant est appelé **'feuille'** (ex D,H,N,O,J,KL,Q)
- À partir d'un noeud on peut définir un sous-arbre gauche et un sous-arbre droit (ex : à partir de C on va trouver un sous-arbre gauche composé des noeuds F, J et K est un sous-arbre droit composé des noeuds G, L, M, P et Q)
- On appelle **arête** le segment qui relie 2 noeuds.
- On appelle **chemin** un ensemble d'arêtes successives qui relient 2 noeuds.  
- On appelle **branche** le chemin le plus court reliant un nœud à la racine.

- La **profondeur d'un nœud** ou d'une feuille dans un arbre binaire le nombre d'arêtes qui composent la branche menant à ce noeud. **Le noeud racine a une profondeur de 0.** Si un noeud est à une profondeur p, tous ses enfants sont à une profondeur p+1. ex : profondeur de B = 1 ; profondeur de I = 3 ; profondeur de P = 4
- On appelle **hauteur** d'un arbre la profondeur maximale des nœuds de l'arbre. Exemple : la profondeur de P = 4, c'est un des noeuds les plus profond, donc la hauteur de l'arbre est de 4.
- On appelle **taille** d'un arbre le nombre de nœuds qui le composent. Exemple : ici la taille de l'arbre est de 17.
- La **taille** d'un arbre binaire de hauteur h est comprise entre **(h+1 pour les arbres filiforme) et** $2^{(h+1)} - 1$ **pour les arbres complets**
- L'**arité** d'un nœud est le nombre de fils du nœud.
- L'**arité d'un arbre** est le nombre maximal de fils des nœuds de l'arbre.
# Types d'arbres
## **Filiforme**  ou **dégénéré**
![[Pasted image 20231127173947.png]]
Tous les noeud possede un unique enfant sauf le dernier (J) qui est une feuille
## **Localement complet** ou **strict** 
![[Pasted image 20231127174137.png]]
Tous les noeuds sont soit des feuilles ou ont 2 enfants. 
## **Complet**
![[Pasted image 20231127174312.png]]
Toutes les feuilles sont au même niveau et même profondeur

## **Equilibré**
![[Pasted image 20231127174137.png]]
Ou 
![[Pasted image 20231127174312.png]]
Les hauteurs du sous arbre gauche et du sous arbre droit du noeud racine (a) sont soit a le même hauteur ou soit a une hauteur différente de 1.

# Algorithmes 

## Définition de l'arbre binaire
L'arbre binaire peut etre définit comme cela, cependant, il peut exister des variantes où le nom des variables diffèrent, ou alors des variantes avec des noeud, ce qui change les algorithmes ci dessous.
```python
class ArbreBinaire:
    def __init__(self,etiquette=None,sag=None, sad=None): #Creer la structure, avec une étiquette (la valeur du noeud (cela peux etre un nombre ou une lettre, voir une chaine de caractere (strin)), son sous arbre gauche et son sous arbre droit qui sont des arbres binaires)
        self.etiquette=etiquette
        self.sag=sag
        self.sad=sad
        
    def est_vide(self): #Renvoie True si l'arbre est vide, sinon False
        if self.etiquette is None:
            return True
        else:
            return False
```
## Taille de l'arbre
Pour calculer la taille d'un arbre binaire, nous pouvons utiliser un algorithme par récurrence

## Implémentation orienté objet :
```python
    def taille(self):
        if self.est_vide():
            return 0
        else:
            return 1 + self.sag.taille() + self.sad.taille()
```


## Hauteur de l'arbre
Pour calculer la hauteur d'un arbre binaire, nous pouvons utiliser un algorithme par récurrence

**ATTENTION, dans la condition d'arrêt il faut return -1, car l'algorithme compte les sous arbres vides**
## Implémentation orienté objet :
```python
def hauteur(self):
	if self.est_vide():
		return -1
	else:
		return 1 + max(self.sag.hauteur(), self.sad.hauteur())
```

# Parcours dans l'arbre
Il existe différent parcours pour parcourir les arbres binaires
- Infixe
- Suffixe / Postfixe
- Préfixe
- Parcours en largeur

Tous les parcours seront appliqué a cette arbre binaire 
![[Pasted image 20231127180344.png]]

## Infixe
```python
def parcoursInfixe(self):
   if not self.etiquette is None:
		x = self
        self.sag.parcoursInfixe()
        print(x.etiquette)
        self.sad.parcoursInfixe()
```
Le parcours de cette arbre donne : C, E, B, D, A, I, G, F, H, J


## Suffixe / postfixe
```python
def parcoursSuffixe(self):
    if not self.etiquette is None:
        x = self
        self.sag.parcoursSuffixe()
        self.sad.parcoursSuffixe()
        print(x.etiquette)
```
Le parcours de cette arbre donne : E, C, D, B, I, G, J, H, F, A

## Préfixe
```python
def parcoursPrefixe(self):
    if not self.etiquette is None:
        x = self
        print(x.etiquette)
        self.sag.parcoursPrefixe()
        self.sad.parcoursPrefixe()
```
Le parcours de cette arbre donne : A, B, C, E, D, F, G, I, H, J

## Parcours en largeur
```python
def parcoursLargeur(self):
    f = File()
    f.enfiler(self)
    while f.est_vide() == False:
        x = f.defiler()
        print(x.etiquette)
        if not x.sag.etiquette is None: 
            f.enfiler(x.sag)
        if not x.sad.etiquette is None: 
            f.enfiler(x.sa)
```
Le parcours de cette arbre donne : A, B, F, C, D, G, H, E, I, J
**/!\\ Ce parcours nécessite l'utilisation de file**  


# Arbre binaire de recherche
 ![[Pasted image 20231127181743.png]]
 ## Critères pour que ca soit un arbre binaire de recherche
 - Doit être un arbre binaire (vu précédemment)
 - Les clés doivent être ordonnable (nombre : croissant, lettre : alphabet)
 - Les clés des sous arbre droites doivent être plus grand que la clé du noeud parent
 - Les clés des sous arbres gauches doivent être plus petite que la clé du noeud parent
## Algorithme de recherche 
```python
def trouver(self, el): #Renvoie true si l'élement est présent et False s'il n'est pas présent dans l'arbre. el = element qu'on recherche dans l'arbre
    if self.etiquette is None:
        return False
    x = self
    if x.etiquette == el:
        return True
    if el < x.etiquette:
        return self.sag.trouver(el)
    else:
        return self.sad.trouver(el)
```
**Les algorithmes de recherche ont un coup logarithmique : n * log(n)**
## Algorithme d'insertion
```python
def inserer(self, cle):
    if self.est_vide():
        return ArbreBinaire(cle, None, None)
    if cle < self.etiquette:
        return ArbreBinaire(self.etiquette, self.sag.inserer(cle), self.sad)
    else:
        return ArbreBinaire(self.etiquette, self.sag, self.sad.inserer(cle))
```

#Cours #NSI
