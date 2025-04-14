# Démo Onyxia x Vault : accéder à une API sécurisée

Ce dépôt contient une démonstration de l’utilisation de **Vault dans Onyxia** pour sécuriser et injecter une **clé API** dans un environnement de développement (Jupyter, VS Code, etc.).

L’exemple utilisé ici est l’API **OpenWeatherMap**, un service météo en ligne nécessitant une authentification par clé API.

## Contenu

- `openweather_vault_demo.py` – Notebook Python avec le code complet
- `README.md` – Ce fichier

## Objectif

- Stocker un secret (clé API) dans **Vault** via l’interface Onyxia
- Lancer un environnement avec injection automatique du secret
- Utiliser ce secret dans un script Python pour interroger une API sécurisée

## Étapes à suivre

1. Créer une clé API gratuite sur : https://openweathermap.org/api
2. Se rendre dans l’onglet **Vault** de l’interface Onyxia
3. Créer un secret :
   - Chemin : `openweathermap`
   - Clé : `OPENWEATHERMAP_API_KEY`
   - Valeur : votre clé API OpenWeatherMap
4. Lancer un environnement Python (Jupyter, VS Code...) sur Onyxia
5. Dans l’onglet **"Vault"**, inclure le chemin `openweathermap`
6. Dans l'onglet Git, cloner ce repository https://github.com/PACordonnier/python-vault-demo
6. Ouvrir le script `openweather_vault_demo.py`
7. Exécuter le code et observer la météo récupérée depuis l’API

## Résultat attendu

Affichage de la météo actuelle d'une ville donnée (description + température), récupérée dynamiquement depuis OpenWeatherMap.

## Bonnes pratiques

- Ne jamais écrire une clé API en dur dans le code
- Utiliser Vault pour centraliser la gestion des secrets
- Injecter les secrets via les environnements Onyxia

---
