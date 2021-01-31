<h1 align="center">Welcome to data-quality 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://opensource.org/licenses/BSD-3-Clause" target="_blank">
    <img alt="License: BSD--3--Clause" src="https://img.shields.io/badge/License-BSD--3--Clause-yellow.svg" />
  </a>
  <a href="https://twitter.com/LouisPerdereau" target="_blank">
    <img alt="Twitter: LouisPerdereau" src="https://img.shields.io/twitter/follow/LouisPerdereau.svg?style=social" />
  </a>
</p>

> Ce projet répond au problème posé dans le TP1 sur la qualité de la données

## Installation

```sh
pip install -r requirements.txt
```

## Usage

```sh
python3 app.py
```

## Comment nous avons corriger les erreurs dans le jeu de données
### Détection des erreurs
Sur le jeu de donnée nous avons deux types d'erreurs. Nous avons les erreurs de format et d'incohérence des données.
### Correction des erreurs de formats
Si la donnée n'est pas exploitable, alors nous faisons la moyenne entre les deux valeurs qui l'entoure. 
### Correction des erreurs incohérentes du fichier
Il y a des erreurs incohérentes dans le fichier des données, par exemple au mois d'août, nous avons une 48 °C qui ressort. Pour la détecter, nous nous sommes basé sur l'écart type entre les données, si une donnée n'est pas entre son prédécésseur moins et plus l'écart type du mois alors la données est mauvaise. Par exemple, si au mois de mars nous avons un écart type de 5 et que nous avons 15 °C, alors la prochaine valeur devra être en 10 et 20 °C, si elle est sort de la borne définie cela signifie que la données n'est pas bonne. Une fois détectés, nous faisons comme pour la correction d'erreur de formatn, nous faisons la moyenne entre les deux valeurs qui l'entoure
## Localisation du SI-Erreur
Nous supposons que les données du **SI-Erreur** proviennent d'Oslo ou Stockholm ou Helsinki.

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