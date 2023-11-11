# philomathia

Ce projet a pour objectif d'explorer les concepts mathématiques de base à l'aide du langage de programmation Python en utilisant principalement la bibliothèque Numpy.   
Les mathématiques sont le fondement de la Data Science, en effet, elles fournissent les outils et les techniques nécessaires pour comprendre, modèliser et analyser les données.

## Contenu du projet
- Dans le ReadMe:
	- Veille scientifique : une introduction sur certaines notions mathématiques.
- Dans le notebook Python ``Philomathia.ipynb``:
  	- Algèbre linéaire : Manipulation de vecteurs et de matrices, application des opérations de bases : addition, soustraction, multiplication et inversion de matrices.   
Elles sont essentielles à la résolution de problèmes de modèlisation et d'optimisation.
	- Probabilités et statistiques : Introduction aux concepts de probabilité, calcul de probabilités distribution normale, échantillonnage aléatoire et estimation statistique.    
Concepts essentiels pour l'analyse exploratioire des données, la modélisation statique et l'interprétation des résultats.
	- Calcul de dérivées (calcul différentiel) : Calcul de dérivées symboliques de fonctions. Permet de comprendre comment les fonctions changent localement.   
 Les dérivées sont utilisées pour optimiser les modèles, trouver les points critiques et comprendre les taux de variation dans les données. Le calcul différentiel est également utilisé dans l'apprentissage automatique pour ajuster les paramètres des modèles.
- Dans les fichiers ``ctl.py`` et ``algotri.py``
  	- Aller plus loin... : Visualisation et simulation de la CLT ainsi qu'application de divers algorithme de tri.

## Veille scientifique

### 1. Un vecteur
Un vecteur est un segment orienté (une flèche) ayant pour extrémités un point de départ (ex. A) et un point d'arrivée (ex. B) possèdant trois éléments caractèristiques: 
	- sa direction (définition de ses extrémité, ex. A et B)
	- son sens: 2 sens sont possibles d'une extrémité à l'autre, soit A vers B, soit B 	vers A
	- sa norme (sa longueur, distance qui sépare A de B)
   
![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/4f488a5e-1883-421d-b909-9ae7f5c0c87c)

### 2. Une matrice
Une matrice est un tableau rectangulaire de nombres, de variables ou d'expressions mathématiques disposé en lignes (horizontalement) et en colonnes (verticalement).

![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/785db427-edfe-4e8c-97c9-60dafb1797f7)

### 3 Probabilité
- Une probabilité est une mesure mathématique qui représente la chance ou la possibilité qu'un événement se produise.
- Une loi de probabilité est une fonction qui décrit la répartition des probabilités pour chaque valeur possible aléatoire.
- Exemple(s):
	- La loi uniforme: elle attribue une probabilité égale à toutes les valeurs possibles d'une variable aléatoire dans un intervalle donné.
		Si on prend un dé à 6 faces équilibrées, alors le score obtenu en lançant le dé suite une loi uniforme sur l'intervalle 1-6.
	- La loi binominale: elle modèlise le nombre de succès dans une série d'expériences indépendantes et identiquement distribuées, où chaque expérience a deux résultats possibles (succès ou echec).   
		Exemple: Lancer un dé plusieurs fois et compter le nombre de fois où il affiche un certain nombre.
		Ou encore, lancer une pièce de monnaie plusieurs fois et compter le nombre de fois où elle atterrit sur l'une des face désignée en amont ("pile").

### 4. Des variables indépendantes
Une variable indépendante est une variable qui est manipulée ou contrôlée dans une expérience ou une étude scientifique afin d'observer son effet sur une autre variable, appelée variable dépendante.
Elle représente la cause ou la raison d'un résultat.   
Exemple:   
Dans une étude qui a pour but de déterminer l'effet de la température sur la pigmentation des plantes, la variable indépendante (la cause) est la température, tandis que la quantité de pigment ou de couleur est la variable dépendante (l'effet).

