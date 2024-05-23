# Introduction
Un dictionnaire est une collection non ordonnée de paires clé-valeur, où chaque clé est unique et associée à une valeur. En Python, les dictionnaires sont définis à l'aide des accolades `{}`.
Les valeurs peuvent être n'importe quelle [[types de variables]] par exemple : [[type int]], [[type float]], [[Liste]],[[Tuple]]...
Par contre les clés doivent être non mutable : [[Variables immuables]].

# Création d'un Dictionnaire
Vous pouvez créer un dictionnaire vide ou un dictionnaire avec des paires clé-valeur initiales :

```python
# Dictionnaire vide 
mon_dictionnaire = {}  
# Dictionnaire avec des paires clé-valeur 
etudiant = {
	"nom": "Alice",     
	"âge": 21,     
	"cours": ["Maths", "Informatique", "Physique"] 
}
```
# Accès aux Valeurs
Pour accéder à une valeur dans un dictionnaire, utilisez la clé correspondante entre crochets `[]` :

```python
# Accéder à la valeur associée à la clé "nom" 
nom_etudiant = etudiant["nom"] 
print(nom_etudiant)  # Output: Alice 

# Accéder à la liste des cours 
cours_etudiant = etudiant["cours"] 
print(cours_etudiant)  # Output: ['Maths', 'Informatique', 'Physique']
```

# Modification des Valeurs
Vous pouvez modifier les valeurs associées à une clé existante ou ajouter de nouvelles paires clé-valeur :

```python
# Modifier la valeur associée à la clé "âge" 
etudiant["âge"] = 22  

# Ajouter une nouvelle paire clé-valeur 
etudiant["adresse"] = "123 Rue Principale"`
```

# Suppression d'Éléments
Vous pouvez supprimer une paire clé-valeur à l'aide de la fonction `del` ou de la méthode `pop` :

```python
# Utiliser del pour supprimer la clé "adresse" 
del etudiant["adresse"]  

# Utiliser pop pour supprimer la clé "âge" et obtenir sa valeur 
age = etudiant.pop("âge") 
print(age)  # Output: 22
```

# Méthodes Utiles des Dictionnaires
Les dictionnaires en Python disposent de nombreuses méthodes utiles :

- `keys()`: Retourne une vue contenant les clés du dictionnaire.
- `values()`: Retourne une vue contenant les valeurs du dictionnaire.
- `items()`: Retourne une vue contenant les paires clé-valeur sous forme de tuples.
- `get(key, default)`: Retourne la valeur associée à la clé ou une valeur par défaut si la clé n'existe pas.
- `update(other_dict)`: Met à jour le dictionnaire avec les paires clé-valeur d'un autre dictionnaire.

Exemples :
```python
# Obtenir les clés du dictionnaire 
clés = etudiant.keys() print(clés)  # Output: dict_keys(['nom', 'cours'])  

# Obtenir les valeurs du dictionnaire 
valeurs = etudiant.values() print(valeurs)  # Output: dict_values(['Alice', ['Maths', 'Informatique', 'Physique']])  

# Obtenir les paires clé-valeur 
paires = etudiant.items() print(paires)  # Output: dict_items([('nom', 'Alice'), ('cours', ['Maths', 'Informatique', 'Physique'])])  

# Utiliser get pour obtenir la valeur associée à une clé 
nom = etudiant.get("nom") print(nom)  # Output: Alice  

# Utiliser get avec une valeur par défaut 
adresse = etudiant.get("adresse", "Adresse non trouvée") 
print(adresse)  # Output: Adresse non trouvée  

# Mettre à jour le dictionnaire 
nouveaux_détails = {"âge": 22, "adresse": "123 Rue Principale"} 
etudiant.update(nouveaux_détails) 
print(etudiant)  # Output: {'nom': 'Alice', 'cours': ['Maths', 'Informatique', 'Physique'], 'âge': 22, 'adresse': '123 Rue Principale'}`
```
#### Boucles sur les Dictionnaires
Vous pouvez parcourir les clés, les valeurs ou les paires clé-valeur d'un dictionnaire à l'aide de boucles `for` :

``` python
# Parcourir les clés 
for cle in etudiant:     
	print(cle)  
	
# Parcourir les valeurs 
for valeur in etudiant.values(): 
	print(valeur)  
	
# Parcourir les paires clé-valeur 

for cle, valeur in etudiant.items():     
	print(f"{cle}: {valeur}")`
```
# Utilisation des Dictionnaires

Les dictionnaires sont couramment utilisés pour :

- Stocker des données structurées et associatives.
- Implémenter des tables de recherche et des bases de données simples.
- Compter des occurrences d'éléments (par exemple, histogrammes).

Exemple d'un compteur d'occurrences :

```python
texte = "abracadabra" 
compteur = {}  
for lettre in texte:     
	if lettre in compteur:
	    compteur[lettre] += 1     
	else:
	    compteur[lettre] = 1 
	    
print(compteur)  # Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

# Conclusion
Les dictionnaires sont des structures de données puissantes et flexibles en Python, permettant de stocker et de manipuler des paires clé-valeur de manière efficace. En comprenant les différentes méthodes et techniques pour travailler avec les dictionnaires, vous pouvez écrire des programmes plus efficaces et plus faciles à comprendre.