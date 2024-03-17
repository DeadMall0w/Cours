$$DM$$
BERQUIER Raphaël 
TG1 

Remarques:



# Exercice 1

## 1.
 f sur ]0;+$\infty$] pour tout x > 0
 
$\dfrac{1 - 3x}{2 - x} \le f(x) \le \sqrt{9+\frac{1}{x}}$

$\lim_{x \rightarrow \infty} \frac{1-3x}{2-x}$  C'est une forme indéterminé du type "$\frac{-\infty}{-\infty}$"

$\dfrac{1 - 3x}{2 - x}  = \dfrac{x(\frac{1}{x} - 3)}{x(\frac{2}{x} - 1)} = \dfrac{\frac{1}{x} - 3}{\frac{2}{x} - 1} = \dfrac{-3}{-1} = 3$
Alors,
$\lim_{x \rightarrow \infty} \frac{1-3x}{2-x} = 3$

$X = \lim_{x \rightarrow \infty} 9+\frac{1}{x}$
$\lim_{X \rightarrow 9} \sqrt{X} = \sqrt{9} = 3$

Alors, d'après le théorème des gendarmes la fonction f tend vers 3.

## 2.
Quand x tend vers - $\infty$ :
$\dfrac{a\times e^x -3 }{e^x + b} = 0,6$

$\dfrac{a\times 0 -3 }{0 + b} = 0,6$

$\dfrac{-3 }{b} = 0,6$

$b = -5$


Quand x tend vers + $\infty$ :
$\dfrac{a\times e^x -3 }{e^x - 5} = 2$

$\dfrac{e^x\times (a - 3/e^x) }{e^x\times (1 - 5/e^x)} = 2$

$\dfrac{a - 3/e^x}{1 - 5/e^x} = 2$

D'après le cours, un nombre divisé par exponentielle de $x$ tend 0 quand $x$ tend vers l'infini.

$\dfrac{a}{1} = 2$
$a = 2$


Alors, 

$\dfrac{2\times e^x -3}{e^x - 5}$

# Exercice 2
P1 : tirer 3 boules de même couleur dans l'Urne 1.
$p(Tirer 3 blanches) = \frac{10}{20}\times\frac{9}{19}\times\frac{8}{18} = \frac{2}{19}$
$p(Tirer 3 rouges) = \frac{10}{20}\times\frac{9}{19}\times\frac{8}{18} = \frac{2}{19}$
$P1 = \frac{2}{19} + \frac{2}{19} = \frac{4}{19}$


P2 : tirer 3 boules de même couleur dans l'Urne 2.
$p(Tirer 3 blanches) = \frac{15}{20}\times\frac{14}{19}\times\frac{13}{18} = \frac{91}{228}$
$p(Tirer 3 rouges) = \frac{5}{20}\times\frac{4}{19}\times\frac{3}{18} = \frac{1}{114}$
$P2 = \frac{91}{228} + \frac{1}{114} = \frac{31}{76}$

$q = \frac{P1}{P2} =  \dfrac{\frac{4}{19}}{\frac{31}{76}} = \dfrac{16}{31}$


# Exercice 3)
$f(x) = \dfrac{e^{2x}-1}{e^{2x}+1}$
## 1)
## Quand $x$ tend vers $+\infty$
$\lim_{x \rightarrow +\infty} e^{2x}-1 = +\infty$
$\lim_{x \rightarrow +\infty} e^{2x}+1 = +\infty$

Il y a une forme indéterminée.
$\dfrac{e^{2x}-1}{e^{2x}+1} = \dfrac{e^{ex}(1-\frac{1}{e^{2x}})}{e^{ex}(1+\frac{1}{e^{2x}})}$
D'apres le cours, un nombre divisé par une exponentielle de x, tend vers 0.
Alors 
$\lim_{x \rightarrow +\infty} \dfrac{e^{2x}-1}{e^{2x}+1} = \dfrac{1}{1} = 1$

## Quand $x$ tend vers $-\infty$
$\lim_{x \rightarrow +\infty} e^{2x}-1 = -1$
$\lim_{x \rightarrow +\infty} e^{2x}+1 = 1$

Alors 
$\lim_{x \rightarrow +\infty} \dfrac{e^{2x}-1}{e^{2x}+1} = \dfrac{-1}{1} = -1$

## 2)
$f'(x) = \dfrac{u' \times v - u \times v'}{v^2}$
$f'(x) = \dfrac{2e^{2x}\times2e^{2x} + 2e^{2x}-(2e^{2x}\times2e^{2x} - 2e^{2x})}{(e^{2x}+1)^2}$
$f'(x) = \dfrac{2e^{2x} + 2e^{2x}}{(e^{2x}+1)^2}$
$f'(x) = \dfrac{4e^{2x}}{(e^{2x}+1)^2}$