### 5. Une espérance, une variance et un écart type
- Une espérance est un terme utilisé en mathémathiques pour désigner la valeur moyenne d'une variable aléatoire.
Elle est calculée en prenant en compte la probabilité de chaque valeur possible de la variable et en multipliant chaque valeur par sa propabilité, puis en sommant le tout.
- Une variance est une mesure statistique qui quantifie la dispersion ou l'écart des valeurs d'un ensemble de données par rapport à leur moyenne.
Elle est la moyenne des carrés des écarts entre chaque valeur et la moyenne.
Elle est calculée en prenant la différence entre chaque caleur de la variable et son espérance, en les élevant au carré, en multipliant chaque résultat par la probabilité correspondante, puis en sommant le tout.
Elle est une mesure de la dispersion des valeurs autour de l'espérance.
- Un écart type est une mesure de dispersion qui indique à quel point les données d'un ensemble sont éloignées de la moyenne. Il permet de quantifier la variabilité des valeurs d'un échantillon ou d'une population.   
Elle est calculée de la manière qui suit:   
écart type = √(Σ(xi - x)² / N)   
où:    
	- xi est chaque donnée
	- x est la moyenne des données
	- N est le nombre total de données
Elle est la racine carrée de la variance.

Autrement dit, l'écart type est une mesure plus intuitive de la dispersion des données, alors que la variance est plus utilie dans les calculs statistiques.

### 6. Une corrélation linéaire
Une corrélation est une relation entre deux variables qui peut être représentée par une ligne droite sur un graphique. Elle indique la force et la direction de la relation entre les deux variables.
Cette droite prote le nom de "droite de régression".
- Une corrémation linéaire positive correstion à une corrélation dont la droite de régression a une pente positive.   
  ![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/7af162b9-9050-4859-b1f8-6ab1fe3358f0)

- une coorélation linéaire négative correspond à une corrélation dont la droite de régression a une pente négative.   
  ![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/e296d7d7-f331-47df-a8b7-521faf1b1e44)

- Une corrélation linéaire nulle correspond à une absence de corrélation.   
  ![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/76360194-8e59-41ef-952a-c06dd109e476)

### 7. Une moyenne, une médiane, un maximum, un minimum.
- En mathématiques, la moyenne est un outil de calcul permettant de résumer une liste de valeurs numérique en un seul nombre réel, indémendamment de l'ordre dans lequel la liste est donnée.
Elle est calculée en additionnant des données et en les divisant par leur nombre.
- En statistiques, la médiane est le nombre qui partage une série statistique en deux parties de même effectif.   
  ![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/3c7e102c-9783-4870-a689-abe2edbe2bed)
- un maximum est la valeur la plus grande atteinte par une quantité variable.
- un minimum est, dans un intervalle donné, la plus petite des valeurs. 

### 8. Les quartiles en statistique
En statistiques et en théorie des probabilités, les quantiles sont les valeurs qui divisent un jeu de données en intervalles de même probabilité. Il y a donc un quantile de moins que le nombre de groupes créés.
Un quartile est chacune des trois valeurs qui divisent les données triées en quatre part égales, de sorte que chaque partie représente 1/4 de l'échantillon de population.
![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/8c3e2897-653e-4f6c-84d5-a4871d793edb)

### 9. Boxplot en statistique
Un boxplot (également appelé boîte à moustache) en statistique descriptive est un type de graphique souvent utilisé dans l'analyse de données.
Il permet de résumer une variable de manière simple et visuel, d'identifier les valeurs extrêmes et de comprendre la répartition des observations.   
![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/d144006b-5edb-4b33-a9d6-a04666eda9bb)   
Sur cette représentation, on peut observer:
	- La valeur centrale, la médiane. Il existe autant de valeur supérieures qu'inférieures à cette valeur dans l'échantillon.
	- Les bords du rectangle, les quartiles. Pour le bord inférieur, un quart des observations ont des valeurs plus petites et trois quart ont des valeurs plus grandes. Le bord supérieur suit le même raisonnement.
	- Les extrémités des moustaches sont calculées en utilisant 1.5 fois l'espace interquartile (distance en le 1er et le 3e quartile.

On peut remarquer que 50% des observations se trouvent à l'intérieur de la boîte.
Les valeurs à l'extérieur des moustaches sont représentées par des points. On ne peut pas dire que si une observation est à l'extérieur des moustaches alors elles est une valeur aberrante. Par contre, cela indique qu'il faut étudier plus en détail cette observation.

