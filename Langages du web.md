## Introduction

Le Web est un système d'information hypertexte distribué, accessible via Internet. Il repose sur un ensemble de technologies et de langages de programmation pour la création, le design et l'interaction avec les sites Web. Trois langages principaux sont utilisés dans le développement Web : HTML, CSS et JavaScript.

## HTML (HyperText Markup Language)

### Définition

HTML est le langage de balisage standard utilisé pour la création et la structuration du contenu des pages Web. Il utilise des balises pour définir le sens et la structure du contenu.

### Structure de Base

Un document HTML de base comporte généralement les éléments suivants :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Titre de la Page</title>
</head>
<body>

    <!-- Contenu de la Page -->
    <h1>Titre Principal</h1>
    <p>Paragraphe de texte.</p>

</body>
</html>
```

### Principaux Éléments HTML

- `<html>` : Élément racine de la page.
- `<head>` : Contient les métadonnées de la page.
- `<title>` : Définit le titre de la page affiché dans la barre de titre du navigateur.
- `<body>` : Contient le contenu visible de la page.
- Balises de structuration : `<h1>` (titre), `<p>` (paragraphe), `<ul>` (liste non ordonnée), `<ol>` (liste ordonnée), etc.

## CSS (Cascading Style Sheets)

### Définition

CSS est un langage de feuilles de style utilisé pour définir l'apparence et la mise en forme du contenu HTML. Il permet de séparer la structure et la présentation d'une page Web.

### Utilisation

Les règles CSS sont définies sous forme de sélecteurs et de déclarations. Par exemple :

```css
/* Style du titre principal */
h1 {
    color: blue;
    font-size: 24px;
}

/* Style des paragraphes */
p {
    color: black;
    font-size: 16px;
}
```

### Sélecteurs CSS

- Sélecteurs d'éléments : `h1`, `p`, `div`, etc.
- Sélecteurs de classe : `.ma-classe`, `.important`, etc.
- Sélecteurs d'identifiant : `#mon-id`, `#en-tete`, etc.

## JavaScript

### Définition

JavaScript est un langage de programmation côté client utilisé pour ajouter des fonctionnalités interactives aux pages Web. Il permet de manipuler le contenu HTML, de réagir aux événements utilisateur et de communiquer avec le serveur.

### Utilisation

JavaScript peut être inclus directement dans le code HTML ou dans des fichiers séparés. Par exemple :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page avec JavaScript</title>
    <script>
        // Code JavaScript intégré
        alert('Bonjour, monde!');
    </script>
</head>
<body>
    <!-- Contenu de la page -->
</body>
</html>
```

### Principales Fonctionnalités

- Manipulation du DOM (Document Object Model) : Modification du contenu HTML et des styles CSS.
- Gestion des événements : Réponse aux actions de l'utilisateur comme les clics de souris ou les pressions de touches.
- Appels AJAX : Communication asynchrone avec le serveur pour mettre à jour dynamiquement le contenu de la page.

## Conclusion

HTML, CSS et JavaScript constituent les fondements du développement Web moderne. HTML est utilisé pour structurer le contenu, CSS pour le style et la mise en page, et JavaScript pour l'interactivité et la dynamique. La maîtrise de ces trois langages est essentielle pour créer des sites Web fonctionnels, esthétiques et interactifs.
