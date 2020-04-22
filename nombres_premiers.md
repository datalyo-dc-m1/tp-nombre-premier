# Nombres premiers

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

Un *nombre premier* est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs. Ces deux diviseurs sont 1 et le nombre considéré.

Par exemple, 7 est premier car il ne possède que deux diviseurs (1 et 7).

Par opposition, on appelle *nombre composé* tout nombre entier qui possédent au moins trois diviseurs.
 
Par exemple, 4 est un nombre composé car il possède 3 diviseurs (1, 2 et 4)

Les vingt-cinq nombres premiers inférieurs à 100 sont : 

`2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, et 97`

De telles listes de nombres premiers inférieurs à une borne donnée, ou compris entre deux bornes, peuvent être obtenues grâce à diverses méthodes de calcul.

Mais on ne peut pas construire une liste exhaustive de tous les nombres premiers: il en existe une infinité!

La notion de nombre premier est une notion de base en arithmétique élémentaire. Il existe de nombreuses applications industrielles basée sur les nombres premiers: c'est le cas de certains systèmes cryptographiques et des méthodes de transmission de l'information.
Les nombres premiers sont également utilisés pour construire des tables de hachage et pour constituer des générateurs de nombres pseudo-aléatoires.

L'objectif est d'implémenter un programme qui donne une liste de `n` nombres premiers:

* L'utilisateur choisit un nombre de chiffres à afficher `n`
* Le programme calcule la liste les `n` premiers nombres premiers

Exemple: 

Si l'utilisateur choisit `n=5` alors le programme retourne `[2, 3, 5, 7, 11]`

## Modélisation

On souhaite modéliser le problème comme suit:

- une classe `Number` qui modélise un nombre entier strictement positif

La classe `Number` comporte un unique attribut: 

* la valeur du nombre

Elle dispose des méthodes suivantes:

* `is_divisible`: qui prend en paramètre un nombre entier `i` et indique si le nombre est divisible par `i`
* `is_prime`: qui indique si le nombre est premier. Nous implémenterons cette méthode dans la section __Test de primalité__.

## Test de primalité

On souhaite tout d'abord implémenter la méthode `is_prime`.

Soit `a` le nombre entier dont on souhaite tester s'il est premier.

L'algorithme se déroule de la manière suivante :
   
* on parcourt l'ensemble des valeurs `i` pouvant diviser `a` :
    * si `a` est divisible par `i` alors `a` n'est pas premier, on arrête le test

## Calculer la liste des n nombres premiers

Implémenter une fonction `get_primes` qui:

* prend en paramètre un entier `n`
* retourne une liste contenant les `n` premiers nombres premiers 

A l'aide de cette fonction, afficher la liste:

* de 5 nombres premiers
* de 25 nombres premiers
* de 1000 nombres premiers

## Tests unitaires

Ecrire des tests unitaires vérifiant le bon fonctionnement des méthodes et fonctions implémentées.

## Amélioration

Un nombre peut-il premier s'il est pair? Améliorer le programme en conséquence.