### 10. Histogramme en statistique
Un histogramme en statistique est un type de graphique qui permet de représenter la répartition d'une variable quantitative* (continue ou discrète).
Il se compose de rectangles dont:
	- la largeur correspond à l'intervalle de classe 
	- la hauteur à l'effectif ou la fréquence de la classe
Il est utile pour visualiser la forme, le centre et la dispersion d'une distribution de données.

Voici un exemple de sa représentation:   
![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/a5d5debb-0cc1-43dc-ae40-b932d70feacc)

*Une variable quantitative peut être discrète ou continue. Une variable discrète a une valeur finie. Il est possible de les énumérer ( » 1, 2, 3,… »). Une variable continue peut prendre, en théorie, une infinité des valeurs, formant un ensemble continu. Par exemple, le temps de réussite d’une tache sera compris entre 0 et 300 secondes, et pourra prendre les valeurs 12,235689 ou 12,235699999.

Des variables discrètes :

* Le nombre d’items dans une liste.
* Le nombre de personnes dans une salle.
* On peut généralement l’énoncé sous la forme « Le nombre de… ».

Des variables continues :

* Le temps de réalisation d’une tâche.
* La taille, le poids d’une personne.
* La vitesse d’une voiture.

### 11. Le théorème Central Limite
Le théorème central limite est un résultat fondamental en probabilités et en statistiques qui énonce que:
sous certaintes conditions, la somme de variables aléatoires indépendantes et identiquement distribuées suit une loi normale*.   
Les conditions sont les suivantes:
- Les variables aléatoires doivent être indépendantes les unes des autres. (le résultat d'une variable n'influence pas le résultat des autres variables)
- Les variables aléatoires doivent suivre la même distribution de probabilité. (elles ont la même moyenne et la même variance)
- La taille d'échantillon doit être suffisamment grande. (généralement supérieure à 30, bien que pouvant varier selon le contexte)

Ce théorème est important en statistiques car il permet de modéiser et d'analyser des phènomènes complexes en utilisant des approximations basées sur la distribution normale, ce qui facilite l'interprétation des données et la prise de décisions éclairées.

Représentation de la loi normale (aussi appelée "courbe en cloche"):   
![image](https://github.com/marwan-rouissi/philomathia/assets/115158061/12f341d1-1944-43d5-8da0-882ea6faf291)


*loi normale: distribution de probabilité continue qui est symétrique et en forme de cloche.   
Elle est utilisée pour modéliser de nombreux phénomènes naturels et humains.

### 12. Une dérivée
La dérivée d'une fonction est le moyen de déterminer combien cette fonction varie quand la quantité dont elle dépend, son argument, change. 
Plus précisément, une dérivée est une expression (numérique ou algébrique) donnant le rapport entre les variations infinitésimales* de la fonction et les variations infinitésimales de son argument. Par exemple, la vitesse est la dérivée du déplacement par rapport au temps, et l'accélération est la dérivée, par rapport au temps, de la vitesse.

La notion de dérivée est une notion fondamentale en analyse fonctionnelle. Elle permet d'étudier les variations d'une fonction, de construire des tangentes à une courbe et de résoudre des problèmes d'optimisation.

*variation infinitésimale: notion mathématique qui représente la différence entre deux valeurs très proches l'une de l'autre.

## Ressources supplémentaires:
Quelques ressources utiles si vous souhaitez approfondir vos connaissances en mathématiques avec Python:
- Documentation officielle de Numpy :    https://numpy.org/doc/stable/user/absolute_beginners.html
- Tutoriel Python, calculs matriciels :   
https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-comment-faire-les-calculs-matriciels-avec-python#_Toc56715054
- Dérivation :   
https://www.studysmarter.fr/resumes/mathematiques/analyse-mathematiques/derivation/
- Calculer la dérivée en Python:   
https://www.delftstack.com/fr/howto/python/python-derivative/#d%C3%A9riv%C3%A9-avec-la-biblioth%C3%A8que-sympy-en-python

Les images utilisées pour illuster certaines des notions plus haut sont tirées d'internet et de sites sources.