$4e^{2x} > 0$ et $(e^{2x}+1)^2 > 0$
Alors cette dérivé est supérieur à 0, alors la fonction est croissante.


## 3)
$m = \dfrac{e^{2x}-1}{e^{2x}+1}$
$m \times (e^{2x} +1) = e^{2x}-1$
$m \times e^{2x} + m =  e^{2x}-1$
$m \times e^{2x} - e^{2x} = 1+m$
$e^{2x} \times (1 - m) = 1+m$ 
$e^{2x} = \dfrac{1+m}{(1 - m)}$ 
${2x} = \ln{\dfrac{1+m}{(1 - m)}}$
${x} = \dfrac{1}{2} \times \ln{\dfrac{1+m}{(1 - m)}}$ 



# Exercice 4)
## 1)
### a. 
Car -2 est le coefficient directeur de $y = -2x -1$
### b. 
On commence par trouver la dérivé de $f$.
$f(x) = e^{2x} - e^x + ax -1$
$f'(x) = 2e^{2x} - e^x + a$

$f'(0) = 2e^{2\times0} - e^0 + a$
$f'(0) = 2 - 1 + a$
$f'(0) = 1 + a$

Or, on a démontrer plus tôt que $f'(0) = -2$

$f'(0) = 1 + a$
$-2 = 1 + a$
$a = -3$

## 2)
### Quand $x$ tend vers + $\infty$ :
$\lim_{x \rightarrow \infty}  e^{2x} - e^x + -3x -1$ est une forme indéterminé du type "$\infty - \infty$"
$\lim_{x \rightarrow \infty} e^{x} \times (e^{x} - 1) + -3x -1$
$\lim_{x \rightarrow \infty} e^{x} \times (e^{x} - 1) = + \infty$
$\lim_{x \rightarrow \infty} -3x -1 = -\infty$
Il y a une forme indéterminé du type "$\infty - \infty$", mais d'après le cours l'exponentielle l'emporte sur toute puissance x. Alors,
$\lim_{x \rightarrow \infty}  e^{2x} - e^x + -3x -1 = +\infty$
### Quand $x$ tend vers - $\infty$ :
$\lim_{x \rightarrow -\infty}  e^{2x} - e^x = 0$ 
$\lim_{x \rightarrow -\infty}  -3x -1 = +\infty$
Alors, 
$\lim_{x \rightarrow -\infty}  e^{2x} - e^x + -3x -1 = +\infty$

## 3)
$f(x) = (2e^x -3)(e^x+1)$
$f(x) = 2e^x\times e^x + 2e^x\times 1 - 3e^x-3$
$f(x) = 2e^{2x}+ 2e^x- 3e^x-3$
$f'(x) = 2e^{2x} - e^x -3$

Et 
$f(x) = e^{2x} - e^x + -3x -1$
$f'(x) = 2e^{2x} - e^x -3$

## 4)
$2e^x -3 = 0$
$2e^x = 3$
$e^x = 1,5$
$x = \ln(1,5)$

$e^x+1=0$
$e^x=-1$
Une exponentielle ne peut pas être inferieur à 0, il n'y a pas de solution.


![[Tableau de variation.png]]


# Exercice 5)
## 1)
$p_2 = p(G_1 \cap G_2) + p(\overline{G_1} \cap G_2)$
$p_2 = 0,5 \times 0,75 + 0,25 \times 0,25$
$p_2 = \frac{7}{16}$


## 2)
a.
![[Pasted image 20231108210616.png]]
b.
$p_{n+1} = p(G_n \cap G_{n+1}) + p(\overline{G_n} \cap G_{n+1})$
$p_{n+1} = 0,25\times P_n + \frac{1}{2} \times (1- P_n)$
$p_{n+1} = 0,25P_n + \frac{1}{2} - 0,5P_n$
$p_{n+1} = -0,25P_n + \frac{1}{2}$

## 3)
$U_n = P_n - 0,4$
$-P_n = -U_n - 0,4$
$P_n = U_n + 0,4$



$U_n = P_n - 0,4$
$U_{n+1} = P_{n+1} - 0,4$
$U_{n+1} = -0,25P_n + \frac{1}{2} - 0,4$
$U_{n+1} = -0,25(U_n + 0,4) + 0,1$
$U_{n+1} = -0,25U_n - 0,1 + 0,1$
$U_{n+1} = -0,25U_n$
Alors $U_n$ est géométrique, de raison -0,25.


$U_1 = P_1 - 0.4$
$U_1 = 0,25 - 0,4$
$U_1 = 0,15$

$U_n = U_1 \times r^{n-1}$
$U_n = 0,15 \times (-0,25^{n-1})$

$P_n = U_n + 0,4$
$P_n = 0,15 \times -0,25^{n-1} + 0,4$

### c)
$\lim_{n \rightarrow +\infty} 0,15 \times -0,25^{n-1} + 0,4 = -\infty$

