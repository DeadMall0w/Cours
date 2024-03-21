
![[test.js]]
<button id="toggleButton" onclick="toggleEmbed()">Afficher/Masquer</button>


<button id="ajouterLigne">Ajouter une ligne</button>```markdown
const toggleButton = document.getElementById('toggleEmbedButton');
    const embedContainer = document.getElementById('embedContainer');

    toggleButton.addEventListener('click', function() {
        if (embedContainer.style.display === 'none') {
            embedContainer.style.display = 'block';
        } else {
            embedContainer.style.display = 'none';
        }
    });
```

```dataviewjs

const button = document.getElementById('ajouterLigne');
const liste = document.getElementById('listeLignes');

button.addEventListener('click', function() {
    const nouvelleLigne = document.createElement('li');
    nouvelleLigne.textContent = "Nouvelle ligne ajoutée";
    liste.appendChild(nouvelleLigne);
});
```
```markdown
const button = document.getElementById('ajouterLigne');
const liste = document.getElementById('listeLignes');

button.addEventListener('click', function() {
    const nouvelleLigne = document.createElement('li');
    nouvelleLigne.textContent = "Nouvelle ligne ajoutée";
    liste.appendChild(nouvelleLigne);
});
```

```dataviewjs
console.log("hello");
const button = document.getElementById('ajouterLigne');

button.addEventListener('click', function() {
    console.log("CA FONCTIONNNNE !!!")
});

```
# test
Bonjour ceci devrait disparaître