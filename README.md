# Cahier des charges du jeu d'echec

## Palier 1 : Interface Graphique et JcJ fonctionnel

- Implémenter le joueur contre joueur sur la même machine.
- Affichage des pions.
- Contrôle des mouvements des pions avec le clavier (en indiquant les coordonnés A et B).
- Faire en sorte que le jeu refuse les coups impossibles. 
- Le jeu signale quand un joueur gagne, qu'il y a égalité ou pat.

## Palier 2 : Implémentation d'une IA basique

- Au lancement d'une partie le joueur peut choisir entre une partie contre une IA ou un autre Joueur.
- L'IA utilise l'euristique à un niveau pour choisir ses coups.

## Palier 3 : Sauvegarde 

- volution darwinienne des IA (avec des tournois).
- Bibliothèque d'ouvertures.
- Implementation d'un système de sauvegarde.
- Enregistrement et replay de la partie.
- Retour arrière.

## Palier 4

## Palier secret

- le robot joue aléatoirement

# Architecture Logicielle

Cette section contien la définition des classes et des types de variables.

## Piéces d'échiquier:

Les pièces d'échiquier sont représentés par des chaines de deux caractères. Le premier charactére représente **le type de la pièce** et le deuxiéme **sa couleur**.

ex : une tour noire "TN"

|lettre|couleur|
|:----:|-------|
|N     |Noir   |
|B     |Blanc  |

|lettre | type    |
|:-----:|---------|
| R	| Roi     |
<<<<<<< HEAD
| Q	| Reinne  |
=======
| Q	| Reine  |
>>>>>>> f94923d6af2b8862e237f11dae86a2140dc08b8b
| F	| Fou     |
| C	| Cavalier|
| T     | Tour    |
| P	| Pion    |

## Échiquier:


