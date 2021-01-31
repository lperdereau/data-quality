<h1 align="center">Welcome to data-quality 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://opensource.org/licenses/BSD-3-Clause" target="_blank">
    <img alt="License: BSD--3--Clause" src="https://img.shields.io/badge/License-BSD--3--Clause-yellow.svg" />
  </a>
</p>

> Ce projet répond au problème posé dans le TP1 sur la qualité de la données

<div style="text-align: justify">

## Pré-requis

Il est vivement recomandé d'utiliser [pyenv](https://github.com/pyenv/pyenv) afin d'avoir un environement python virtuel en Python 3.8.6.
Il vous permmettera la bonne execution du code et le partitionement de dépendance python nécéssaire.

De plus il nous à fallut adapter les fichiers de données fournit dans le sujet. Les versions modifiés sont disponnible dans `data/inputs/`.

## Installation

```sh
pip install -r requirements.txt
```

## Exercice 1

L'exercice 1 à pour but de répondre aux questions :
- calculer la moyenne, l'écart type, min /max par mois et le min / max pour l'année année
- Utiliser Python Scipy pour les pares mathématiques.

**Exécution**
```sh
python3 exo1.py --csv 'data/inputs/Climat - SI.csv'
```

Le résultat sera lisible dans le terminal éxécutant le programme

## Exercice 2

L'exercice 2 à pour but de répondre aux questions :
- Tracer les courbes de chaque mois avec une bibliothèque graphique python Matplotlib, 12 vues mensuelles et vue annuelle.
- Présenter la valeur lue en parcourant la courbe à l'aide du pointeur.
- Présenter les valeurs précédentes par mois glissant de 30 jours centré sur la valeur lue.

Par manque de compréhension du résultat attendu nous n'avons pas réaliser le dernier point.

**Exécution**
```sh
python3 exo2.py --csv 'data/inputs/Climat - SI.csv'
```

Le résultat sera lisible dans une interface qui s'ouvrira lors de l'exécution du programme. Si dessous un exemple de l'UI. En cliquant sur next vous accèderez au graphique du mois suivant le dernier graphique correspond au graphique des températures sur l'année.

![screenshot](docs/screenshot.png)

## Exercice 3

L'exercice 3 à pour but de répondre aux questions :

- Recommencez avec le jeu SI-erreur après avoir corrigé les valeurs en erreur. Précisez vos méthodes.
- Les données corrigées sont elles proches des valeurs sans erreur ?
- A partir de données opendata du second fichier, retrouver le type de climat.
- Reprendre les données typiques de la localisation proche fournies en complément dans le fichier `data/inputs/Savukoski kirkonkyla.csv`, comparer les écarts. Qu'en concluez vous ?
- De quelle capitale européenne avez vous eu les données ?


**Exécution**
```sh
python3 exo3.py --csv 'data/inputs/Climat - SI erreur.csv'
```

A la suite de cette execution un fichier sera disponnible `data/outputs/Climat - SI erreur.csv`.

Il sera donc possible de réexécuter les commande de l'éxercice 1 et 2 avec se nouveau fichier.

**Exécution**
```sh
python3 exo1.py --csv 'data/outputs/Climat - SI erreur.csv'
python3 exo2.py --csv 'data/outputs/Climat - SI erreur.csv'
```

### Comment nous avons corriger les erreurs dans le jeu de données
**Détection des erreurs**

Sur le jeu de donnée nous avons deux types d'erreurs. Nous avons les erreurs de format et d'incohérence des données.

**Correction des erreurs de formats**

Si la donnée n'est pas exploitable, alors nous faisons la moyenne entre les deux valeurs qui l'entoure. 

**Correction des erreurs incohérentes du fichier**

Il y a des erreurs incohérentes dans le fichier des données, par exemple au mois d'août, nous avons une 48 °C qui ressort. Pour la détecter, nous nous sommes basé sur l'écart type entre les données, si une donnée n'est pas entre son prédécésseur moins et plus l'écart type fois 3 du mois alors la données est mauvaise. Par exemple, si au mois de mars nous avons un écart type de 5 et que nous avons 15 °C, alors la prochaine valeur devra être en 0 et 30 °C, si elle est sort de la borne définie cela signifie que la données n'est pas bonne. Une fois détectés, nous faisons comme pour la correction d'erreur de formatn, nous faisons la moyenne entre les deux valeurs qui l'entoure

**Localisation du SI-Erreur**
Pour trouver la localisation, nous nous sommes basé sur plusieurs sites pour vérifier, nos sites sont:
 - https://nomadlist.com/climate-finder
 - https://www.infoclimat.fr/

Le premier sites, nous a permis de sortir une petite liste de ville. Le deuxième site quand a lui nous a permis de faire une vérification des données à la main.
Pour faire nos comparaisons, nous nous sommes basés sur la moyenne et l'écart type des mois. De plus, nous avons essayé de regarder les courbes par mois, mais cela est compliqué car nous nous sommes pas certains de nos données.

:warning: Il est difficile de se baser sur le minimum et le maximum car nous ne sommes pas sur des données fournis.

Nous supposons que les données du _"SI-Erreur"_ proviennent d'Oslo.

</div>

## Auteurs

👤 **Louis Perdereau**

* Twitter: [@LouisPerdereau](https://twitter.com/LouisPerdereau)
* Github: [@lperdereau](https://github.com/lperdereau)

👤 **Jérémy Chauvin**

* Twitter: [@SingeBob](https://twitter.com/SingeBob)
* Github: [@SingeBob](https://github.com/SingeBob)

## 📝 License

Copyright © 2021 [Louis Perdereau & Jérémy Chauvin](https://github.com/lperdereau).<br />
This project is [BSD--3--Clause](https://opensource.org/licenses/BSD-3-Clause) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_