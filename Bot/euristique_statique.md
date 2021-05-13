# La terminologie
Cette section contient des termes et leurs définition que on s'accorde a utiliser,
pour ajouter une définition uriliser le format :

```
mot
: définition du mot
```
manger une piéce
: L'action de placer une piéce sur celle de sont adversaire de maniére a la supprimer de la partie.

sauver une piéce
: L'action d'empécher une piéce allié de se faire tué en tuant la piéce adverse la menasasant ou en en mettant une autre dans la route.

note (d'un coup)
: La note d'un coup est un nombre réel attribué a une action, plus la note est haute plus l'action sera bénéfique, a l'inverse si la notte est basse l'action se fait a perte.

une étoile de danger
: une étoile de danger
 
## Le poid des piéces
Le `poid` attribué a une piéce est sa "valeurs" stratégique.
Cette variable va être utilisée pour calculer la note des coups.

| type     | Poid |
|----------|:----:|
| Roi      |      |
| Reine    |      |
| Fou      |      |
| Cavalier |      |
| Tour     |      |
| Pion     |      |

## Les facteurs 
Les facteur sont des nombres réels, propre a chaque instance de `Bot`.

Facteur d'agresivité
: Le fait de capturer une piéce énnemie fait gagner `poid_piéce_mangée * facteur_agressivité`

Facteur perte
: Le fait de perdre un piéce fait gagner `-1 * poid_piéce_perdue * facteur_perte`

Facteur sauvetage
: Le nombre de point gagné en sauvant une piéce est égal a `poid_piéce_sauvée * facteur_sauvtage`

*(les trois facteur au dessus pourais raisonablement être réunis en un mais je les laisse car on pourrais avoir besoin de les séparer)*

Facteur Roi *(suggestion)*
: Facteur qui determine la punitivité de jouer le roi.


# Fonctionement

## Entrée et retour
A chaque tour le bot va recevoir un échiquier avec l'information de quel couleur il doit jouer et il devra renvoiyer un mouvment pour faire cela.

## Hypothése de méthode de réfléction

Algorytme de base *(va probablement servire de base aux autres)*:
1. Donner une note sur tous les coups <u>**possibles**</u> avec une évalutation légére (une méthode d'analyse avec peut de profondeur).
2. Tri les coups en fonction de leurs note.
3. Met de côté/supprime les coups les plus désaventageux de la liste.
4. Evalue a nouveau les coups les plus proffitables avec d'avantage de proffondeur et trier la liste, si des coups arrivent a égalité les réevaluer avec plus de profondeur.
5. Proposer le coup avec la note la plus haute au moteur, si le coup et refuser proposer le suivant et ainsi de suite.

Méthode "de la castagne"
: La méthode de la casatgne consiste a vérifier quelle piéce menace/protége quelle piéce sur l'échiqier. (mettre a jours)
