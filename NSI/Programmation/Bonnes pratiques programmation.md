La lisibilité d'un programme informatique est cruciale pour faciliter sa compréhension, sa maintenance et sa collaboration entre développeurs. En NSI, il est important d'adopter des bonnes pratiques de programmation pour rendre les programmes plus lisibles et plus compréhensibles.

> [!note]
> 
> Pour le reste de toute cette note, les commetaires, noms de variable, ect... sont écrites en français, cependant il est mieux vu d'écrire en anglais, car c'est dans ce langage que la plupart du code est écrit

# Docstring
Les docstrings sont des chaînes de documentation intégrées dans le code source d'un programme (en commentaire [[Faire un commentaire en python]] )pour décrire son fonctionnement, ses entrées, ses sorties et son comportement. Voici un exemple de docstring en Python :

```python
def addition(a, b):
    """
    Cette fonction effectue une addition de deux nombres.
    
    Paramètres :
    a (int) : Le premier nombre à additionner.
    b (int) : Le deuxième nombre à additionner.
    
    Retour :
    int : La somme des deux nombres.
    """
    return a + b
```

# Indication type de variable

### Introduction
Indiquer explicitement les [[types de variables]] dans le code source peut aider à clarifier le fonctionnement du programme et à réduire les erreurs. De nombreux langages de programmation modernes, comme Python avec l'ajout des annotations de type, permettent de spécifier les types de variables dans le code source.
### Utilisation
Après avoir définit une variable, on rajoute le type de la variable précédé par ":" Ex:

```python
nom_variable: type = valeur
```

Il existe aussi la meme chose pour le type de variable retourné par la fonction, pour cela il faut, après avoir fermé la paranthèse, contenant les [[Parametres de la fonction]] le type, précédé par "- >", et finir les ":" comme habituellement. 

### Exemple

```python
def addition(a: int, b: int) -> int:
    return a + b
```

Ici, les 2 variables *a* et *b* sont du [[type int]], soit un entier, et la variable retourné par cette fonction est aussi du même type.

# Assert
[[Assert]]
Les assertions sont des déclarations qui vérifient si une condition est vraie à un point donné du programme. Elles sont souvent utilisées pour vérifier la validité des entrées, des états intermédiaires ou des résultats de fonctionnement. L'utilisation d'assertions appropriées peut rendre le code plus robuste et plus sûr.

```python
def division(a: int, b: int) -> float:
    assert b != 0, "Le diviseur ne peut pas être zéro"
    return a / b
```

# Noms
Il est important de choisir des **noms de variables** et de **fonctions** **significatifs** qui reflètent leur **but** et leur **utilisation** dans le programme. Des noms bien choisis rendent le code plus **compréhensible** et **réduisent** le besoin de commentaires explicatifs excessifs.
De plus, les accents (é, ê, è ë, ...) sont **prohibés** meme si python les supportes.

## Utilisation

Pour cela, les fonctions, variables, ect... porte le nom qui **définit** le plus, et les mots sont séparé par __ puisqu'il n'est pas possible de mettre un espace dans un nom de variable

```python
def calculer_moyenne(liste_notes: List[float]) -> float:
    somme = sum(liste_notes)
    nombre_notes = len(liste_notes)
    return somme / nombre_notes 
```
