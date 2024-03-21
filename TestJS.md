<button id="toggleButton" onClick="toggleEmbed()">Afficher/Masquer l'embed</button> 

# Test
![[Test better embed#test]]

```dataviewjs
const embed = document.getElementById('test'); 
const toggleButton = document.getElementById('toggleButton');

console.log("CPICPI");

toggleButton.addEventListener('click', function() {
	console.log("test");
	if (embed.style.display == 'none') { 
		embed.style.display = 'block'; 
	} else { 
		embed.style.display = 'none'; 
	} 

} );

```
# T 2
