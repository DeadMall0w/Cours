<button id="ajouterLigne">Ajouter une ligne</button>


```dataviewjs
document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById('ajouterLigne');
    const liste = document.getElementById('listeLignes');

    button.addEventListener('click', function() {
        const nouvelleLigne = document.createElement('li');
        nouvelleLigne.textContent = "Nouvelle ligne ajoutée";
        liste.appendChild(nouvelleLigne);
    });
});
```
